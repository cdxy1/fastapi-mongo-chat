from pymongo import AsyncMongoClient


class MongoDB:
    _CLIENT = AsyncMongoClient()
    _DATABASE = _CLIENT["TEMPORARY"]
    
    @classmethod
    def collection_factory(cls, collection: str) -> None:
        return cls._CLIENT[cls._DATABASE][collection]
