from bson import ObjectId
from pymongo.database import Database
import hashlib
import random

from connectors import MongoDBConnector
from validators import validate_db_connection
from ..config import settings

class PyObjectId(ObjectId):
    @classmethod
    def __get_validators__(cls):
        yield cls.validate
    
    @classmethod
    def validate(cls, v):
        if not ObjectId.is_valid(v):
            raise ValueError('Invalid ObjectId')
        return ObjectId(v)
    
    @classmethod
    def __modify_schema__(cls, field_schema):
        field_schema.update(type='string')


class UsernameGenerator:
    db: Database = None
    __hashed_app_name: str = None

    @classmethod
    def __init__(cls):
        cls.__hashed_app_name = hashlib.sha256(settings.project_name.encode()).hexdigest()
        cls.__initiate_db()
    
    @classmethod
    def __initiate_db(cls):
        if cls.db is not None:
            return cls.db
        
        cls.db = MongoDBConnector().connect_sync()
        validate_db_connection(cls.db)

    @property
    def __prefix(self):
        return ''.join(random.sample(self.__hashed_app_name, 6))
    
    @property
    def __assignable_number(self):
        # get the last user
        last_user = self.db.users.find_one(sort=[('created_at', -1)])
        if last_user is None:
            return 1
        
        # get the user's username
        username = last_user.get('username')
        last_user_number = username.split('_')[-1]
        
        # convert from hex to int
        new_assignable_number = int(last_user_number, 16)
        return hex(new_assignable_number + 1)[2:]

    def __str__(self):
        return f'{self.__prefix}_{self.__assignable_number}'
