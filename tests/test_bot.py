import pytest
import telebot
from telebot import types


@pytest.fixture()
def telegram_bot():
    return telebot.TeleBot("", threaded=False)


@pytest.fixture
def private_chat():
    return types.Chat(id=11, type="private")


@pytest.fixture
def user():
    return types.User(id=10, is_bot=False, first_name="Some User")


@pytest.fixture()
def message(user, private_chat):
    params = {"text": "/start"}
    return types.Message(
        message_id=1, from_user=user, date=None, chat=private_chat, content_type="text", options=params, json_string=""
    )


def test_welcome():
    assert True
