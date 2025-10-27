# ReconciliationBreak

A reconciliation break
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**instrument_scope** | **str** | The scope in which the instrument lies. | [optional] 
**instrument_uid** | **str** | Unique instrument identifier | 
**sub_holding_keys** | [**Dict[str, PerpetualProperty]**](PerpetualProperty.md) | Any other properties that comprise the Sub-Holding Key | 
**left_units** | **float** | Units from the left hand side | 
**right_units** | **float** | Units from the right hand side | 
**difference_units** | **float** | Difference in units | 
**left_cost** | [**CurrencyAndAmount**](CurrencyAndAmount.md) |  | 
**right_cost** | [**CurrencyAndAmount**](CurrencyAndAmount.md) |  | 
**difference_cost** | [**CurrencyAndAmount**](CurrencyAndAmount.md) |  | 
**instrument_properties** | [**List[ModelProperty]**](ModelProperty.md) | Additional features relating to the instrument | 
## Example

```python
from lusid.models.reconciliation_break import ReconciliationBreak
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

instrument_scope: Optional[StrictStr] = "example_instrument_scope"
instrument_uid: StrictStr = "example_instrument_uid"
sub_holding_keys: Dict[str, PerpetualProperty] = # Replace with your value
left_units: Union[StrictFloat, StrictInt] = # Replace with your value
right_units: Union[StrictFloat, StrictInt] = # Replace with your value
difference_units: Union[StrictFloat, StrictInt] = # Replace with your value
left_cost: CurrencyAndAmount = # Replace with your value
right_cost: CurrencyAndAmount = # Replace with your value
difference_cost: CurrencyAndAmount = # Replace with your value
instrument_properties: List[ModelProperty] = # Replace with your value
reconciliation_break_instance = ReconciliationBreak(instrument_scope=instrument_scope, instrument_uid=instrument_uid, sub_holding_keys=sub_holding_keys, left_units=left_units, right_units=right_units, difference_units=difference_units, left_cost=left_cost, right_cost=right_cost, difference_cost=difference_cost, instrument_properties=instrument_properties)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

