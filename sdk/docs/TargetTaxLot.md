# TargetTaxLot

Used to specify holdings target amounts at the tax-lot level
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**units** | **float** | The number of units of the instrument in this tax-lot. | 
**cost** | [**CurrencyAndAmount**](CurrencyAndAmount.md) |  | [optional] 
**portfolio_cost** | **float** | The total cost of the tax-lot in the transaction portfolio&#39;s base currency. | [optional] 
**price** | **float** | The purchase price of each unit of the instrument held in this tax-lot. This forms part of the unique key required for multiple tax-lots. | [optional] 
**purchase_date** | **datetime** | The purchase date of this tax-lot. This forms part of the unique key required for multiple tax-lots. | [optional] 
**settlement_date** | **datetime** | The settlement date of the tax-lot&#39;s opening transaction. | [optional] 
**notional_cost** | **float** | The notional cost of the tax-lot&#39;s opening transaction. | [optional] 
**variation_margin** | **float** | The variation margin of the tax-lot&#39;s opening transaction. | [optional] 
**variation_margin_portfolio_ccy** | **float** | The variation margin in portfolio currency of the tax-lot&#39;s opening transaction. | [optional] 
## Example

```python
from lusid.models.target_tax_lot import TargetTaxLot
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

units: Union[StrictFloat, StrictInt] = # Replace with your value
cost: Optional[CurrencyAndAmount] = None
portfolio_cost: Optional[Union[StrictFloat, StrictInt]] = # Replace with your value
price: Optional[Union[StrictFloat, StrictInt]] = # Replace with your value
purchase_date: Optional[datetime] = # Replace with your value
settlement_date: Optional[datetime] = # Replace with your value
notional_cost: Optional[Union[StrictFloat, StrictInt]] = # Replace with your value
variation_margin: Optional[Union[StrictFloat, StrictInt]] = # Replace with your value
variation_margin_portfolio_ccy: Optional[Union[StrictFloat, StrictInt]] = # Replace with your value
target_tax_lot_instance = TargetTaxLot(units=units, cost=cost, portfolio_cost=portfolio_cost, price=price, purchase_date=purchase_date, settlement_date=settlement_date, notional_cost=notional_cost, variation_margin=variation_margin, variation_margin_portfolio_ccy=variation_margin_portfolio_ccy)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

