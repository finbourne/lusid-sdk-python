# MovementSettlementSummary

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**type** | **str** |  | [optional] 
**lusid_instrument_id** | **str** |  | [optional] 
**instrument_scope** | **str** |  | [optional] 
**settlement_mode** | **str** |  | [optional] 
**contractual_settlement_date** | **str** |  | [optional] 
**units** | **float** |  | [optional] 
**settled_units** | **float** |  | [optional] 
**unsettled_units** | **float** |  | [optional] 
**overdue_units** | **float** |  | [optional] 
## Example

```python
from lusid.models.movement_settlement_summary import MovementSettlementSummary
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

name: Optional[StrictStr] = "example_name"
type: Optional[StrictStr] = "example_type"
lusid_instrument_id: Optional[StrictStr] = "example_lusid_instrument_id"
instrument_scope: Optional[StrictStr] = "example_instrument_scope"
settlement_mode: Optional[StrictStr] = "example_settlement_mode"
contractual_settlement_date: Optional[StrictStr] = "example_contractual_settlement_date"
units: Optional[Union[StrictFloat, StrictInt]] = None
settled_units: Optional[Union[StrictFloat, StrictInt]] = # Replace with your value
unsettled_units: Optional[Union[StrictFloat, StrictInt]] = # Replace with your value
overdue_units: Optional[Union[StrictFloat, StrictInt]] = # Replace with your value
movement_settlement_summary_instance = MovementSettlementSummary(name=name, type=type, lusid_instrument_id=lusid_instrument_id, instrument_scope=instrument_scope, settlement_mode=settlement_mode, contractual_settlement_date=contractual_settlement_date, units=units, settled_units=settled_units, unsettled_units=unsettled_units, overdue_units=overdue_units)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

