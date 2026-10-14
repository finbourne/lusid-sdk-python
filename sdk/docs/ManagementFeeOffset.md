# ManagementFeeOffset

A fee income the manager has earned elsewhere that offsets the management fee.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**source_ref** | **str** | A reference to the fee income being offset. | 
**amount** | **float** | The amount of fee income received. | 
**offset_percentage** | **float** | The fraction of the fee income that offsets the management fee, between 0 and 1. | 
**deal** | **str** | For a deal-linked offset, the deal the fee income relates to. | [optional] 
## Example

```python
from lusid.models.management_fee_offset import ManagementFeeOffset
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

source_ref: StrictStr = "example_source_ref"
amount: Union[StrictFloat, StrictInt] = # Replace with your value
offset_percentage: Union[StrictFloat, StrictInt] = # Replace with your value
deal: Optional[StrictStr] = "example_deal"
management_fee_offset_instance = ManagementFeeOffset(source_ref=source_ref, amount=amount, offset_percentage=offset_percentage, deal=deal)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

