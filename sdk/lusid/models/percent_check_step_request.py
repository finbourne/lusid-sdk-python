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


from typing import Any, Dict
from pydantic.v1 import Field, StrictStr, constr, validator
from lusid.models.compliance_step_request import ComplianceStepRequest

class PercentCheckStepRequest(ComplianceStepRequest):
    """
    PercentCheckStepRequest
    """
    label: constr(strict=True, max_length=64, min_length=1) = Field(..., description="The label of the compliance step")
    compliance_step_type_request: StrictStr = Field(..., alias="complianceStepTypeRequest", description=". The available values are: FilterStepRequest, GroupByStepRequest, GroupFilterStepRequest, BranchStepRequest, CheckStepRequest, PercentCheckStepRequest")
    additional_properties: Dict[str, Any] = {}
    __properties = ["complianceStepTypeRequest", "label"]

    @validator('label')
    def label_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if not re.match(r"^[a-zA-Z0-9\-_]+$", value):
            raise ValueError(r"must validate the regular expression /^[a-zA-Z0-9\-_]+$/")
        return value

    @validator('compliance_step_type_request')
    def compliance_step_type_request_validate_enum(cls, value):
        """Validates the enum"""
        if value not in ('FilterStepRequest', 'GroupByStepRequest', 'GroupFilterStepRequest', 'BranchStepRequest', 'CheckStepRequest', 'PercentCheckStepRequest'):
            raise ValueError("must be one of enum values ('FilterStepRequest', 'GroupByStepRequest', 'GroupFilterStepRequest', 'BranchStepRequest', 'CheckStepRequest', 'PercentCheckStepRequest')")
        return value

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
    def from_json(cls, json_str: str) -> PercentCheckStepRequest:
        """Create an instance of PercentCheckStepRequest from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                            "additional_properties"
                          },
                          exclude_none=True)
        # puts key-value pairs in additional_properties in the top level
        if self.additional_properties is not None:
            for _key, _value in self.additional_properties.items():
                _dict[_key] = _value

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> PercentCheckStepRequest:
        """Create an instance of PercentCheckStepRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return PercentCheckStepRequest.parse_obj(obj)

        _obj = PercentCheckStepRequest.parse_obj({
            "compliance_step_type_request": obj.get("complianceStepTypeRequest"),
            "label": obj.get("label")
        })
        # store additional fields in additional_properties
        for _key in obj.keys():
            if _key not in cls.__properties:
                _obj.additional_properties[_key] = obj.get(_key)

        return _obj