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

    def find_by_shortened_url(self, shortened_url: str) -> Url:
        try:
            result = self.collection.find_one({"shortened_url": shortened_url})
            if result:
                return Url(url_id=result["_id"],
                           shortened_url=result["shortened_url"],
                           original_url=result["original_url"],
                           created_at=result["created_at"],
                           expires_at=result["expires_at"]
                           )
            return None
        except PyMongoError as e:
            print(f"Error finding url: {e}")
            return None

    def find_by_original_url(self, original_url: str) -> Url:
        try:
            result = self.collection.find_one({"original_url": original_url})
            if result:
                return Url(url_id=result["_id"],
                           original_url=result["original_url"],
                           shortened_url=result["shortened_url"],
                           created_at=result["created_at"],
                           expires_at=result["expires_at"]
                           )
            return None
        except PyMongoError as e:
            print(f"Error finding url: {e}")
            return None