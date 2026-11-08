# CollateralAllocationCandidate

One holding the allocation considered for a margin call, with its figures as far as they could be computed and  either its rank or the constraint that excluded it.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**instrument_id** | **str** | The LUSID instrument identifier of the asset, or CCY_ and the currency code for cash. | 
**instrument_identifiers** | **Dict[str, Optional[str]]** | The instrument identifiers a transaction for the line is booked against. | 
**portfolio_id** | [**ResourceId**](ResourceId.md) |  | 
**custodian_account** | [**ResourceId**](ResourceId.md) |  | [optional] 
**asset_kind** | **str** | Cash or Security. | 
**currency** | **str** | The currency the asset is denominated in, when known. | [optional] 
**units_free** | **float** | Units not in a margin account and not promised to an earlier call of the run. | 
**lot_size** | **float** | The smallest number of units the asset is delivered in. | 
**price** | **float** | The market value per unit in the base currency, before any haircut. Null when the asset could not be priced. | [optional] 
**eligibility_seq** | **int** | The one-based position of the schedule row that admits the asset. Null when no row does. | [optional] 
**valuation_percentage** | **float** | The fraction of market value the schedule row counts as collateral. | [optional] 
**fx_haircut** | **float** | The further fraction deducted because the asset is not in the base currency. Zero when it is. | [optional] 
**effective_value_per_unit** | **float** | Price times the valuation percentage, less the FX haircut: what one unit counts for as collateral. | [optional] 
**opportunity_rate** | **float** | The annual rate the fund gives up by locking the asset up: funding less the agreement&#39;s cash interest for cash, the lending fee it would otherwise earn for a security. | [optional] 
**cost_per_unit_of_value** | **float** | The ranking key: the annual cost of one unit of collateral value from this asset. | [optional] 
**concentration_cap** | **float** | The collateral value the schedule&#39;s concentration limit still allows from the asset&#39;s group. Null when the row sets no limit. | [optional] 
**settlement_date** | **datetime** | When the movement would settle under the agreement&#39;s settlement lag, counting weekdays. | [optional] 
**rank** | **int** | The asset&#39;s position in the ranking, cheapest first. Null when excluded. | [optional] 
**exclusion_reason** | **str** | The constraint the asset failed, when it did. One of NotEligible, NoFreeUnits, MissingPrice, MissingRate, MissesDeadline, BelowMinimumLot or ConcentrationExhausted. Null when it passed. | [optional] 
## Example

```python
from lusid.models.collateral_allocation_candidate import CollateralAllocationCandidate
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

instrument_id: StrictStr = "example_instrument_id"
instrument_identifiers: Dict[str, Optional[StrictStr]] = # Replace with your value
portfolio_id: ResourceId = # Replace with your value
custodian_account: Optional[ResourceId] = # Replace with your value
asset_kind: StrictStr = "example_asset_kind"
currency: Optional[StrictStr] = "example_currency"
units_free: Union[StrictFloat, StrictInt] = # Replace with your value
lot_size: Union[StrictFloat, StrictInt] = # Replace with your value
price: Optional[Union[StrictFloat, StrictInt]] = # Replace with your value
eligibility_seq: Optional[StrictInt] = # Replace with your value
eligibility_seq: Optional[StrictInt] = None
valuation_percentage: Optional[Union[StrictFloat, StrictInt]] = # Replace with your value
fx_haircut: Optional[Union[StrictFloat, StrictInt]] = # Replace with your value
effective_value_per_unit: Optional[Union[StrictFloat, StrictInt]] = # Replace with your value
opportunity_rate: Optional[Union[StrictFloat, StrictInt]] = # Replace with your value
cost_per_unit_of_value: Optional[Union[StrictFloat, StrictInt]] = # Replace with your value
concentration_cap: Optional[Union[StrictFloat, StrictInt]] = # Replace with your value
settlement_date: Optional[datetime] = # Replace with your value
rank: Optional[StrictInt] = # Replace with your value
rank: Optional[StrictInt] = None
exclusion_reason: Optional[StrictStr] = "example_exclusion_reason"
collateral_allocation_candidate_instance = CollateralAllocationCandidate(instrument_id=instrument_id, instrument_identifiers=instrument_identifiers, portfolio_id=portfolio_id, custodian_account=custodian_account, asset_kind=asset_kind, currency=currency, units_free=units_free, lot_size=lot_size, price=price, eligibility_seq=eligibility_seq, valuation_percentage=valuation_percentage, fx_haircut=fx_haircut, effective_value_per_unit=effective_value_per_unit, opportunity_rate=opportunity_rate, cost_per_unit_of_value=cost_per_unit_of_value, concentration_cap=concentration_cap, settlement_date=settlement_date, rank=rank, exclusion_reason=exclusion_reason)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

