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
from pydantic.v1 import BaseModel, Field, StrictStr, conlist, constr
from lusid.models.group_reconciliation_aggregate_attribute_values import GroupReconciliationAggregateAttributeValues
from lusid.models.group_reconciliation_core_attribute_values import GroupReconciliationCoreAttributeValues
from lusid.models.group_reconciliation_dates import GroupReconciliationDates
from lusid.models.group_reconciliation_instance_id import GroupReconciliationInstanceId
from lusid.models.group_reconciliation_user_review import GroupReconciliationUserReview
from lusid.models.link import Link
from lusid.models.resource_id import ResourceId
from lusid.models.version import Version

class GroupReconciliationComparisonResult(BaseModel):
    """
    GroupReconciliationComparisonResult
    """
    id: ResourceId = Field(...)
    reconciliation_type: constr(strict=True, min_length=1) = Field(..., alias="reconciliationType", description="The type of reconciliation to perform. \"Holding\" | \"Transaction\" | \"Valuation\"")
    group_reconciliation_definition_id: ResourceId = Field(..., alias="groupReconciliationDefinitionId")
    instance_id: GroupReconciliationInstanceId = Field(..., alias="instanceId")
    comparison_result_id: constr(strict=True, min_length=1) = Field(..., alias="comparisonResultId", description="Comparison result identifier, encoded value for core attribute results, aggregate attribute results, reconciliation type and run instanceId.")
    reconciliation_run_as_at: datetime = Field(..., alias="reconciliationRunAsAt", description="The timestamp when the run occurred.")
    result_type: constr(strict=True, min_length=1) = Field(..., alias="resultType", description="Reconciliation run general result. \"Break\" | \"Match\" | \"PartialMatch\" | \"NotFound")
    result_status: constr(strict=True, min_length=1) = Field(..., alias="resultStatus", description="Indicates how a particular result evolves from one run to the next. \"New\" | \"Confirmed\" | \"Changed\"")
    review_status: constr(strict=True, min_length=1) = Field(..., alias="reviewStatus", description="Status of whether user has provided any input (comments, manual matches, break codes). \"Pending\" | \"Reviewed\" | \"Matched\" | \"Invalid\"")
    dates_reconciled: GroupReconciliationDates = Field(..., alias="datesReconciled")
    core_attributes: GroupReconciliationCoreAttributeValues = Field(..., alias="coreAttributes")
    aggregate_attributes: GroupReconciliationAggregateAttributeValues = Field(..., alias="aggregateAttributes")
    user_review: Optional[GroupReconciliationUserReview] = Field(None, alias="userReview")
    href: Optional[StrictStr] = Field(None, description="The specific Uniform Resource Identifier (URI) for this resource at the requested effective and asAt datetime.")
    version: Optional[Version] = None
    links: Optional[conlist(Link)] = None
    __properties = ["id", "reconciliationType", "groupReconciliationDefinitionId", "instanceId", "comparisonResultId", "reconciliationRunAsAt", "resultType", "resultStatus", "reviewStatus", "datesReconciled", "coreAttributes", "aggregateAttributes", "userReview", "href", "version", "links"]

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
    def from_json(cls, json_str: str) -> GroupReconciliationComparisonResult:
        """Create an instance of GroupReconciliationComparisonResult from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of id
        if self.id:
            _dict['id'] = self.id.to_dict()
        # override the default output from pydantic by calling `to_dict()` of group_reconciliation_definition_id
        if self.group_reconciliation_definition_id:
            _dict['groupReconciliationDefinitionId'] = self.group_reconciliation_definition_id.to_dict()
        # override the default output from pydantic by calling `to_dict()` of instance_id
        if self.instance_id:
            _dict['instanceId'] = self.instance_id.to_dict()
        # override the default output from pydantic by calling `to_dict()` of dates_reconciled
        if self.dates_reconciled:
            _dict['datesReconciled'] = self.dates_reconciled.to_dict()
        # override the default output from pydantic by calling `to_dict()` of core_attributes
        if self.core_attributes:
            _dict['coreAttributes'] = self.core_attributes.to_dict()
        # override the default output from pydantic by calling `to_dict()` of aggregate_attributes
        if self.aggregate_attributes:
            _dict['aggregateAttributes'] = self.aggregate_attributes.to_dict()
        # override the default output from pydantic by calling `to_dict()` of user_review
        if self.user_review:
            _dict['userReview'] = self.user_review.to_dict()
        # override the default output from pydantic by calling `to_dict()` of version
        if self.version:
            _dict['version'] = self.version.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in links (list)
        _items = []
        if self.links:
            for _item in self.links:
                if _item:
                    _items.append(_item.to_dict())
            _dict['links'] = _items
        # set to None if href (nullable) is None
        # and __fields_set__ contains the field
        if self.href is None and "href" in self.__fields_set__:
            _dict['href'] = None

        # set to None if links (nullable) is None
        # and __fields_set__ contains the field
        if self.links is None and "links" in self.__fields_set__:
            _dict['links'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> GroupReconciliationComparisonResult:
        """Create an instance of GroupReconciliationComparisonResult from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return GroupReconciliationComparisonResult.parse_obj(obj)

        _obj = GroupReconciliationComparisonResult.parse_obj({
            "id": ResourceId.from_dict(obj.get("id")) if obj.get("id") is not None else None,
            "reconciliation_type": obj.get("reconciliationType"),
            "group_reconciliation_definition_id": ResourceId.from_dict(obj.get("groupReconciliationDefinitionId")) if obj.get("groupReconciliationDefinitionId") is not None else None,
            "instance_id": GroupReconciliationInstanceId.from_dict(obj.get("instanceId")) if obj.get("instanceId") is not None else None,
            "comparison_result_id": obj.get("comparisonResultId"),
            "reconciliation_run_as_at": obj.get("reconciliationRunAsAt"),
            "result_type": obj.get("resultType"),
            "result_status": obj.get("resultStatus"),
            "review_status": obj.get("reviewStatus"),
            "dates_reconciled": GroupReconciliationDates.from_dict(obj.get("datesReconciled")) if obj.get("datesReconciled") is not None else None,
            "core_attributes": GroupReconciliationCoreAttributeValues.from_dict(obj.get("coreAttributes")) if obj.get("coreAttributes") is not None else None,
            "aggregate_attributes": GroupReconciliationAggregateAttributeValues.from_dict(obj.get("aggregateAttributes")) if obj.get("aggregateAttributes") is not None else None,
            "user_review": GroupReconciliationUserReview.from_dict(obj.get("userReview")) if obj.get("userReview") is not None else None,
            "href": obj.get("href"),
            "version": Version.from_dict(obj.get("version")) if obj.get("version") is not None else None,
            "links": [Link.from_dict(_item) for _item in obj.get("links")] if obj.get("links") is not None else None
        })
        return _obj