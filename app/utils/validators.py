import validators
from fastapi import HTTPException, status

def validate_db_connection(db):
    if db is None:
        raise HTTPException(
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
            detail="Database connection not available",
        )