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


from typing import Any, Dict, List, Optional
from pydantic.v1 import StrictStr, Field, Field, StrictStr, conlist, validator 
from lusid.models.option_entry import OptionEntry
from lusid.models.schedule import Schedule

class OptionalitySchedule(Schedule):
    """
    Optionality Schedule represents a class for creation of schedules for optionality (call, put)  # noqa: E501
    """
    exercise_type:  Optional[StrictStr] = Field(None,alias="exerciseType", description="The exercise type of the optionality schedule (American or European).  For American type, the bond is perpetually callable from a given exercise date until it matures, or the next date in the schedule.  For European type, the bond is only callable on a given exercise date.    Supported string (enumeration) values are: [European, American].") 
    option_entries: Optional[conlist(OptionEntry)] = Field(None, alias="optionEntries", description="The dates at which the bond call/put may be actioned, and associated strikes.")
    option_type:  Optional[StrictStr] = Field(None,alias="optionType", description="Type of optionality for the schedule.    Supported string (enumeration) values are: [Call, Put].") 
    schedule_type:  StrictStr = Field(...,alias="scheduleType", description="The available values are: FixedSchedule, FloatSchedule, OptionalitySchedule, StepSchedule, Exercise, FxRateSchedule, FxLinkedNotionalSchedule, BondConversionSchedule, Invalid") 
    additional_properties: Dict[str, Any] = {}
    __properties = ["scheduleType", "exerciseType", "optionEntries", "optionType"]

    @validator('schedule_type')
    def schedule_type_validate_enum(cls, value):
        """Validates the enum"""

        # Finbourne have removed enum validation on all models, except for this use case:
        # Workflow and notification application SDK use the property name 'type' as the discriminator on a number of classes.
        # During instantiation, the value of 'type' is checked against the enum values, 
        

        # check it's a class that uses the 'type' property as a discriminator
        # list of classes can be found by searching for 'actual_instance: Union[' in the generated code
        if 'OptionalitySchedule' not in [ 
                                    # For notification application classes
                                    'AmazonSqsNotificationType',
                                    'AmazonSqsNotificationTypeResponse',
                                    'AmazonSqsPrincipalAuthNotificationType',
                                    'AmazonSqsPrincipalAuthNotificationTypeResponse',
                                    'AzureServiceBusTypeResponse',
                                    'AzureServiceBusNotificationType',
                                    'EmailNotificationType',
                                    'EmailNotificationTypeResponse',
                                    'SmsNotificationType',
                                    'SmsNotificationTypeResponse',
                                    'WebhookNotificationType',
                                    'WebhookNotificationTypeResponse',
                        
                                    # For workflow application classes
                                    'CreateChildTasksAction', 
                                    'RunWorkerAction', 
                                    'TriggerParentTaskAction',
                                    'CreateChildTasksActionResponse', 
                                    'RunWorkerActionResponse',
                                    'TriggerParentTaskActionResponse',
                                    'CreateNewTaskActivity',
                                    'UpdateMatchingTasksActivity',
                                    'CreateNewTaskActivityResponse', 
                                    'UpdateMatchingTasksActivityResponse',
                                    'Fail', 
                                    'GroupReconciliation', 
                                    'HealthCheck', 
                                    'LuminesceView', 
                                    'SchedulerJob', 
                                    'Sleep',
                                    'FailResponse', 
                                    'GroupReconciliationResponse', 
                                    'HealthCheckResponse', 
                                    'LuminesceViewResponse', 
                                    'SchedulerJobResponse', 
                                    'SleepResponse']:
           return value
        
        # Only validate the 'type' property of the class
        if "schedule_type" != "type":
            return value

        if value not in ('FixedSchedule', 'FloatSchedule', 'OptionalitySchedule', 'StepSchedule', 'Exercise', 'FxRateSchedule', 'FxLinkedNotionalSchedule', 'BondConversionSchedule', 'Invalid'):
            raise ValueError("must be one of enum values ('FixedSchedule', 'FloatSchedule', 'OptionalitySchedule', 'StepSchedule', 'Exercise', 'FxRateSchedule', 'FxLinkedNotionalSchedule', 'BondConversionSchedule', 'Invalid')")
        return value

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
    def from_json(cls, json_str: str) -> OptionalitySchedule:
        """Create an instance of OptionalitySchedule from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                            "additional_properties"
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in option_entries (list)
        _items = []
        if self.option_entries:
            for _item in self.option_entries:
                if _item:
                    _items.append(_item.to_dict())
            _dict['optionEntries'] = _items
        # puts key-value pairs in additional_properties in the top level
        if self.additional_properties is not None:
            for _key, _value in self.additional_properties.items():
                _dict[_key] = _value

        # set to None if exercise_type (nullable) is None
        # and __fields_set__ contains the field
        if self.exercise_type is None and "exercise_type" in self.__fields_set__:
            _dict['exerciseType'] = None

        # set to None if option_entries (nullable) is None
        # and __fields_set__ contains the field
        if self.option_entries is None and "option_entries" in self.__fields_set__:
            _dict['optionEntries'] = None

        # set to None if option_type (nullable) is None
        # and __fields_set__ contains the field
        if self.option_type is None and "option_type" in self.__fields_set__:
            _dict['optionType'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> OptionalitySchedule:
        """Create an instance of OptionalitySchedule from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return OptionalitySchedule.parse_obj(obj)

        _obj = OptionalitySchedule.parse_obj({
            "schedule_type": obj.get("scheduleType"),
            "exercise_type": obj.get("exerciseType"),
            "option_entries": [OptionEntry.from_dict(_item) for _item in obj.get("optionEntries")] if obj.get("optionEntries") is not None else None,
            "option_type": obj.get("optionType")
        })
        # store additional fields in additional_properties
        for _key in obj.keys():
            if _key not in cls.__properties:
                _obj.additional_properties[_key] = obj.get(_key)

        return _obj
