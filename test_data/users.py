import random

_new_users = [
    ("user", "user", "test@mail.ru", "88005555555", "test", "test"),
    ("user1", "user1", "test1@mail.ru", "88015555555", "test1", "test1"),
    ("user2", "user2", "test2@mail.ru", "88025555555", "test2", "test2"),
    ("user3", "user3", "test3@mail.ru", "88035555555", "test3", "test3")
]

_users = [
    ("user", "bitnami"),
    ("test2@mail.ru", "test"),
    ("test3@mail.ru", "test"),

]


def get_new_user():
    return random.choice(_new_users)


def get_user():
    return random.choice(_users)


def get_admin():
    return _users[0]
