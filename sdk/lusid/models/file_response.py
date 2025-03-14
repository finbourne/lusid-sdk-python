# coding: utf-8

"""
    LUSID API

    FINBOURNE Technology  # noqa: E501

    Contact: info@finbourne.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import Any, Dict, Optional, Union
from pydantic.v1 import StrictStr, Field, BaseModel, Field, StrictBytes, StrictStr 

class FileResponse(BaseModel):
    """
    Allows a file (represented as a stream) to be returned from an Api call  # noqa: E501
    """
    file_stream: Optional[Union[StrictBytes, StrictStr]] = Field(None, alias="fileStream")
    content_type:  Optional[StrictStr] = Field(None,alias="contentType") 
    downloaded_filename:  Optional[StrictStr] = Field(None,alias="downloadedFilename") 
    __properties = ["fileStream", "contentType", "downloadedFilename"]

    class Config:
        """Pydantic configuration"""
        allow_population_by_field_name = True
        validate_assignment = True

    def __str__(self):
        """For `print` and `pprint`"""
        return pprint.pformat(self.dict(by_alias=False))

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.dict(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> FileResponse:
        """Create an instance of FileResponse from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # set to None if file_stream (nullable) is None
        # and __fields_set__ contains the field
        if self.file_stream is None and "file_stream" in self.__fields_set__:
            _dict['fileStream'] = None

        # set to None if content_type (nullable) is None
        # and __fields_set__ contains the field
        if self.content_type is None and "content_type" in self.__fields_set__:
            _dict['contentType'] = None

        # set to None if downloaded_filename (nullable) is None
        # and __fields_set__ contains the field
        if self.downloaded_filename is None and "downloaded_filename" in self.__fields_set__:
            _dict['downloadedFilename'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> FileResponse:
        """Create an instance of FileResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return FileResponse.parse_obj(obj)

        _obj = FileResponse.parse_obj({
            "file_stream": obj.get("fileStream"),
            "content_type": obj.get("contentType"),
            "downloaded_filename": obj.get("downloadedFilename")
        })
        return _obj
