# Bucket

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tax_lot_id** | **str** | The identifier of the tax lot this bucket is for. | [optional] 
**movement_name** | **str** | The name of the movement. | [optional] 
**holding_type** | **str** | The type of the holding. | [optional] 
**economic_bucket** | **str** | The economic bucket. | [optional] 
**economic_bucket_component** | **str** | The economic bucket component. | [optional] 
**economic_bucket_variant** | **str** | The economic bucket component. | [optional] 
**holding_sign** | **str** | The holding sign. | [optional] 
**local** | [**CurrencyAndAmount**](CurrencyAndAmount.md) |  | [optional] 
**base** | [**CurrencyAndAmount**](CurrencyAndAmount.md) |  | [optional] 
**units** | **float** | The units. | [optional] 
**activity_date** | **datetime** | The activity date of the bucket. | [optional] 
## Example

```python
from lusid.models.bucket import Bucket
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

tax_lot_id: Optional[StrictStr] = "example_tax_lot_id"
movement_name: Optional[StrictStr] = "example_movement_name"
holding_type: Optional[StrictStr] = "example_holding_type"
economic_bucket: Optional[StrictStr] = "example_economic_bucket"
economic_bucket_component: Optional[StrictStr] = "example_economic_bucket_component"
economic_bucket_variant: Optional[StrictStr] = "example_economic_bucket_variant"
holding_sign: Optional[StrictStr] = "example_holding_sign"
local: Optional[CurrencyAndAmount] = None
base: Optional[CurrencyAndAmount] = None
units: Optional[Union[StrictFloat, StrictInt]] = # Replace with your value
activity_date: Optional[datetime] = # Replace with your value
bucket_instance = Bucket(tax_lot_id=tax_lot_id, movement_name=movement_name, holding_type=holding_type, economic_bucket=economic_bucket, economic_bucket_component=economic_bucket_component, economic_bucket_variant=economic_bucket_variant, holding_sign=holding_sign, local=local, base=base, units=units, activity_date=activity_date)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

