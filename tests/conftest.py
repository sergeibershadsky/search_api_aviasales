import pytest
import db
from db import create_table_in_database


def pytest_configure(config):
    from peewee import SqliteDatabase

    db.database = SqliteDatabase(":memory:")


@pytest.fixture(autouse=True)
def create_tables():
    create_table_in_database()
