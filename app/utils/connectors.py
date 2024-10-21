from motor.motor_asyncio import AsyncIOMotorClient, AsyncIOMotorDatabase
from pymongo import MongoClient
from pymongo.database import Database
from pymongo.errors import ConnectionFailure
from urllib.parse import urlparse, parse_qs

from app.config import settings
from app.logger import logger

class MongoDBConnector:
    # Async connections
    client: AsyncIOMotorClient = None
    db = None

    # Sync connections
    client_sync: MongoClient = None
    db_sync = None

    # Collections
    collections = ["users", "devices", "communities", "settings"]
    collections_indexes = [
        {
            "username": {"unique": True},
            "device_hash": {"unique": True},
            "status": 1,
        },
    ]

    # Environment variables
    URI: str = settings.mongodb_uri

    @classmethod
    def __init__(cls) -> None:
        # Async connection
        cls.client = None
        cls.db = None

        # Sync connection
        cls.client_sync = None
        cls.db_sync = None

    @staticmethod
    def get_db_name(uri) -> str | None:
        db_name = uri.split("/")[-1]
        if db_name:
            return db_name
        
        # extract from search params
        parsed_uri = urlparse(uri)
        query_params = parse_qs(parsed_uri.query)
        db_name = query_params.get('appName', [None])[0]
        return db_name if db_name else None

    @classmethod
    def __setup(cls, db: AsyncIOMotorDatabase | Database) -> None:
        for indexes_pos, collection in enumerate(cls.collections):
            # Create collections
            if collection not in db.list_collection_names():
                db.create_collection(collection)
                logger.success(f"Created collection '{collection}'")
            
            # Create indexes
            if len(cls.collections_indexes) > indexes_pos:
                for index, options in cls.collections_indexes[indexes_pos].items():
                    db[collection].create_index(index, **(options if type(options) == dict else {}))
                    logger.success(f"Created index '{index}' for collection '{collection}'")
    
    @classmethod
    async def connect(cls):
        if cls.db is not None:
            return cls.db
        
        try:
            cls.client = AsyncIOMotorClient(cls.URI)
            cls.db = cls.client[cls.get_db_name(cls.URI)]
            if cls.db is None:
                raise ConnectionFailure("Could not connect to MongoDB server (async)")

            logger.info(f"Connected to MongoDB at {cls.URI} (async)")
            
            cls.__setup(cls.db)
            return cls.db
        except ConnectionFailure as e:
            logger.critical(f"Could not connect to MongoDB server (async): {e._message}")
            return None
        
    @classmethod
    async def disconnect(cls):
        if cls.client is not None:
            cls.client.close()
            logger.info("Disconnected from MongoDB server (async)")
    
    @classmethod
    def connect_sync(cls):
        if cls.db_sync is not None:
            return cls.db_sync
        
        try:
            cls.client_sync = MongoClient(cls.URI)
            cls.db_sync = cls.client_sync[cls.get_db_name(cls.URI)]
            if cls.db_sync is None:
                raise ConnectionFailure("Could not connect to MongoDB server (sync)")

            logger.info(f"Connected to MongoDB at {cls.URI} (sync)")

            cls.__setup(cls.db_sync)
            return cls.db_sync
        except ConnectionFailure as e:
            logger.critical(f"Could not connect to MongoDB server (sync): {e._message}")
            return None

    @classmethod
    def disconnect_sync(cls):
        if cls.client_sync is not None:
            cls.client_sync.close()
            logger.info("Disconnected from MongoDB server (sync)")
