# SubscriptionDefinition

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**scope** | **str** |  | 
**code** | **str** |  | 
**display_name** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**portfolio_id** | [**ResourceId**](ResourceId.md) |  | 
**timeline_id** | [**ResourceId**](ResourceId.md) |  | [optional] 
**address_keys** | **List[str]** | The set of addresses the subscriber wishes to receive. | [optional] 
**by_tax_lots** | **bool** |  | [optional] 
**subscription_type** | **str** | The kind of data the subscription streams (holdings or transactions), defaulting to holdings.  Address keys and byTaxLots are not valid for a transactions subscription. Available values: Holdings, Transactions. | [optional] 
**start_effective_at** | **datetime** |  | [optional] 
**end_effective_at** | **datetime** |  | [optional] 
## Example

```python
from lusid.models.subscription_definition import SubscriptionDefinition
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

scope: StrictStr = "example_scope"
code: StrictStr = "example_code"
display_name: Optional[StrictStr] = "example_display_name"
description: Optional[StrictStr] = "example_description"
portfolio_id: ResourceId = # Replace with your value
timeline_id: Optional[ResourceId] = # Replace with your value
address_keys: Optional[List[StrictStr]] = # Replace with your value
by_tax_lots: Optional[StrictBool] = # Replace with your value
by_tax_lots:Optional[StrictBool] = None
subscription_type: Optional[StrictStr] = "example_subscription_type"
start_effective_at: Optional[datetime] = # Replace with your value
end_effective_at: Optional[datetime] = # Replace with your value
subscription_definition_instance = SubscriptionDefinition(scope=scope, code=code, display_name=display_name, description=description, portfolio_id=portfolio_id, timeline_id=timeline_id, address_keys=address_keys, by_tax_lots=by_tax_lots, subscription_type=subscription_type, start_effective_at=start_effective_at, end_effective_at=end_effective_at)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

