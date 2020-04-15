import logging

from django.core.management import BaseCommand

from main.models import Employee
from main.services import EmployeeService, EmployeeServiceDataBaseException

logger = logging.getLogger(__name__)


class Command(BaseCommand):
    help = 'Generate employee'

    def add_arguments(self, parser):
        parser.add_argument(
            '--action',
            choices=['create', 'get'],
            default='create',
            type=str,
            help='Choose action for employee. Variants: [create, get]',
        )

    def handle(self, *args, **options):
        if options['action'] == 'create':
            self.create()
        else:
            self.get()

    def create(self):
        logger.info('Create employee with all parameters')
        e = Employee('Alex', 'Karpenko', 1000, 26)
        try:
            EmployeeService.save(e)
        except EmployeeServiceDataBaseException:
            logger.error('Failed create employee with all params')

        logger.info('Create employee with required fields.')
        e = Employee('Alex', 'Kravchuk')
        try:
            EmployeeService.save(e)
        except EmployeeServiceDataBaseException:
            logger.error('Failed create employee with required fields.')

        logger.info('Create employee with non validate fields.')
        e = Employee('Alex', 'Kravchuk', 100000000000)
        try:
            EmployeeService.save(e)
        except EmployeeServiceDataBaseException:
            logger.info('Failed create employee with non validate fields.')

    def get(self):
        logger.info('Get data from database by name=Alex')
        try:
            result = EmployeeService.get(name='Alex')
            logger.info(f'Result: {result}')
        except EmployeeServiceDataBaseException:
            logger.error('Failed get data by Alex name')
