# UnsettledTransactionCounterLegRevaluation

The receiving (counter) leg of an FX forward revalued into the fund's base currency at the valuation point's  FX rates. Populated only for FX forward transactions.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**local_currency** | **str** | The currency of the FX forward&#39;s receiving (counter) leg. | [optional] 
**local_amount** | **float** | The amount of the receiving leg in its own currency. | [optional] 
**base_currency** | **str** | The fund&#39;s base currency. | [optional] 
**booked_base_amount** | **float** | The receiving leg amount in base currency at the rate booked on the transaction. Null when no booked rate was recorded. | [optional] 
**revaluation_fx_rate** | **float** | The FX rate from the counter-leg currency to base currency at the valuation point&#39;s effective date. Null when the rate could not be resolved. | [optional] 
**revalued_base_amount** | **float** | The receiving leg amount in base currency revalued at the valuation point&#39;s FX rate. Null when the revaluation rate is unavailable. | [optional] 
**revaluation_fx_rate_effective_at** | **datetime** | The effective date of the quote used for the counter-leg revaluation FX rate. Null for same-currency legs or when the rate is missing. | [optional] 
**status** | **str** | Whether counter-leg revaluation succeeded (Revalued), was not needed (SameCurrency), or failed due to a missing FX rate (MissingFxRate). | [optional] 
**problems** | [**List[RevaluationProblem]**](RevaluationProblem.md) | Reasons why any counter-leg amounts could not be populated. Empty when revaluation succeeded. | [optional] 
## Example

```python
from lusid.models.unsettled_transaction_counter_leg_revaluation import UnsettledTransactionCounterLegRevaluation
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

local_currency: Optional[StrictStr] = "example_local_currency"
local_amount: Optional[Union[StrictFloat, StrictInt]] = # Replace with your value
base_currency: Optional[StrictStr] = "example_base_currency"
booked_base_amount: Optional[Union[StrictFloat, StrictInt]] = # Replace with your value
revaluation_fx_rate: Optional[Union[StrictFloat, StrictInt]] = # Replace with your value
revalued_base_amount: Optional[Union[StrictFloat, StrictInt]] = # Replace with your value
revaluation_fx_rate_effective_at: Optional[datetime] = # Replace with your value
status: Optional[StrictStr] = "example_status"
problems: Optional[List[RevaluationProblem]] = # Replace with your value
unsettled_transaction_counter_leg_revaluation_instance = UnsettledTransactionCounterLegRevaluation(local_currency=local_currency, local_amount=local_amount, base_currency=base_currency, booked_base_amount=booked_base_amount, revaluation_fx_rate=revaluation_fx_rate, revalued_base_amount=revalued_base_amount, revaluation_fx_rate_effective_at=revaluation_fx_rate_effective_at, status=status, problems=problems)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

