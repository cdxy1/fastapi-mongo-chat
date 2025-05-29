from beanie import Document


class UserModel(Document):
    username: str
    first_name: str
    last_name: str
    
    class Settings:
        name = "users"
        
    class Config:
        schema_extra = {
            "example": {
                "username": "JohnDoe123",
                "first_name": "John",
                "last_name": "Doe"
            }
        }
