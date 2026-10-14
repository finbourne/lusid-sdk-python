# MarginCalculation

How the margin requirement for an item is calculated. The method field selects the method and the  remaining fields are the ones that method uses.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**method** | **str** | The calculation method. One of NetMtm, Ccp, GmraExposure, GmslaRcv, HouseRules, Simm, RegulatoryGrid or CcpIngested. Available values: NetMtm, Ccp, GmraExposure, GmslaRcv, HouseRules, Simm, RegulatoryGrid, CcpIngested. | 
**exposure_method** | **str** | For GmraExposure, the exposure method. One of Gmra2011A or Gmra2011B. Available values: Gmra2011A, Gmra2011B. | [optional] 
**repricing_permitted** | **bool** | For GmraExposure, whether repricing is permitted. | [optional] 
**margin_percentage** | **float** | For GmslaRcv, the margin percentage applied to the loan value. | [optional] 
**lending_fee_bps** | **int** | For GmslaRcv, the lending fee in basis points. | [optional] 
**credit_line** | **float** | For HouseRules, the credit line extended to the counterparty. | [optional] 
**threshold_allocation** | [**ThresholdAllocation**](ThresholdAllocation.md) |  | [optional] 
**ccp** | **str** | For CcpIngested, the name of the central counterparty. | [optional] 
**fcm_add_on** | **float** | For CcpIngested, the add-on charged by the futures commission merchant. | [optional] 
## Example

```python
from lusid.models.margin_calculation import MarginCalculation
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

method: StrictStr = "example_method"
exposure_method: Optional[StrictStr] = "example_exposure_method"
repricing_permitted: Optional[StrictBool] = # Replace with your value
repricing_permitted:Optional[StrictBool] = None
margin_percentage: Optional[Union[StrictFloat, StrictInt]] = # Replace with your value
lending_fee_bps: Optional[StrictInt] = # Replace with your value
lending_fee_bps: Optional[StrictInt] = None
credit_line: Optional[Union[StrictFloat, StrictInt]] = # Replace with your value
threshold_allocation: Optional[ThresholdAllocation] = # Replace with your value
ccp: Optional[StrictStr] = "example_ccp"
fcm_add_on: Optional[Union[StrictFloat, StrictInt]] = # Replace with your value
margin_calculation_instance = MarginCalculation(method=method, exposure_method=exposure_method, repricing_permitted=repricing_permitted, margin_percentage=margin_percentage, lending_fee_bps=lending_fee_bps, credit_line=credit_line, threshold_allocation=threshold_allocation, ccp=ccp, fcm_add_on=fcm_add_on)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

