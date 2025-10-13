from config.config import url_collection
from src.config.config import url_collection
from src.data.model.url import Url
from pymongo.errors import PyMongoError

class UrlRepository:
    def __init__(self, collection=url_collection):
        self.collection = collection

    def save(self, url: Url):
        try:
            data = url.to_dict()
            result = self.collection.insert_one(data)
            return str(result.inserted_id)
        except PyMongoError as e:
            print(f"Error saving url: {e}")
        return None