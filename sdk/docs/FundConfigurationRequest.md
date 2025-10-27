# FundConfigurationRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** |  | 
**display_name** | **str** | The name of the Fund. | [optional] 
**description** | **str** | A description for the Fund. | [optional] 
**dealing_filters** | [**List[ComponentFilter]**](ComponentFilter.md) | The set of filters used to decide which JE lines are included in the dealing. | 
**pnl_filters** | [**List[ComponentFilter]**](ComponentFilter.md) | The set of filters used to decide which JE lines are included in the PnL. | 
**back_out_filters** | [**List[ComponentFilter]**](ComponentFilter.md) | The set of filters used to decide which JE lines are included in the back outs. | 
**external_fee_filters** | [**List[ExternalFeeComponentFilter]**](ExternalFeeComponentFilter.md) | The set of filters used to decide which JE lines are used for inputting fees from an external source. | [optional] 
**properties** | [**Dict[str, ModelProperty]**](ModelProperty.md) | A set of properties for the Fund Configuration. | [optional] 
## Example

```python
from lusid.models.fund_configuration_request import FundConfigurationRequest
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

code: StrictStr = "example_code"
display_name: Optional[StrictStr] = "example_display_name"
description: Optional[StrictStr] = "example_description"
dealing_filters: List[ComponentFilter] = # Replace with your value
pnl_filters: List[ComponentFilter] = # Replace with your value
back_out_filters: List[ComponentFilter] = # Replace with your value
external_fee_filters: Optional[List[ExternalFeeComponentFilter]] = # Replace with your value
properties: Optional[Dict[str, ModelProperty]] = # Replace with your value
fund_configuration_request_instance = FundConfigurationRequest(code=code, display_name=display_name, description=description, dealing_filters=dealing_filters, pnl_filters=pnl_filters, back_out_filters=back_out_filters, external_fee_filters=external_fee_filters, properties=properties)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

