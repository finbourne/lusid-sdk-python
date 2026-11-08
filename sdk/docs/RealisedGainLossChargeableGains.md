# RealisedGainLossChargeableGains

The UK chargeable-gains figures the engine worked for a realised-gain/loss leg: the chargeable gain, the  indexation allowance and the part of it taken, the proceeds the leg was worked on, both sides of the s.35  kink test on a 1982 holding, the basis and identification rule the leg was matched under, the lot it was  matched against, whether its transaction stands reversed, and the treatment applied. All amounts are in  the portfolio currency.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**chargeable_gain** | [**CurrencyAndAmount**](CurrencyAndAmount.md) |  | [optional] 
**indexation_allowance** | [**CurrencyAndAmount**](CurrencyAndAmount.md) |  | [optional] 
**indexation_allowance_taken** | [**CurrencyAndAmount**](CurrencyAndAmount.md) |  | [optional] 
**proceeds** | [**CurrencyAndAmount**](CurrencyAndAmount.md) |  | [optional] 
**gain_on_original_cost** | [**CurrencyAndAmount**](CurrencyAndAmount.md) |  | [optional] 
**gain_on_market_value1982** | [**CurrencyAndAmount**](CurrencyAndAmount.md) |  | [optional] 
**basis** | **str** | Available values: IndexedCost, MarketValue1982, OriginalCost, NilGain. | [optional] 
**match_rule** | **str** | Available values: SameDay, TenDay, Section210B, Section104Pool, Holding1982, Holding1965. | [optional] 
**matched_lot** | [**RealisedGainLossMatchedLot**](RealisedGainLossMatchedLot.md) |  | [optional] 
**market_value1965** | [**CurrencyAndAmount**](CurrencyAndAmount.md) |  | [optional] 
**reversed** | **bool** |  | [optional] 
**tax_treatment** | **str** |  | [optional] 
## Example

```python
from lusid.models.realised_gain_loss_chargeable_gains import RealisedGainLossChargeableGains
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

chargeable_gain: Optional[CurrencyAndAmount] = # Replace with your value
indexation_allowance: Optional[CurrencyAndAmount] = # Replace with your value
indexation_allowance_taken: Optional[CurrencyAndAmount] = # Replace with your value
proceeds: Optional[CurrencyAndAmount] = None
gain_on_original_cost: Optional[CurrencyAndAmount] = # Replace with your value
gain_on_market_value1982: Optional[CurrencyAndAmount] = # Replace with your value
basis: Optional[StrictStr] = "example_basis"
match_rule: Optional[StrictStr] = "example_match_rule"
matched_lot: Optional[RealisedGainLossMatchedLot] = # Replace with your value
market_value1965: Optional[CurrencyAndAmount] = # Replace with your value
reversed: Optional[StrictBool] = None
reversed:Optional[StrictBool] = None
tax_treatment: Optional[StrictStr] = "example_tax_treatment"
realised_gain_loss_chargeable_gains_instance = RealisedGainLossChargeableGains(chargeable_gain=chargeable_gain, indexation_allowance=indexation_allowance, indexation_allowance_taken=indexation_allowance_taken, proceeds=proceeds, gain_on_original_cost=gain_on_original_cost, gain_on_market_value1982=gain_on_market_value1982, basis=basis, match_rule=match_rule, matched_lot=matched_lot, market_value1965=market_value1965, reversed=reversed, tax_treatment=tax_treatment)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

