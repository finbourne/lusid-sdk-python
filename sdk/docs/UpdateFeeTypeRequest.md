# UpdateFeeTypeRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**display_name** | **str** | The name of the fee type. | 
**description** | **str** | The description of the fee type. | [optional] 
**component_transactions** | [**List[ComponentTransaction]**](ComponentTransaction.md) | A set of component transactions that relate to the fee type to be created. | 
## Example

```python
from lusid.models.update_fee_type_request import UpdateFeeTypeRequest
from typing import Any, Dict, List, Optional
from pydantic.v1 import BaseModel, Field, conlist, constr, validator

display_name: StrictStr = "example_display_name"
description: Optional[StrictStr] = "example_description"
component_transactions: conlist(ComponentTransaction, max_items=1000) = Field(..., alias="componentTransactions", description="A set of component transactions that relate to the fee type to be created.")
update_fee_type_request_instance = UpdateFeeTypeRequest(display_name=display_name, description=description, component_transactions=component_transactions)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

