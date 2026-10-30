# EstimateValuation

The swing decision read at both unit prices the transfer agency's unit-denominated orders could be valued at: this valuation point's estimate price and the last official price, with which one the decision used and how far apart they are.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**decision_price** | **str** | The unit price the swing decision was taken on. &#39;EstimatePrice&#39; is the price struck at this valuation point; &#39;LastOfficialPrice&#39; is the unit price the previous valuation point published. &#39;EstimatePrice&#39; when the fund asked for the last official price but has none yet, as on its first valuation point. | 
**at_estimate_price** | [**DealingFlowValuation**](DealingFlowValuation.md) |  | 
**at_last_official_price** | [**DealingFlowValuation**](DealingFlowValuation.md) |  | [optional] 
**difference** | [**EstimateValuationDifference**](EstimateValuationDifference.md) |  | [optional] 
**unit_based_share** | **float** | The fraction of the decision&#39;s net cashflow that came from unit-denominated orders, from 0 to 1. Zero when the net cashflow is zero. | 
## Example

```python
from lusid.models.estimate_valuation import EstimateValuation
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

decision_price: StrictStr = "example_decision_price"
at_estimate_price: DealingFlowValuation = # Replace with your value
at_last_official_price: Optional[DealingFlowValuation] = # Replace with your value
difference: Optional[EstimateValuationDifference] = None
unit_based_share: Union[StrictFloat, StrictInt] = # Replace with your value
estimate_valuation_instance = EstimateValuation(decision_price=decision_price, at_estimate_price=at_estimate_price, at_last_official_price=at_last_official_price, difference=difference, unit_based_share=unit_based_share)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

