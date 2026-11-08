# CollateralAllocationLine

One asset chosen for a margin call, with what a transaction moving it needs: the instrument, the portfolio and  account it leaves, the units, the price and the consideration. An override that fails a constraint is kept with  its exclusion reason and covers nothing.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**instrument_id** | **str** | The LUSID instrument identifier of the asset, or CCY_ and the currency code for cash. | 
**instrument_identifiers** | **Dict[str, Optional[str]]** | The instrument identifiers a transaction for the line is booked against. | 
**portfolio_id** | [**ResourceId**](ResourceId.md) |  | 
**custodian_account** | [**ResourceId**](ResourceId.md) |  | [optional] 
**currency** | **str** | The currency the asset is denominated in, when known. | [optional] 
**units** | **float** | The units to move. | 
**price** | **float** | The market value per unit in the base currency, before any haircut. Null when the asset could not be priced. | [optional] 
**consideration** | **float** | Units times price in the base currency: what a transaction for the line settles. Null when the asset could not be priced. | [optional] 
**effective_value_per_unit** | **float** | Price times the valuation percentage, less the FX haircut: what one unit counts for as collateral. | [optional] 
**collateral_value** | **float** | The collateral value the line covers: units times the effective value per unit. | 
**cost_per_unit_of_value** | **float** | The ranking key: the annual cost of one unit of collateral value from this asset. | [optional] 
**settlement_date** | **datetime** | When the movement would settle under the agreement&#39;s settlement lag, counting weekdays. | [optional] 
**bound_by** | **str** | Which limit decided the units. One of RemainingRequirement, FreeUnits, ConcentrationCap, LotRounding or Override. | 
**exclusion_reason** | **str** | The constraint the asset failed, when it did. One of NotEligible, NoFreeUnits, MissingPrice, MissingRate, MissesDeadline, BelowMinimumLot or ConcentrationExhausted. Null when it passed. | [optional] 
## Example

```python
from lusid.models.collateral_allocation_line import CollateralAllocationLine
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

instrument_id: StrictStr = "example_instrument_id"
instrument_identifiers: Dict[str, Optional[StrictStr]] = # Replace with your value
portfolio_id: ResourceId = # Replace with your value
custodian_account: Optional[ResourceId] = # Replace with your value
currency: Optional[StrictStr] = "example_currency"
units: Union[StrictFloat, StrictInt] = # Replace with your value
price: Optional[Union[StrictFloat, StrictInt]] = # Replace with your value
consideration: Optional[Union[StrictFloat, StrictInt]] = # Replace with your value
effective_value_per_unit: Optional[Union[StrictFloat, StrictInt]] = # Replace with your value
collateral_value: Union[StrictFloat, StrictInt] = # Replace with your value
cost_per_unit_of_value: Optional[Union[StrictFloat, StrictInt]] = # Replace with your value
settlement_date: Optional[datetime] = # Replace with your value
bound_by: StrictStr = "example_bound_by"
exclusion_reason: Optional[StrictStr] = "example_exclusion_reason"
collateral_allocation_line_instance = CollateralAllocationLine(instrument_id=instrument_id, instrument_identifiers=instrument_identifiers, portfolio_id=portfolio_id, custodian_account=custodian_account, currency=currency, units=units, price=price, consideration=consideration, effective_value_per_unit=effective_value_per_unit, collateral_value=collateral_value, cost_per_unit_of_value=cost_per_unit_of_value, settlement_date=settlement_date, bound_by=bound_by, exclusion_reason=exclusion_reason)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

