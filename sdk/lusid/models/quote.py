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

from datetime import datetime
from typing import Any, Dict, Optional, Union
from pydantic.v1 import StrictStr, Field, BaseModel, Field, StrictFloat, StrictInt, StrictStr, constr 
from lusid.models.metric_value import MetricValue
from lusid.models.quote_id import QuoteId

class Quote(BaseModel):
    """
    The quote id, value and lineage of the quotes all keyed by a unique correlation id.  # noqa: E501
    """
    quote_id: QuoteId = Field(..., alias="quoteId")
    metric_value: Optional[MetricValue] = Field(None, alias="metricValue")
    lineage:  Optional[StrictStr] = Field(None,alias="lineage", description="Description of the quote's lineage e.g. 'FundAccountant_GreenQuality'.") 
    cut_label:  Optional[StrictStr] = Field(None,alias="cutLabel", description="The cut label that this quote was updated or inserted with.") 
    uploaded_by:  StrictStr = Field(...,alias="uploadedBy", description="The unique id of the user that updated or inserted the quote.") 
    as_at: datetime = Field(..., alias="asAt", description="The asAt datetime at which the quote was committed to LUSID.")
    scale_factor: Optional[Union[StrictFloat, StrictInt]] = Field(None, alias="scaleFactor", description="An optional scale factor for non-standard scaling of quotes against the instrument. For example, if you wish the quote's Value to be scaled down by a factor of 100, enter 100. If not supplied, the default ScaleFactor is 1.")
    __properties = ["quoteId", "metricValue", "lineage", "cutLabel", "uploadedBy", "asAt", "scaleFactor"]

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
    def from_json(cls, json_str: str) -> Quote:
        """Create an instance of Quote from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of quote_id
        if self.quote_id:
            _dict['quoteId'] = self.quote_id.to_dict()
        # override the default output from pydantic by calling `to_dict()` of metric_value
        if self.metric_value:
            _dict['metricValue'] = self.metric_value.to_dict()
        # set to None if lineage (nullable) is None
        # and __fields_set__ contains the field
        if self.lineage is None and "lineage" in self.__fields_set__:
            _dict['lineage'] = None

        # set to None if cut_label (nullable) is None
        # and __fields_set__ contains the field
        if self.cut_label is None and "cut_label" in self.__fields_set__:
            _dict['cutLabel'] = None

        # set to None if scale_factor (nullable) is None
        # and __fields_set__ contains the field
        if self.scale_factor is None and "scale_factor" in self.__fields_set__:
            _dict['scaleFactor'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> Quote:
        """Create an instance of Quote from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return Quote.parse_obj(obj)

        _obj = Quote.parse_obj({
            "quote_id": QuoteId.from_dict(obj.get("quoteId")) if obj.get("quoteId") is not None else None,
            "metric_value": MetricValue.from_dict(obj.get("metricValue")) if obj.get("metricValue") is not None else None,
            "lineage": obj.get("lineage"),
            "cut_label": obj.get("cutLabel"),
            "uploaded_by": obj.get("uploadedBy"),
            "as_at": obj.get("asAt"),
            "scale_factor": obj.get("scaleFactor")
        })
        return _obj
