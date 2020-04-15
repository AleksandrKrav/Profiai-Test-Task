import logging
from typing import List, Optional, Tuple

from django.db import connection, DatabaseError

from main.models import Employee

logger = logging.getLogger(__name__)


class EmployeeServiceDataBaseException(Exception):
    pass


class EmployeeService:

    @staticmethod
    def save(employee: Employee):
        empl_json = employee.to_json()
        try:
            with connection.cursor() as cursor:
                cursor.callproc('creator', (empl_json,))
        except DatabaseError:
            logger.error('Failed to save employee to database', extra={
                'employee_json': empl_json,
            })
            raise EmployeeServiceDataBaseException()

    @classmethod
    def get(cls, **kwargs) -> Optional[List[Employee]]:
        sql, parameters = cls._form_sql_query(**kwargs)

        try:
            with connection.cursor() as cursor:
                cursor.execute(sql, parameters)
                cursor_data = cursor.fetchall()
                data = cls._dictfetchall(cursor.description, cursor_data)
        except DatabaseError:
            logger.exception('Failed get employee from database', extra={
                'sql': sql,
                'parameters': parameters
            })
            raise EmployeeServiceDataBaseException()

        result = []
        for employee in data:
            result.append(
                Employee(
                    employee['name'],
                    employee['surname'],
                    employee['age'],
                    employee['salary']
                ))

        return result

    @classmethod
    def _form_sql_query(self, **kwargs) -> Tuple[str, dict]:
        sql = 'SELECT name, surname, age, salary FROM person WHERE '
        filters = []
        parameters = dict()

        if kwargs.get('id') is not None:
            filters.append('id = %(id)s')
            parameters['id'] = kwargs.get('id')
        if kwargs.get('name') is not None:
            filters.append('name = %(name)s')
            parameters['name'] = kwargs.get('name')
        if kwargs.get('surname') is not None:
            filters.append(f'surname = %(surname)s')
            parameters['surname'] = kwargs.get('name')
        if kwargs.get('age') is not None:
            filters.append(f'age = %(age)s')
            parameters['age'] = kwargs.get('age')
        if kwargs.get('salary') is not None:
            filters.append(f'salary = %(salary)s')
            parameters['salary'] = kwargs.get('salary')
        sql += ' AND '.join(filters)
        return sql, parameters

    @classmethod
    def _dictfetchall(cls, description, cursor_data):
        columns = [col[0] for col in description]
        return [
            dict(zip(columns, row))
            for row in cursor_data
        ]
