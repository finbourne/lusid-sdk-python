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


from typing import Any, Dict, Optional
from pydantic.v1 import BaseModel, Field, StrictStr

class GroupReconciliationUserReviewAdd(BaseModel):
    """
    GroupReconciliationUserReviewAdd
    """
    break_code: Optional[StrictStr] = Field(None, alias="breakCode", description="The break code of the reconciliation result.")
    match_key: Optional[StrictStr] = Field(None, alias="matchKey", description="The match key of the reconciliation result.")
    comment_text: Optional[StrictStr] = Field(None, alias="commentText", description="User's comment regarding the reconciliation result.")
    __properties = ["breakCode", "matchKey", "commentText"]

    class Config:
        """Pydantic configuration"""
        allow_population_by_field_name = True
        validate_assignment = True

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.dict(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> GroupReconciliationUserReviewAdd:
        """Create an instance of GroupReconciliationUserReviewAdd from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # set to None if break_code (nullable) is None
        # and __fields_set__ contains the field
        if self.break_code is None and "break_code" in self.__fields_set__:
            _dict['breakCode'] = None

        # set to None if match_key (nullable) is None
        # and __fields_set__ contains the field
        if self.match_key is None and "match_key" in self.__fields_set__:
            _dict['matchKey'] = None

        # set to None if comment_text (nullable) is None
        # and __fields_set__ contains the field
        if self.comment_text is None and "comment_text" in self.__fields_set__:
            _dict['commentText'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> GroupReconciliationUserReviewAdd:
        """Create an instance of GroupReconciliationUserReviewAdd from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return GroupReconciliationUserReviewAdd.parse_obj(obj)

        _obj = GroupReconciliationUserReviewAdd.parse_obj({
            "break_code": obj.get("breakCode"),
            "match_key": obj.get("matchKey"),
            "comment_text": obj.get("commentText")
        })
        return _obj