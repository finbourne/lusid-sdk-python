# TransactionRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**transaction_id** | **str** | The unique identifier of the transaction. | 
**type** | **str** | The type of the transaction, for example &#39;Buy&#39; or &#39;Sell&#39;. The transaction type must have been pre-configured using the System Configuration API. If not, this operation will succeed but you are not able to calculate holdings for the portfolio that include this transaction. | 
**instrument_identifiers** | **Dict[str, str]** | A set of instrument identifiers that can resolve the transaction to a unique instrument. | 
**transaction_date** | **str** | The date of the transaction. | 
**settlement_date** | **str** | The settlement date of the transaction. | 
**units** | **float** | The number of units of the transacted instrument. | 
**transaction_price** | [**TransactionPrice**](TransactionPrice.md) |  | [optional] 
**total_consideration** | [**CurrencyAndAmount**](CurrencyAndAmount.md) |  | 
**exchange_rate** | **float** | The exchange rate between the transaction and settlement currency (settlement currency being represented by TotalConsideration.Currency). For example, if the transaction currency is USD and the settlement currency is GBP, this would be the appropriate USD/GBP rate. | [optional] 
**transaction_currency** | **str** | The transaction currency. | [optional] 
**properties** | [**Dict[str, PerpetualProperty]**](PerpetualProperty.md) | A list of unique transaction properties and associated values to store for the transaction. Each property must be from the &#39;Transaction&#39; domain. | [optional] 
**counterparty_id** | **str** | The identifier for the counterparty of the transaction. | [optional] 
**source** | **str** | The source of the transaction. This is used to look up the appropriate transaction group set in the transaction type configuration. | [optional] 
**otc_confirmation** | [**OtcConfirmation**](OtcConfirmation.md) |  | [optional] 
**order_id** | [**ResourceId**](ResourceId.md) |  | [optional] 
**allocation_id** | [**ResourceId**](ResourceId.md) |  | [optional] 
**custodian_account_id** | [**ResourceId**](ResourceId.md) |  | [optional] 
**transaction_group_id** | **str** | The identifier for grouping economic events across multiple transactions | [optional] 
**strategy_tag** | [**List[Strategy]**](Strategy.md) | A list of strategies representing the allocation of units across multiple sub-holding keys | [optional] 
## Example

```python
from lusid.models.transaction_request import TransactionRequest
from typing import Any, Dict, List, Optional, Union
from pydantic.v1 import BaseModel, Field, StrictFloat, StrictInt, StrictStr, conlist, constr

transaction_id: StrictStr = "example_transaction_id"
type: StrictStr = "example_type"
instrument_identifiers: Dict[str, StrictStr] = # Replace with your value
transaction_date: StrictStr = "example_transaction_date"
settlement_date: StrictStr = "example_settlement_date"
units: Union[StrictFloat, StrictInt] = # Replace with your value
transaction_price: Optional[TransactionPrice] = # Replace with your value
total_consideration: CurrencyAndAmount = # Replace with your value
exchange_rate: Optional[Union[StrictFloat, StrictInt]] = # Replace with your value
transaction_currency: Optional[StrictStr] = "example_transaction_currency"
properties: Optional[Dict[str, PerpetualProperty]] = # Replace with your value
counterparty_id: Optional[StrictStr] = "example_counterparty_id"
source: Optional[StrictStr] = "example_source"
otc_confirmation: Optional[OtcConfirmation] = # Replace with your value
order_id: Optional[ResourceId] = # Replace with your value
allocation_id: Optional[ResourceId] = # Replace with your value
custodian_account_id: Optional[ResourceId] = # Replace with your value
transaction_group_id: Optional[StrictStr] = "example_transaction_group_id"
strategy_tag: Optional[conlist(Strategy)] = # Replace with your value
transaction_request_instance = TransactionRequest(transaction_id=transaction_id, type=type, instrument_identifiers=instrument_identifiers, transaction_date=transaction_date, settlement_date=settlement_date, units=units, transaction_price=transaction_price, total_consideration=total_consideration, exchange_rate=exchange_rate, transaction_currency=transaction_currency, properties=properties, counterparty_id=counterparty_id, source=source, otc_confirmation=otc_confirmation, order_id=order_id, allocation_id=allocation_id, custodian_account_id=custodian_account_id, transaction_group_id=transaction_group_id, strategy_tag=strategy_tag)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

