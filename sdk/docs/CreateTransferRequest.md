# CreateTransferRequest

A request to create a transfer: the paired transaction legs that move a position, and the Transfer entity  recording them.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**transfer_id** | [**ResourceId**](ResourceId.md) |  | 
**portfolio_id_out** | [**ResourceId**](ResourceId.md) |  | 
**portfolio_id_in** | [**ResourceId**](ResourceId.md) |  | 
**instrument_identifier_out** | **str** |  | 
**instrument_identifier_in** | **str** |  | 
**pricing_method** | **str** | Available values: AtCost, AtPrice. | 
**tax_lot_structure** | **str** | Available values: Consolidate, Preserve. | [optional] 
**units_out** | **float** |  | 
**units_in** | **float** |  | 
**amount_out** | **float** |  | [optional] 
**weight_out** | **float** |  | [optional] 
**trade_date_out** | **datetime** |  | 
**trade_date_in** | **datetime** |  | 
**settlement_date_out** | **datetime** |  | 
**settlement_date_in** | **datetime** |  | [optional] 
**exchange_rate_out** | **float** |  | [optional] 
**exchange_rate_in** | **float** |  | [optional] 
**transaction_price_out** | **float** |  | [optional] 
**transaction_price_in** | **float** |  | [optional] 
**counterparty_id_out** | **str** |  | [optional] 
**counterparty_id_in** | **str** |  | [optional] 
**custodian_account_id_out** | [**ResourceId**](ResourceId.md) |  | [optional] 
**custodian_account_id_in** | [**ResourceId**](ResourceId.md) |  | [optional] 
**source** | **str** |  | 
**accounting_method** | **str** | Available values: AverageCost, FirstInFirstOut, LastInFirstOut, HighestCostFirst, LowestCostFirst, ProRateByUnits, ProRateByCost, ProRateByCostPortfolioCurrency, IntraDayThenFirstInFirstOut, LongTermHighestCostFirst, LongTermHighestCostFirstPortfolioCurrency, HighestCostFirstPortfolioCurrency, LowestCostFirstPortfolioCurrency, MaximumLossMinimumGain, MaximumLossMinimumGainPortfolioCurrency. | [optional] 
**properties** | [**Dict[str, PerpetualProperty]**](PerpetualProperty.md) |  | [optional] 
**properties_in** | [**Dict[str, PerpetualProperty]**](PerpetualProperty.md) |  | [optional] 
## Example

```python
from lusid.models.create_transfer_request import CreateTransferRequest
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

transfer_id: ResourceId = # Replace with your value
portfolio_id_out: ResourceId = # Replace with your value
portfolio_id_in: ResourceId = # Replace with your value
instrument_identifier_out: StrictStr = "example_instrument_identifier_out"
instrument_identifier_in: StrictStr = "example_instrument_identifier_in"
pricing_method: StrictStr = "example_pricing_method"
tax_lot_structure: Optional[StrictStr] = "example_tax_lot_structure"
units_out: Union[StrictFloat, StrictInt] = # Replace with your value
units_in: Union[StrictFloat, StrictInt] = # Replace with your value
amount_out: Optional[Union[StrictFloat, StrictInt]] = # Replace with your value
weight_out: Optional[Union[StrictFloat, StrictInt]] = # Replace with your value
trade_date_out: datetime = # Replace with your value
trade_date_in: datetime = # Replace with your value
settlement_date_out: datetime = # Replace with your value
settlement_date_in: Optional[datetime] = # Replace with your value
exchange_rate_out: Optional[Union[StrictFloat, StrictInt]] = # Replace with your value
exchange_rate_in: Optional[Union[StrictFloat, StrictInt]] = # Replace with your value
transaction_price_out: Optional[Union[StrictFloat, StrictInt]] = # Replace with your value
transaction_price_in: Optional[Union[StrictFloat, StrictInt]] = # Replace with your value
counterparty_id_out: Optional[StrictStr] = "example_counterparty_id_out"
counterparty_id_in: Optional[StrictStr] = "example_counterparty_id_in"
custodian_account_id_out: Optional[ResourceId] = # Replace with your value
custodian_account_id_in: Optional[ResourceId] = # Replace with your value
source: StrictStr = "example_source"
accounting_method: Optional[StrictStr] = "example_accounting_method"
properties: Optional[Dict[str, PerpetualProperty]] = None
properties_in: Optional[Dict[str, PerpetualProperty]] = # Replace with your value
create_transfer_request_instance = CreateTransferRequest(transfer_id=transfer_id, portfolio_id_out=portfolio_id_out, portfolio_id_in=portfolio_id_in, instrument_identifier_out=instrument_identifier_out, instrument_identifier_in=instrument_identifier_in, pricing_method=pricing_method, tax_lot_structure=tax_lot_structure, units_out=units_out, units_in=units_in, amount_out=amount_out, weight_out=weight_out, trade_date_out=trade_date_out, trade_date_in=trade_date_in, settlement_date_out=settlement_date_out, settlement_date_in=settlement_date_in, exchange_rate_out=exchange_rate_out, exchange_rate_in=exchange_rate_in, transaction_price_out=transaction_price_out, transaction_price_in=transaction_price_in, counterparty_id_out=counterparty_id_out, counterparty_id_in=counterparty_id_in, custodian_account_id_out=custodian_account_id_out, custodian_account_id_in=custodian_account_id_in, source=source, accounting_method=accounting_method, properties=properties, properties_in=properties_in)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

