# CreateTransferRequest

A request to create a transfer: the paired transaction legs that move a position, and the Transfer entity  recording them.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**transfer_id** | [**ResourceId**](ResourceId.md) |  | 
**portfolio_id_out** | [**ResourceId**](ResourceId.md) |  | 
**portfolio_id_in** | [**ResourceId**](ResourceId.md) |  | 
**instrument_identifier_out** | **str** | The LUSID instrument id of the instrument moving out. A position in this instrument must exist in the outgoing portfolio on the outgoing trade date. | 
**instrument_identifier_in** | **str** | The LUSID instrument id of the instrument moving in. Equal to InstrumentIdentifierOut for a transfer between portfolios. | 
**pricing_method** | **str** | How the legs are priced. &#39;AtCost&#39; uses the cost per unit of the outgoing holding; &#39;AtPrice&#39; uses the supplied TransactionPriceOut, which is then required. Available values: AtCost, AtPrice. | 
**tax_lot_structure** | **str** | What happens to the tax lots of the outgoing position. Only &#39;Consolidate&#39; is currently supported; &#39;Preserve&#39; is rejected. Defaults to &#39;Consolidate&#39;. Available values: Consolidate, Preserve. | [optional] 
**units_out** | **float** | The number of units to move out. Must be greater than zero. | 
**units_in** | **float** | The number of units to move in. Must be greater than zero. | 
**amount_out** | **float** | The total consideration of the outgoing leg. Recorded, not applied. | [optional] 
**weight_out** | **float** | The weighting factor of the outgoing leg. Recorded, not applied. | [optional] 
**trade_date_out** | **datetime** | The trade date of the outgoing leg. Must not be later than TradeDateIn. | 
**trade_date_in** | **datetime** | The trade date of the incoming leg. | 
**settlement_date_out** | **datetime** | The settlement date of the outgoing leg. Must not be later than SettlementDateIn. | 
**settlement_date_in** | **datetime** | The settlement date of the incoming leg. Defaults to SettlementDateOut when not supplied. | [optional] 
**exchange_rate_out** | **float** | The FX rate to apply to the outgoing leg. | [optional] 
**exchange_rate_in** | **float** | The FX rate to apply to the incoming leg. | [optional] 
**transaction_price_out** | **float** | The unit price of the outgoing leg. Required when PricingMethod is &#39;AtPrice&#39;, and ignored when it is &#39;AtCost&#39;. | [optional] 
**transaction_price_in** | **float** | The unit price of the incoming leg. Ignored for a transfer, which carries the outgoing price across; defaults to the outgoing price for a switch. | [optional] 
**counterparty_id_out** | **str** | The counterparty identifier of the outgoing leg. | [optional] 
**counterparty_id_in** | **str** | The counterparty identifier of the incoming leg. Defaults to CounterpartyIdOut. | [optional] 
**custodian_account_id_out** | [**ResourceId**](ResourceId.md) |  | [optional] 
**custodian_account_id_in** | [**ResourceId**](ResourceId.md) |  | [optional] 
**source** | **str** | The transaction source the generated legs are booked against. | 
**accounting_method** | **str** | An accounting method to record against the transfer. Available values: AverageCost, FirstInFirstOut, LastInFirstOut, HighestCostFirst, LowestCostFirst, ProRateByUnits, ProRateByCost, ProRateByCostPortfolioCurrency, IntraDayThenFirstInFirstOut, LongTermHighestCostFirst, LongTermHighestCostFirstPortfolioCurrency, HighestCostFirstPortfolioCurrency, LowestCostFirstPortfolioCurrency, MaximumLossMinimumGain, MaximumLossMinimumGainPortfolioCurrency. | [optional] 
**properties_out** | [**Dict[str, PerpetualProperty]**](PerpetualProperty.md) | Transaction Properties to set on the outgoing transaction leg, and on the incoming transaction leg when PropertiesIn is absent. Supplying an empty collection for PropertiesIn leaves the incoming leg with no properties. | [optional] 
**properties_in** | [**Dict[str, PerpetualProperty]**](PerpetualProperty.md) | Transaction Properties to set on the incoming transaction leg, replacing rather than adding to PropertiesOut. | [optional] 
**properties** | [**Dict[str, PerpetualProperty]**](PerpetualProperty.md) | Properties to set on the transfer itself, in the Transfer domain. These are separate from PropertiesOut and PropertiesIn, which are Transaction domain and land on the legs. | [optional] 
**transaction_to_portfolio_rate_out** | **float** | The rate from the outgoing leg&#39;s trade currency to the outgoing portfolio&#39;s base currency, applied whenever supplied. | [optional] 
**transaction_to_portfolio_rate_in** | **float** | The rate from the incoming leg&#39;s trade currency to the incoming portfolio&#39;s base currency. Required when the two portfolios have different base currencies, and applied whenever supplied. | [optional] 
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
properties_out: Optional[Dict[str, PerpetualProperty]] = # Replace with your value
properties_in: Optional[Dict[str, PerpetualProperty]] = # Replace with your value
properties: Optional[Dict[str, PerpetualProperty]] = # Replace with your value
transaction_to_portfolio_rate_out: Optional[Union[StrictFloat, StrictInt]] = # Replace with your value
transaction_to_portfolio_rate_in: Optional[Union[StrictFloat, StrictInt]] = # Replace with your value
create_transfer_request_instance = CreateTransferRequest(transfer_id=transfer_id, portfolio_id_out=portfolio_id_out, portfolio_id_in=portfolio_id_in, instrument_identifier_out=instrument_identifier_out, instrument_identifier_in=instrument_identifier_in, pricing_method=pricing_method, tax_lot_structure=tax_lot_structure, units_out=units_out, units_in=units_in, amount_out=amount_out, weight_out=weight_out, trade_date_out=trade_date_out, trade_date_in=trade_date_in, settlement_date_out=settlement_date_out, settlement_date_in=settlement_date_in, exchange_rate_out=exchange_rate_out, exchange_rate_in=exchange_rate_in, transaction_price_out=transaction_price_out, transaction_price_in=transaction_price_in, counterparty_id_out=counterparty_id_out, counterparty_id_in=counterparty_id_in, custodian_account_id_out=custodian_account_id_out, custodian_account_id_in=custodian_account_id_in, source=source, accounting_method=accounting_method, properties_out=properties_out, properties_in=properties_in, properties=properties, transaction_to_portfolio_rate_out=transaction_to_portfolio_rate_out, transaction_to_portfolio_rate_in=transaction_to_portfolio_rate_in)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

