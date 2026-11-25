# FacilityPayableDifference

A date on which a Facility's principal balance and its payable differ.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_date** | **datetime** | The date the principal balance and the payable differ on. | 
**balance** | **float** | The principal balance at the end of the date. | 
**payable** | **float** | The principal on the payable at the end of the date. | 
**difference** | **float** | The principal balance less the payable. | 
## Example

```python
from lusid.models.facility_payable_difference import FacilityPayableDifference
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

var_date: datetime = # Replace with your value
balance: Union[StrictFloat, StrictInt] = # Replace with your value
payable: Union[StrictFloat, StrictInt] = # Replace with your value
difference: Union[StrictFloat, StrictInt] = # Replace with your value
facility_payable_difference_instance = FacilityPayableDifference(var_date=var_date, balance=balance, payable=payable, difference=difference)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

