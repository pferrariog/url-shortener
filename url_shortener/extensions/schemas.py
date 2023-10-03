from datetime import date

from pydantic import BaseModel
from pydantic import HttpUrl


class UrlSchema(BaseModel):
    """Url request body base schema"""

    url: HttpUrl


class UrlInfo(UrlSchema):
    """Url response body base schema"""

    encoded_url: HttpUrl
    creation_date: date
