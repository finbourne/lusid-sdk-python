# CorporateAction

A corporate action
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**corporate_action_code** | **str** | The unique identifier of this corporate action | 
**description** | **str** | The description of the corporate action. | [optional] 
**announcement_date** | **datetime** | The announcement date of the corporate action | [optional] 
**ex_date** | **datetime** | The ex date of the corporate action | [optional] 
**record_date** | **datetime** | The record date of the corporate action | [optional] 
**payment_date** | **datetime** | The payment date of the corporate action | [optional] 
**transitions** | [**List[CorporateActionTransition]**](CorporateActionTransition.md) | The transitions that result from this corporate action | [optional] 
## Example

```python
from lusid.models.corporate_action import CorporateAction
from typing import Any, Dict, List, Optional
from pydantic.v1 import BaseModel, Field, StrictStr, conlist
from datetime import datetime
corporate_action_code: StrictStr = "example_corporate_action_code"
description: Optional[StrictStr] = "example_description"
announcement_date: Optional[datetime] = # Replace with your value
ex_date: Optional[datetime] = # Replace with your value
record_date: Optional[datetime] = # Replace with your value
payment_date: Optional[datetime] = # Replace with your value
transitions: Optional[conlist(CorporateActionTransition)] = # Replace with your value
corporate_action_instance = CorporateAction(corporate_action_code=corporate_action_code, description=description, announcement_date=announcement_date, ex_date=ex_date, record_date=record_date, payment_date=payment_date, transitions=transitions)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

