# MarginLine

One holding's contribution to a margin call: its exposure, or its value as collateral.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**run_id** | **str** | The run that produced the line. | 
**agreement_id** | [**ResourceId**](ResourceId.md) |  | 
**item** | **str** | The margin item the line falls under. Filterable. | 
**portfolio_id** | [**ResourceId**](ResourceId.md) |  | [optional] 
**holding_id** | **str** | The holding the line was valued from. | [optional] 
**custodian_account_scope** | **str** | The scope of the custodian account the holding sits in, when it has one. | [optional] 
**custodian_account_code** | **str** | The code of the custodian account the holding sits in, when it has one. | [optional] 
**custodian_account_name** | **str** | The name of the custodian account, when it has one. | [optional] 
**instrument_identifiers** | **Dict[str, Optional[str]]** | The identifiers of the instrument held. | 
**units** | **float** | The units held. | 
**pv** | **float** | The present value of the holding in the agreement&#39;s base currency, when it contributes to exposure. | [optional] 
**variation_margin** | **float** | The holding&#39;s contribution to variation margin, when it contributes to exposure. | [optional] 
**collateral_value** | **float** | The holding&#39;s value as collateral after haircuts, when it is held as collateral. | [optional] 
**initial_margin_item** | **str** | The initial-margin item the line falls under, when the holding matched one. Filterable. | [optional] 
**initial_margin** | **float** | The holding&#39;s share of its netting set&#39;s initial margin, before the threshold, when it contributes to it. | [optional] 
**scenario** | [**ResourceId**](ResourceId.md) |  | [optional] 
## Example

```python
from lusid.models.margin_line import MarginLine
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

run_id: StrictStr = "example_run_id"
agreement_id: ResourceId = # Replace with your value
item: StrictStr = "example_item"
portfolio_id: Optional[ResourceId] = # Replace with your value
holding_id: Optional[StrictStr] = "example_holding_id"
custodian_account_scope: Optional[StrictStr] = "example_custodian_account_scope"
custodian_account_code: Optional[StrictStr] = "example_custodian_account_code"
custodian_account_name: Optional[StrictStr] = "example_custodian_account_name"
instrument_identifiers: Dict[str, Optional[StrictStr]] = # Replace with your value
units: Union[StrictFloat, StrictInt] = # Replace with your value
pv: Optional[Union[StrictFloat, StrictInt]] = # Replace with your value
variation_margin: Optional[Union[StrictFloat, StrictInt]] = # Replace with your value
collateral_value: Optional[Union[StrictFloat, StrictInt]] = # Replace with your value
initial_margin_item: Optional[StrictStr] = "example_initial_margin_item"
initial_margin: Optional[Union[StrictFloat, StrictInt]] = # Replace with your value
scenario: Optional[ResourceId] = None
margin_line_instance = MarginLine(run_id=run_id, agreement_id=agreement_id, item=item, portfolio_id=portfolio_id, holding_id=holding_id, custodian_account_scope=custodian_account_scope, custodian_account_code=custodian_account_code, custodian_account_name=custodian_account_name, instrument_identifiers=instrument_identifiers, units=units, pv=pv, variation_margin=variation_margin, collateral_value=collateral_value, initial_margin_item=initial_margin_item, initial_margin=initial_margin, scenario=scenario)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

