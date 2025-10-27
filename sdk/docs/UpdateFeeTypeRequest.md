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
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

display_name: StrictStr = "example_display_name"
description: Optional[StrictStr] = "example_description"
component_transactions: List[ComponentTransaction] = # Replace with your value
update_fee_type_request_instance = UpdateFeeTypeRequest(display_name=display_name, description=description, component_transactions=component_transactions)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

