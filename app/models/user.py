from beanie import Document

class UserModel(Document):
    username: str
    first_name: str
    last_name: str
