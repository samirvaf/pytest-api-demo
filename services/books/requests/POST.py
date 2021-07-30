import os

import requests

from config.base_config import BaseConfig


def add_user():
    new_user_data = open(os.path.join(os.getcwd(), 'services', 'books', 'payloads', 'add-book.json'), 'r').read()
    return requests.post(BaseConfig.BASE_URL, new_user_data)
