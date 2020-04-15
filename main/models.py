import json


class NegativeValueException(Exception):
    pass


class Employee:

    def __init__(self, name: str, surname: str, salary: int = None, age: int = None):
        self.name = name
        self.surname = surname
        self._salary = salary
        self._age = age

    @property
    def salary(self):
        return self._salary

    @salary.setter
    def salary(self, value: int):
        if value < 0:
            raise NegativeValueException()
        self._salary = value

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value: int):
        if value < 0:
            raise NegativeValueException()
        self._age = value

    def to_json(self):
        return json.dumps(self.__dict__)

    def __repr__(self):
        return f'Employee(name={self.name}, surname={self.surname}, salary={self.salary} age={self.age})'
