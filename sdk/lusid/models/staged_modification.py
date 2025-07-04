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
from pydantic.v1 import StrictStr, Field, BaseModel, Field, StrictInt, StrictStr, conlist 
from lusid.models.link import Link
from lusid.models.requested_changes import RequestedChanges
from lusid.models.staged_modification_decision import StagedModificationDecision
from lusid.models.staged_modification_staging_rule import StagedModificationStagingRule
from lusid.models.staged_modifications_entity_hrefs import StagedModificationsEntityHrefs

class StagedModification(BaseModel):
    """
    StagedModification
    """
    id:  Optional[StrictStr] = Field(None,alias="id", description="The unique Id for the staged modification") 
    as_at_staged: Optional[datetime] = Field(None, alias="asAtStaged", description="Time at which the modification was staged.")
    user_id_staged:  Optional[StrictStr] = Field(None,alias="userIdStaged", description="Id of the user who created the stage modification request.") 
    requested_id_staged:  Optional[StrictStr] = Field(None,alias="requestedIdStaged", description="The Request Id that initiated this staged modification.") 
    request_reason:  Optional[StrictStr] = Field(None,alias="requestReason", description="The Request Reason from the context that initiated this staged modification.") 
    action:  Optional[StrictStr] = Field(None,alias="action", description="Type of action of the staged modification, either create, update or delete.") 
    staging_rule: Optional[StagedModificationStagingRule] = Field(None, alias="stagingRule")
    decisions: Optional[conlist(StagedModificationDecision)] = Field(None, description="Object containing information relating to the decision on the staged modification.")
    decisions_count: Optional[StrictInt] = Field(None, alias="decisionsCount", description="Number of decisions made.")
    status:  Optional[StrictStr] = Field(None,alias="status", description="The status of the staged modification.") 
    as_at_closed: Optional[datetime] = Field(None, alias="asAtClosed", description="Time at which the modification was closed by either rejection or approval.")
    entity_type:  Optional[StrictStr] = Field(None,alias="entityType", description="The type of the entity that the staged modification applies to.") 
    scope:  Optional[StrictStr] = Field(None,alias="scope", description="The scope of the entity that this staged modification applies to.") 
    entity_unique_id:  Optional[StrictStr] = Field(None,alias="entityUniqueId", description="The unique Id of the entity the staged modification applies to.") 
    requested_changes: Optional[RequestedChanges] = Field(None, alias="requestedChanges")
    entity_hrefs: Optional[StagedModificationsEntityHrefs] = Field(None, alias="entityHrefs")
    display_name:  Optional[StrictStr] = Field(None,alias="displayName", description="The display name of the entity the staged modification applies to.") 
    links: Optional[conlist(Link)] = None
    __properties = ["id", "asAtStaged", "userIdStaged", "requestedIdStaged", "requestReason", "action", "stagingRule", "decisions", "decisionsCount", "status", "asAtClosed", "entityType", "scope", "entityUniqueId", "requestedChanges", "entityHrefs", "displayName", "links"]

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
    def from_json(cls, json_str: str) -> StagedModification:
        """Create an instance of StagedModification from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of staging_rule
        if self.staging_rule:
            _dict['stagingRule'] = self.staging_rule.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in decisions (list)
        _items = []
        if self.decisions:
            for _item in self.decisions:
                if _item:
                    _items.append(_item.to_dict())
            _dict['decisions'] = _items
        # override the default output from pydantic by calling `to_dict()` of requested_changes
        if self.requested_changes:
            _dict['requestedChanges'] = self.requested_changes.to_dict()
        # override the default output from pydantic by calling `to_dict()` of entity_hrefs
        if self.entity_hrefs:
            _dict['entityHrefs'] = self.entity_hrefs.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in links (list)
        _items = []
        if self.links:
            for _item in self.links:
                if _item:
                    _items.append(_item.to_dict())
            _dict['links'] = _items
        # set to None if id (nullable) is None
        # and __fields_set__ contains the field
        if self.id is None and "id" in self.__fields_set__:
            _dict['id'] = None

        # set to None if user_id_staged (nullable) is None
        # and __fields_set__ contains the field
        if self.user_id_staged is None and "user_id_staged" in self.__fields_set__:
            _dict['userIdStaged'] = None

        # set to None if requested_id_staged (nullable) is None
        # and __fields_set__ contains the field
        if self.requested_id_staged is None and "requested_id_staged" in self.__fields_set__:
            _dict['requestedIdStaged'] = None

        # set to None if request_reason (nullable) is None
        # and __fields_set__ contains the field
        if self.request_reason is None and "request_reason" in self.__fields_set__:
            _dict['requestReason'] = None

        # set to None if action (nullable) is None
        # and __fields_set__ contains the field
        if self.action is None and "action" in self.__fields_set__:
            _dict['action'] = None

        # set to None if decisions (nullable) is None
        # and __fields_set__ contains the field
        if self.decisions is None and "decisions" in self.__fields_set__:
            _dict['decisions'] = None

        # set to None if status (nullable) is None
        # and __fields_set__ contains the field
        if self.status is None and "status" in self.__fields_set__:
            _dict['status'] = None

        # set to None if as_at_closed (nullable) is None
        # and __fields_set__ contains the field
        if self.as_at_closed is None and "as_at_closed" in self.__fields_set__:
            _dict['asAtClosed'] = None

        # set to None if entity_type (nullable) is None
        # and __fields_set__ contains the field
        if self.entity_type is None and "entity_type" in self.__fields_set__:
            _dict['entityType'] = None

        # set to None if scope (nullable) is None
        # and __fields_set__ contains the field
        if self.scope is None and "scope" in self.__fields_set__:
            _dict['scope'] = None

        # set to None if entity_unique_id (nullable) is None
        # and __fields_set__ contains the field
        if self.entity_unique_id is None and "entity_unique_id" in self.__fields_set__:
            _dict['entityUniqueId'] = None

        # set to None if display_name (nullable) is None
        # and __fields_set__ contains the field
        if self.display_name is None and "display_name" in self.__fields_set__:
            _dict['displayName'] = None

        # set to None if links (nullable) is None
        # and __fields_set__ contains the field
        if self.links is None and "links" in self.__fields_set__:
            _dict['links'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> StagedModification:
        """Create an instance of StagedModification from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return StagedModification.parse_obj(obj)

        _obj = StagedModification.parse_obj({
            "id": obj.get("id"),
            "as_at_staged": obj.get("asAtStaged"),
            "user_id_staged": obj.get("userIdStaged"),
            "requested_id_staged": obj.get("requestedIdStaged"),
            "request_reason": obj.get("requestReason"),
            "action": obj.get("action"),
            "staging_rule": StagedModificationStagingRule.from_dict(obj.get("stagingRule")) if obj.get("stagingRule") is not None else None,
            "decisions": [StagedModificationDecision.from_dict(_item) for _item in obj.get("decisions")] if obj.get("decisions") is not None else None,
            "decisions_count": obj.get("decisionsCount"),
            "status": obj.get("status"),
            "as_at_closed": obj.get("asAtClosed"),
            "entity_type": obj.get("entityType"),
            "scope": obj.get("scope"),
            "entity_unique_id": obj.get("entityUniqueId"),
            "requested_changes": RequestedChanges.from_dict(obj.get("requestedChanges")) if obj.get("requestedChanges") is not None else None,
            "entity_hrefs": StagedModificationsEntityHrefs.from_dict(obj.get("entityHrefs")) if obj.get("entityHrefs") is not None else None,
            "display_name": obj.get("displayName"),
            "links": [Link.from_dict(_item) for _item in obj.get("links")] if obj.get("links") is not None else None
        })
        return _obj
