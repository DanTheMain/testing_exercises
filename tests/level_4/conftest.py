import os
import string
import tempfile
import pytest
from random import choice
from faker import Faker
from functions.level_4.two_students import Student


fake = Faker()


@pytest.fixture
def temp_file():
    fpath = tempfile.TemporaryFile().name
    yield os.path.abspath(fpath)
    os.remove(fpath)


@pytest.fixture
def create_temp_file(temp_file):

    def inner(file_contents: str):
        with open(temp_file, "w") as file:
            file.writelines(file_contents)

        return temp_file

    return inner


@pytest.fixture
def test_file():

    def inner(file_contents: str | None = None):
        fpath = 'temp_config.properties'
        with open(fpath, 'w') as file:
            file.writelines(file_contents or '[default section]')

        yield fpath

        os.remove(fpath)

    return inner


@pytest.fixture
def promocode_test_char():
    return choice(string.ascii_uppercase)


@pytest.fixture
def promocode_test_len():
    return choice(range(1, 100))


@pytest.fixture
def generate_test_promocode(promocode_test_len, promocode_test_char):
    return promocode_test_char * promocode_test_len



@pytest.fixture
def student_first_name():
    return fake.first_name()


@pytest.fixture
def student_last_name():
    return fake.last_name()


@pytest.fixture()
def generate_telegram_account_and_username():

    def inner():
        account = f'{fake.ascii_safe_email()}'
        return account, account.strip('@')

    return inner


@pytest.fixture
def generate_test_student(student_first_name, student_last_name, generate_telegram_account_and_username):

    def inner(first_name: str | None, last_name: str | None, telegram_account: str | None):
        return Student(
            first_name=first_name or student_first_name,
            last_name=last_name or student_last_name,
            telegram_account=telegram_account if telegram_account else generate_telegram_account_and_username()[0]
        )

    return inner


@pytest.fixture
def generate_test_students(generate_test_student):

    def inner(student_amount: int):
        return [generate_test_student() for _ in range(student_amount)]

    return inner

