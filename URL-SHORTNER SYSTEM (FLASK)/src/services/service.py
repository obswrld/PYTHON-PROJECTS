import random
import string
from data.model.url import Url
from data.repositories.url_repo import UrlRepository
from utils.mapper.url_mapper import UrlMapper

class UrlService:
    def __init__(self, url_repository=None):
        self.url_repository = url_repository if url_repository else UrlRepository()

    @staticmethod
    def generate_short_url(length: int = 6):
        char = string.ascii_letters + string.digits
        return ''.join(random.choice(char) for _ in range(length))

    @staticmethod
    def shorten_url(self, original_url: str):
        short_url = self.generate_short_url()
        url = Url(original_url=original_url, short_url=short_url)
        self.url_repository.save(url)
        return UrlMapper.to_dict(url)

    @staticmethod
    def get_by_short_url(self, short_url: str):
        short_url = self.url_repository.find_by_short_url(short_url)
        if short_url:
            return UrlMapper.to_dict(short_url)
        else:
            return None

    @staticmethod
    def get_by_original_url(self, original_url: str):
        short_url = self.url_repository.find_by_original_url(original_url)
        if short_url:
            return UrlMapper.to_dict(short_url)
        else:
            return None

    @staticmethod
    def delete_by_short_url(self, short_url: str):
        short_url = self.url_repository.delete_by_short_url(short_url)

    @staticmethod
    def clean_expired_url(self):
        return self.url_repository.delete_url_expired_url()