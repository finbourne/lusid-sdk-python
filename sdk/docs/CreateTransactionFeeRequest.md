# CreateTransactionFeeRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The display name of the transaction fee. | 
**description** | **str** | A description of the transaction fee. | 
**calculation** | [**FeeCalculationRequest**](FeeCalculationRequest.md) |  | 
**condition** | **str** | The condition that the transaction must meet in order for the fee to be applied. | 
**capitalised** | **str** | Specifies whether the fee should be capitalised, not capitalised or conditionally capitalised. | 
**capitalisation_condition** | **str** | If the fee Capitalisation is Conditional, this condition determines whether the fee is capitalised, when applied to the transaction. | [optional] 
**txn_property_key** | **str** | The property key to which the fee value will be applied and decorated onto the transaction. Must be in the &#39;Transaction&#39; property domain. | 
**properties** | [**Dict[str, ModelProperty]**](ModelProperty.md) | A set of properties for the transaction fee. | [optional] 
**is_active** | **bool** | Indicates whether the transaction fee is currently active and should be applied to transactions. Optional when creating a transaction fee, defaults to true, if a value is not provided. | [optional] 
## Example

```python
from lusid.models.create_transaction_fee_request import CreateTransactionFeeRequest
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

name: StrictStr = "example_name"
description: StrictStr = "example_description"
calculation: FeeCalculationRequest
condition: StrictStr = "example_condition"
capitalised: StrictStr = "example_capitalised"
capitalisation_condition: Optional[StrictStr] = "example_capitalisation_condition"
txn_property_key: StrictStr = "example_txn_property_key"
properties: Optional[Dict[str, ModelProperty]] = # Replace with your value
is_active: Optional[StrictBool] = # Replace with your value
is_active:Optional[StrictBool] = None
create_transaction_fee_request_instance = CreateTransactionFeeRequest(name=name, description=description, calculation=calculation, condition=condition, capitalised=capitalised, capitalisation_condition=capitalisation_condition, txn_property_key=txn_property_key, properties=properties, is_active=is_active)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

