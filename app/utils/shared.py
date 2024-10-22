from bson import ObjectId
from pymongo.database import Database
import hashlib
import random
from PIL import Image, ImageDraw, ImageFont
import os
from io import BytesIO

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


"""
    This class is used to generate avatars for users. The avatars are generated using the user's username.
    The class generates a random background color and a text with the first letter of the username.

    Adapted from: https://github.com/maethor/avatar-generator/blob/b6cce9a1d3eac770555ed944d3d1caa48424bed4/avatar_generator/__init__.py
"""
class AvatarGenerator:
    FONT_COLOR = (255, 255, 255)
    MIN_RENDER_SIZE = 512

    @staticmethod
    def __background_color(s: int) -> tuple:
        random.seed(s)
        r = g = b = 255
        while r + g + b > 255*2:
            r = random.randint(0, 255)
            g = random.randint(0, 255)
            b = random.randint(0, 255)

        return r, g, b
    
    @staticmethod
    def __font(size: int) -> ImageFont.FreeTypeFont:
        path = os.path.join(os.path.dirname(__file__), 'fonts', 'Roboto-Regular.ttf')
        return ImageFont.truetype(path, size=int(0.8 * size))
    
    @staticmethod
    def __text(text: str) -> str:
        return text[0].upper() if text else '#'
    
    @staticmethod
    def __text_position(size: int, text: str, font: ImageFont.FreeTypeFont) -> tuple:
        left, top, right, bottom = font.getbbox(text)

        width = right - left
        left = (size - width) / 2.0

        height = bottom - top
        top = (size - height) / 5.5

        return left, top
    
    @classmethod
    def generate(cls, size: int, string: str, filetype='PNG') -> bytes:
        render_size = max(size, cls.MIN_RENDER_SIZE)
        image = Image.new('RGB', (render_size, render_size), cls.__background_color(string))
        draw = ImageDraw.Draw(image)

        font = cls.__font(size)
        text = cls.__text(string)
        draw.text(
            cls.__text_position(render_size, text, font),
            text,
            fill=cls.FONT_COLOR,
            font=font
        )

        stream = BytesIO()
        image = image.resize((size, size), Image.Resampling.LANCZOS)
        image.save(stream, format=filetype, optimize=True)
        return stream.getvalue()
    
    def random(self):
        return self.generate(
            random.randint(128, 512),
            UsernameGenerator(),
            random.choice(['PNG', 'JPEG'])
        )

