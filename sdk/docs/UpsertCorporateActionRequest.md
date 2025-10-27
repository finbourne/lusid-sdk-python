# UpsertCorporateActionRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**corporate_action_code** | **str** | The unique identifier of this corporate action | 
**description** | **str** | The description of the corporate action. | [optional] 
**announcement_date** | **datetime** | The announcement date of the corporate action | 
**ex_date** | **datetime** | The ex date of the corporate action | 
**record_date** | **datetime** | The record date of the corporate action | 
**payment_date** | **datetime** | The payment date of the corporate action | 
**transitions** | [**List[CorporateActionTransitionRequest]**](CorporateActionTransitionRequest.md) | The transitions that result from this corporate action | 
## Example

```python
from lusid.models.upsert_corporate_action_request import UpsertCorporateActionRequest
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

corporate_action_code: StrictStr = "example_corporate_action_code"
description: Optional[StrictStr] = "example_description"
announcement_date: datetime = # Replace with your value
ex_date: datetime = # Replace with your value
record_date: datetime = # Replace with your value
payment_date: datetime = # Replace with your value
transitions: List[CorporateActionTransitionRequest] = # Replace with your value
upsert_corporate_action_request_instance = UpsertCorporateActionRequest(corporate_action_code=corporate_action_code, description=description, announcement_date=announcement_date, ex_date=ex_date, record_date=record_date, payment_date=payment_date, transitions=transitions)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

