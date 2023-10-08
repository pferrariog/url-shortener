from datetime import datetime

from pydantic import BaseModel
from pydantic import HttpUrl


class UrlSchema(BaseModel):
    """Url request body base schema"""

    original_url: HttpUrl


class UrlInfo(UrlSchema):
    """Url response body base schema"""

    reference_code: str  # TODO maybe add an alias optional request body field?
    creation_date: datetime


class UrlExists(UrlInfo):
    """Url response body if already exists"""

    message: str
