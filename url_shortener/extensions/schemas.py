from datetime import datetime

from pydantic import BaseModel
from pydantic import HttpUrl


class UrlSchema(BaseModel):
    """Url request body base schema"""

    original_url: HttpUrl


class UrlInfo(UrlSchema):
    """Url response body base schema"""

    reference_code: str
    creation_date: datetime
