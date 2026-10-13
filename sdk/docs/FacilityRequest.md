# FacilityRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** | The code of the Facility, unique within the Fund. | 
**display_name** | **str** | The name of the Facility. | 
**description** | **str** | A description for the Facility. | [optional] 
**lender** | **str** | The name of the lender providing the Facility. | 
**limit** | **float** | The committed limit of the Facility. Must be greater than zero. | 
**currency** | **str** | The three-letter currency code in which the Facility is denominated. | 
**rate_reference** | **str** | The reference rate the Facility interest is based on, for example SOFR. Optional. | [optional] 
**margin** | **float** | The margin over the reference rate, expressed as a decimal. Must be zero or greater. | 
**commitment_fee_rate** | **float** | The annual commitment fee rate charged on the undrawn balance, expressed as a decimal. Must be zero or greater. | 
**day_count_convention** | **str** | The day count convention used to accrue interest. One of: Act360, Act365, Act365F, Thirty360. | 
## Example

```python
from lusid.models.facility_request import FacilityRequest
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

code: StrictStr = "example_code"
display_name: StrictStr = "example_display_name"
description: Optional[StrictStr] = "example_description"
lender: StrictStr = "example_lender"
limit: Union[StrictFloat, StrictInt] = # Replace with your value
currency: StrictStr = "example_currency"
rate_reference: Optional[StrictStr] = "example_rate_reference"
margin: Union[StrictFloat, StrictInt] = # Replace with your value
commitment_fee_rate: Union[StrictFloat, StrictInt] = # Replace with your value
day_count_convention: StrictStr = "example_day_count_convention"
facility_request_instance = FacilityRequest(code=code, display_name=display_name, description=description, lender=lender, limit=limit, currency=currency, rate_reference=rate_reference, margin=margin, commitment_fee_rate=commitment_fee_rate, day_count_convention=day_count_convention)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

