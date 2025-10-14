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