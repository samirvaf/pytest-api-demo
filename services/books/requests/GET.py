import requests
from config.base_config import BaseConfig


def all_books():
    return requests.get(BaseConfig.BASE_URL)
