from db.models.common import TimestampModel, UUIDModel
from sqlmodel import Field, SQLModel

class User(UUIDModel, table=True):
    __tablename__ = "users"
    first_name: str 
    last_name: str
    email: str = Field(primary_key=True)
    password: str

    def __repr__(self):
        return f"<User (id: {self.id})>"
