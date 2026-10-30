# DealingFlowValuation

The transfer agency's dealing flows with unit-denominated orders valued at one unit price, and the swing outcome that net flow leads the methodology to.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**net_cashflow** | **float** | The inflows less the outflows at this unit price, in the fund currency. | 
**net_cashflow_pct_of_nav** | **float** | The net cashflow as a percentage of the fund&#39;s NAV at the previous valuation point. Absent when there is no previous NAV. | [optional] 
**gross_inflow** | **float** | The sum of the inflows at this unit price, in the fund currency. Zero or more. | 
**gross_outflow** | **float** | The sum of the outflows at this unit price, in the fund currency, as a magnitude. Zero or more. | 
**outcome** | [**EstimateValuationOutcome**](EstimateValuationOutcome.md) |  | [optional] 
## Example

```python
from lusid.models.dealing_flow_valuation import DealingFlowValuation
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

net_cashflow: Union[StrictFloat, StrictInt] = # Replace with your value
net_cashflow_pct_of_nav: Optional[Union[StrictFloat, StrictInt]] = # Replace with your value
gross_inflow: Union[StrictFloat, StrictInt] = # Replace with your value
gross_outflow: Union[StrictFloat, StrictInt] = # Replace with your value
outcome: Optional[EstimateValuationOutcome] = None
dealing_flow_valuation_instance = DealingFlowValuation(net_cashflow=net_cashflow, net_cashflow_pct_of_nav=net_cashflow_pct_of_nav, gross_inflow=gross_inflow, gross_outflow=gross_outflow, outcome=outcome)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

