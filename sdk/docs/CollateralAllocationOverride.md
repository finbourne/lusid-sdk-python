# CollateralAllocationOverride

An asset and the units of it a user chooses to move for a margin call, validated against the agreement's  constraints as the allocation is.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**instrument_id** | **str** | The LUSID instrument identifier of the asset to move, or CCY_ and the currency code for cash. | 
**portfolio_id** | [**ResourceId**](ResourceId.md) |  | 
**units** | **float** | The units to move. | 
**custodian_account** | [**ResourceId**](ResourceId.md) |  | [optional] 
## Example

```python
from lusid.models.collateral_allocation_override import CollateralAllocationOverride
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

instrument_id: StrictStr = "example_instrument_id"
portfolio_id: ResourceId = # Replace with your value
units: Union[StrictFloat, StrictInt] = # Replace with your value
custodian_account: Optional[ResourceId] = # Replace with your value
collateral_allocation_override_instance = CollateralAllocationOverride(instrument_id=instrument_id, portfolio_id=portfolio_id, units=units, custodian_account=custodian_account)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

