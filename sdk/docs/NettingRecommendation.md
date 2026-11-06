# NettingRecommendation

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**run_id** | **str** | The run the recommendation was made from. Filterable. | 
**source_agreement_id** | [**ResourceId**](ResourceId.md) |  | 
**source_item** | **str** | The initial-margin item the trades would leave. Filterable. | 
**target_agreement_id** | [**ResourceId**](ResourceId.md) |  | 
**target_item** | **str** | The initial-margin item the trades would join. Filterable. | 
**transfer** | **str** | How the trades would get there: Redesignation when both agreements face one counterparty, Novation otherwise. Filterable. | 
**instrument_type** | **str** | LUSID&#39;s type for the instruments in the cluster. Filterable. | [optional] 
**currency** | **str** | The currency the cluster&#39;s trades are denominated in. Filterable. | [optional] 
**maturity_bucket** | **str** | The residual-maturity bucket the cluster&#39;s trades fall in on the run date; empty for instruments without a maturity. Filterable. | [optional] 
**trades** | [**List[TradeReference]**](TradeReference.md) | The holdings that would move. | 
**saving_per_day** | **float** | What we would no longer fund each day across both sets, in the sets&#39; base currency. Filterable. | 
**one_off_cost** | **float** | The novation cost when the transfer is one; zero for a re-designation. Filterable. | 
**payback_days** | **float** | How many days of saving cover the one-off cost. Filterable. | 
**initial_margin_change** | **float** | The sum over both sets of what we would post after the move less what we post today. Filterable. | 
**source** | [**InitialMarginChange**](InitialMarginChange.md) |  | 
**target** | [**InitialMarginChange**](InitialMarginChange.md) |  | 
## Example

```python
from lusid.models.netting_recommendation import NettingRecommendation
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

run_id: StrictStr = "example_run_id"
source_agreement_id: ResourceId = # Replace with your value
source_item: StrictStr = "example_source_item"
target_agreement_id: ResourceId = # Replace with your value
target_item: StrictStr = "example_target_item"
transfer: StrictStr = "example_transfer"
instrument_type: Optional[StrictStr] = "example_instrument_type"
currency: Optional[StrictStr] = "example_currency"
maturity_bucket: Optional[StrictStr] = "example_maturity_bucket"
trades: List[TradeReference] = # Replace with your value
saving_per_day: Union[StrictFloat, StrictInt] = # Replace with your value
one_off_cost: Union[StrictFloat, StrictInt] = # Replace with your value
payback_days: Union[StrictFloat, StrictInt] = # Replace with your value
initial_margin_change: Union[StrictFloat, StrictInt] = # Replace with your value
source: InitialMarginChange
target: InitialMarginChange
netting_recommendation_instance = NettingRecommendation(run_id=run_id, source_agreement_id=source_agreement_id, source_item=source_item, target_agreement_id=target_agreement_id, target_item=target_item, transfer=transfer, instrument_type=instrument_type, currency=currency, maturity_bucket=maturity_bucket, trades=trades, saving_per_day=saving_per_day, one_off_cost=one_off_cost, payback_days=payback_days, initial_margin_change=initial_margin_change, source=source, target=target)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

