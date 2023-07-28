from enum import IntEnum
from telebot import types
from peewee import Model, BigIntegerField, CharField, IntegerField, SqliteDatabase, DateField, ForeignKeyField
from __future__ import annotations

database = SqliteDatabase("mydatabase.db")


def create_table_in_database() -> None:
    database.create_tables(
        [
            Users,
        ]
    )


class UserStates(IntEnum):
    """
    Class in which all possible status for user state are created.
    """

    WAIT_FOR_TRANSIT_PERIOD = 1
    WAIT_FOR_AIRPORT = 2
    WAIT_FOR_START = 3
    WAIT_FOR_HOME = 4
    WAIT_FOR_DATA_HOME_DEPARTURE = 5
    WAIT_FOR_CIRCLE_OR_NOT = 6
    WAIT_FOR_FINISH_DEPARTURE_FIRST_FROM_PERIOD = 7
    WAIT_FOR_CHOOSE = 8
    WAIT_FOR_HATE_AIRL = 9
    WAIT_FOR_END = 10
    WAIT_FOR_FINISH_AIRPORT = 11
    WAIT_FOR_MORE_TICKETS = 12
    WAIT_FOR_SECOND_DATE_FROM_PERIOD_HOME = 13
    WAIT_FOR_FIRST_DATE_FROM_PERIOD_HOME = 14
    WAIT_FOR_DATE_OR_PERIOD_FROM_HOME = 15
    WAIT_FOR_DATE_OR_PERIOD_TO_FINISH = 16
    WAIT_FOR_SECOND_DATE_FROM_PERIOD_FINISH = 17


class Users(Model):
    user_id = BigIntegerField(primary_key=True)  # 0
    username = CharField()  # 1
    full_name = CharField()  # 2
    states = IntegerField(choices=((el.value, el.name) for el in UserStates))  # 3
    start_date = DateField()  # 4
    end_date = CharField()  # 5
    start_period = CharField()  # 6
    end_period = CharField()  # 7
    home = CharField()  # 8
    finish = CharField()  # 9
    hate_airl = CharField()  # 10

    class Meta:
        database = database

    @classmethod
    def create_from_message(cls, message: types.Message) -> tuple[Users, bool]:
        user, created = cls.get_or_create(
            user_id=message.from_user.id, username=message.from_user.username, full_name=message.from_user.full_name
        )
        return user, created


class UserAirports(Model):
    user_id = ForeignKeyField(Users)
    airport = CharField()

    class Meta:
        database = database


class UsersTranzit(Model):
    user_id = ForeignKeyField(Users)
    airport = CharField()
    duration = CharField()

    class Meta:
        database = database
