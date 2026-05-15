# UpdateTransactionFeeTypeRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** | A description of the transaction fee type. | [optional] 
**calculation** | [**FeeCalculationRequest**](FeeCalculationRequest.md) |  | [optional] 
**condition** | **str** | The condition that the transaction must meet in order for the fee to be applied. | [optional] 
**properties** | [**Dict[str, ModelProperty]**](ModelProperty.md) | A set of properties for the transaction fee type. | [optional] 
**is_active** | **bool** | Indicates whether the transaction fee type is currently active and should be applied to transactions. Optional when creating a transaction fee type, defaults to true, if a value is not provided. | [optional] 
## Example

```python
from lusid.models.update_transaction_fee_type_request import UpdateTransactionFeeTypeRequest
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

description: Optional[StrictStr] = "example_description"
calculation: Optional[FeeCalculationRequest] = None
condition: Optional[StrictStr] = "example_condition"
properties: Optional[Dict[str, ModelProperty]] = # Replace with your value
is_active: Optional[StrictBool] = # Replace with your value
is_active:Optional[StrictBool] = None
update_transaction_fee_type_request_instance = UpdateTransactionFeeTypeRequest(description=description, calculation=calculation, condition=condition, properties=properties, is_active=is_active)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

