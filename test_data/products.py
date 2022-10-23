import random

_products = [
    ("What is Lorem Ipsum", "Lorem Ipsum is simply dummy text of the printing and typesetting industry", "Lorem Ipsum"),
    ("Why do we use it", "It is a long established fact that a reader will be distracted", "Use it"),
    ("Some", "test", "I love cats")
]


def get_product():
    return random.choice(_products)
