from datetime import datetime

from pydantic import BaseModel
from pydantic import HttpUrl


class UrlSchema(BaseModel):
    """Url request body base schema"""

    original_url: HttpUrl
    reference_code: str = None


class UrlInfo(UrlSchema):
    """Url response body base schema"""

    creation_date: datetime


class UrlExists(UrlInfo):
    """Url response body if already exists"""

    message: str
