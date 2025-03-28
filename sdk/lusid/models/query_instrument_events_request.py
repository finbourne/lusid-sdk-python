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
from typing import Any, Dict, List, Optional
from pydantic.v1 import StrictStr, Field, BaseModel, Field, conlist, constr, validator 
from lusid.models.portfolio_entity_id import PortfolioEntityId
from lusid.models.resource_id import ResourceId

class QueryInstrumentEventsRequest(BaseModel):
    """
    Instrument event query.  # noqa: E501
    """
    as_at: Optional[datetime] = Field(None, alias="asAt", description="The time of the system at which to query for bucketed cashflows.")
    window_start: datetime = Field(..., alias="windowStart", description="The start date of the window.")
    window_end: datetime = Field(..., alias="windowEnd", description="The end date of the window.")
    portfolio_entity_ids: conlist(PortfolioEntityId) = Field(..., alias="portfolioEntityIds", description="The set of portfolios and portfolio groups to which the instrument events must belong.")
    effective_at: datetime = Field(..., alias="effectiveAt", description="The Effective date used in the valuation of the cashflows.")
    recipe_id: ResourceId = Field(..., alias="recipeId")
    filter_instrument_events:  Optional[StrictStr] = Field(None,alias="filterInstrumentEvents", description="Expression to filter the result set.") 
    __properties = ["asAt", "windowStart", "windowEnd", "portfolioEntityIds", "effectiveAt", "recipeId", "filterInstrumentEvents"]

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
    def from_json(cls, json_str: str) -> QueryInstrumentEventsRequest:
        """Create an instance of QueryInstrumentEventsRequest from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in portfolio_entity_ids (list)
        _items = []
        if self.portfolio_entity_ids:
            for _item in self.portfolio_entity_ids:
                if _item:
                    _items.append(_item.to_dict())
            _dict['portfolioEntityIds'] = _items
        # override the default output from pydantic by calling `to_dict()` of recipe_id
        if self.recipe_id:
            _dict['recipeId'] = self.recipe_id.to_dict()
        # set to None if as_at (nullable) is None
        # and __fields_set__ contains the field
        if self.as_at is None and "as_at" in self.__fields_set__:
            _dict['asAt'] = None

        # set to None if filter_instrument_events (nullable) is None
        # and __fields_set__ contains the field
        if self.filter_instrument_events is None and "filter_instrument_events" in self.__fields_set__:
            _dict['filterInstrumentEvents'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> QueryInstrumentEventsRequest:
        """Create an instance of QueryInstrumentEventsRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return QueryInstrumentEventsRequest.parse_obj(obj)

        _obj = QueryInstrumentEventsRequest.parse_obj({
            "as_at": obj.get("asAt"),
            "window_start": obj.get("windowStart"),
            "window_end": obj.get("windowEnd"),
            "portfolio_entity_ids": [PortfolioEntityId.from_dict(_item) for _item in obj.get("portfolioEntityIds")] if obj.get("portfolioEntityIds") is not None else None,
            "effective_at": obj.get("effectiveAt"),
            "recipe_id": ResourceId.from_dict(obj.get("recipeId")) if obj.get("recipeId") is not None else None,
            "filter_instrument_events": obj.get("filterInstrumentEvents")
        })
        return _obj
