# CreditSupportAnnex

Entity to capture the calculable and queryable methods and practices of determining and transferring collateral  to a counterparty as part of margining of transactions. These typically come from a particular ISDA agreement  that is in place between the two counterparties.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**reference_currency** | **str** | The base, or reference, currency against which MtM value and exposure should be calculated  and in which the CSA parameters are defined if the currency is not otherwise explicitly stated. | 
**collateral_currencies** | **List[str]** | The set of currencies within which it is acceptable to post cash collateral. | 
**isda_agreement_version** | **str** | The transactions will take place with reference to a particular ISDA master agreement. This  will likely be either the ISDA 1992 or ISDA 2002 agremeents or ISDA close-out 2009. | 
**margin_call_frequency** | **str** | The tenor, e.g. daily (1D) or biweekly (2W), at which frequency a margin call will be made, calculations  made and money transferred to readjust. The calculation might also require a specific time for valuation and notification. | 
**valuation_agent** | **str** | Are the calculations performed by the institutions&#39;s counterparty or the institution trading with them. | 
**threshold_amount** | **float** | At what level of exposure does collateral need to be posted. Will typically be zero for banks.  Should be stated in reference currency | 
**rounding_decimal_places** | **int** | Where a calculation needs to be rounded to a specific number of decimal places,  this states the number that that requires. | 
**initial_margin_amount** | **float** | The initial margin that is required. In the reference currency | 
**minimum_transfer_amount** | **float** | The minimum amount, in the reference currency, that must be transferred when required. | 
**id** | [**ResourceId**](ResourceId.md) |  | 
## Example

```python
from lusid.models.credit_support_annex import CreditSupportAnnex
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

reference_currency: StrictStr = "example_reference_currency"
collateral_currencies: List[StrictStr] = # Replace with your value
isda_agreement_version: StrictStr = "example_isda_agreement_version"
margin_call_frequency: StrictStr = "example_margin_call_frequency"
valuation_agent: StrictStr = "example_valuation_agent"
threshold_amount: Union[StrictFloat, StrictInt] = # Replace with your value
rounding_decimal_places: StrictInt = # Replace with your value
rounding_decimal_places: StrictInt = 42
initial_margin_amount: Union[StrictFloat, StrictInt] = # Replace with your value
minimum_transfer_amount: Union[StrictFloat, StrictInt] = # Replace with your value
id: ResourceId
credit_support_annex_instance = CreditSupportAnnex(reference_currency=reference_currency, collateral_currencies=collateral_currencies, isda_agreement_version=isda_agreement_version, margin_call_frequency=margin_call_frequency, valuation_agent=valuation_agent, threshold_amount=threshold_amount, rounding_decimal_places=rounding_decimal_places, initial_margin_amount=initial_margin_amount, minimum_transfer_amount=minimum_transfer_amount, id=id)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

