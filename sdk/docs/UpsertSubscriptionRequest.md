# UpsertSubscriptionRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**subscription** | [**SubscriptionDefinition**](SubscriptionDefinition.md) |  | 
## Example

```python
from lusid.models.upsert_subscription_request import UpsertSubscriptionRequest
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

subscription: SubscriptionDefinition
upsert_subscription_request_instance = UpsertSubscriptionRequest(subscription=subscription)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

