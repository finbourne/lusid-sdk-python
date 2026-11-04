# UnsettledTransactionRevaluation

The transaction's total consideration in base currency, both at the rate it was booked at and revalued at the  valuation point's FX rate. Rates and amounts are null when they could not be resolved; Problems explains why.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**local_currency** | **str** | The settlement currency of the transaction (the &#39;local&#39; currency for revaluation purposes). | [optional] 
**local_amount** | **float** | The total consideration in the settlement currency, as booked. | [optional] 
**base_currency** | **str** | The fund&#39;s base currency. | [optional] 
**base_fx_rate** | **float** | The FX rate from settlement currency to base currency at the time the transaction was booked. Null when no booked rate was recorded. | [optional] 
**base_amount** | **float** | The total consideration in base currency at the booked FX rate. Null when the booked rate is unavailable. | [optional] 
**revaluation_fx_rate** | **float** | The FX rate from settlement currency to base currency at the valuation point&#39;s effective date. Null when the rate could not be resolved. | [optional] 
**revalued_base_amount** | **float** | The total consideration in base currency revalued at the valuation point&#39;s FX rate. Null when the revaluation rate is unavailable. | [optional] 
**revaluation_fx_rate_effective_at** | **datetime** | The effective date of the quote used for the revaluation FX rate. Null for same-currency transactions or when the rate is missing. | [optional] 
**status** | **str** | Whether revaluation succeeded (Revalued), was not needed (SameCurrency), or failed due to a missing FX rate (MissingFxRate). | [optional] 
**problems** | [**List[RevaluationProblem]**](RevaluationProblem.md) | Reasons why any of the amounts could not be populated. Empty when revaluation succeeded. | [optional] 
**counter_leg** | [**UnsettledTransactionCounterLegRevaluation**](UnsettledTransactionCounterLegRevaluation.md) |  | [optional] 
## Example

```python
from lusid.models.unsettled_transaction_revaluation import UnsettledTransactionRevaluation
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

local_currency: Optional[StrictStr] = "example_local_currency"
local_amount: Optional[Union[StrictFloat, StrictInt]] = # Replace with your value
base_currency: Optional[StrictStr] = "example_base_currency"
base_fx_rate: Optional[Union[StrictFloat, StrictInt]] = # Replace with your value
base_amount: Optional[Union[StrictFloat, StrictInt]] = # Replace with your value
revaluation_fx_rate: Optional[Union[StrictFloat, StrictInt]] = # Replace with your value
revalued_base_amount: Optional[Union[StrictFloat, StrictInt]] = # Replace with your value
revaluation_fx_rate_effective_at: Optional[datetime] = # Replace with your value
status: Optional[StrictStr] = "example_status"
problems: Optional[List[RevaluationProblem]] = # Replace with your value
counter_leg: Optional[UnsettledTransactionCounterLegRevaluation] = # Replace with your value
unsettled_transaction_revaluation_instance = UnsettledTransactionRevaluation(local_currency=local_currency, local_amount=local_amount, base_currency=base_currency, base_fx_rate=base_fx_rate, base_amount=base_amount, revaluation_fx_rate=revaluation_fx_rate, revalued_base_amount=revalued_base_amount, revaluation_fx_rate_effective_at=revaluation_fx_rate_effective_at, status=status, problems=problems, counter_leg=counter_leg)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

