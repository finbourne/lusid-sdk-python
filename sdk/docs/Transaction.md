# Transaction

A list of transactions.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**transaction_id** | **str** | The unique identifier for the transaction. | 
**type** | **str** | The type of the transaction e.g. &#39;Buy&#39;, &#39;Sell&#39;. The transaction type should have been pre-configured via the System Configuration API endpoint. | 
**instrument_identifiers** | **Dict[str, Optional[str]]** | A set of instrument identifiers that can resolve the transaction to a unique instrument. | [optional] 
**instrument_scope** | **str** | The scope in which the transaction&#39;s instrument lies. | [optional] 
**instrument_uid** | **str** | The unique Lusid Instrument Id (LUID) of the instrument that the transaction is in. | 
**transaction_date** | **datetime** | The date of the transaction. | 
**settlement_date** | **datetime** | The settlement date of the transaction. | 
**units** | **float** | The number of units transacted in the associated instrument. | 
**transaction_price** | [**TransactionPrice**](TransactionPrice.md) |  | [optional] 
**total_consideration** | [**CurrencyAndAmount**](CurrencyAndAmount.md) |  | 
**exchange_rate** | **float** | The exchange rate between the transaction and settlement currency (settlement currency being represented by the TotalConsideration.Currency). For example if the transaction currency is in USD and the settlement currency is in GBP this this the USD/GBP rate. | [optional] 
**transaction_currency** | **str** | The transaction currency. | [optional] 
**properties** | [**Dict[str, PerpetualProperty]**](PerpetualProperty.md) | Set of unique transaction properties and associated values to stored with the transaction. Each property will be from the &#39;Transaction&#39; domain. | [optional] 
**counterparty_id** | **str** | The identifier for the counterparty of the transaction. | [optional] 
**source** | **str** | The source of the transaction. This is used to look up the appropriate transaction group set in the transaction type configuration. | [optional] 
**entry_date_time** | **datetime** | The asAt datetime that the transaction was added to LUSID. | [optional] 
**otc_confirmation** | [**OtcConfirmation**](OtcConfirmation.md) |  | [optional] 
**transaction_status** | **str** | The status of the transaction. The available values are: Active, Amended, Cancelled, ActiveReversal, ActiveTrueUp, CancelledTrueUp | [optional] 
**cancel_date_time** | **datetime** | If the transaction has been cancelled, the asAt datetime that the transaction was cancelled. | [optional] 
**order_id** | [**ResourceId**](ResourceId.md) |  | [optional] 
**allocation_id** | [**ResourceId**](ResourceId.md) |  | [optional] 
**custodian_account** | [**CustodianAccount**](CustodianAccount.md) |  | [optional] 
**transaction_group_id** | **str** | The identifier for grouping economic events across multiple transactions | [optional] 
**strategy_tag** | [**List[Strategy]**](Strategy.md) | A list of strategies representing the allocation of units across multiple sub-holding keys | [optional] 
**resolved_transaction_type_details** | [**TransactionTypeDetails**](TransactionTypeDetails.md) |  | [optional] 
**data_model_membership** | [**DataModelMembership**](DataModelMembership.md) |  | [optional] 
## Example

```python
from lusid.models.transaction import Transaction
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

transaction_id: StrictStr = "example_transaction_id"
type: StrictStr = "example_type"
instrument_identifiers: Optional[Dict[str, Optional[StrictStr]]] = # Replace with your value
instrument_scope: Optional[StrictStr] = "example_instrument_scope"
instrument_uid: StrictStr = "example_instrument_uid"
transaction_date: datetime = # Replace with your value
settlement_date: datetime = # Replace with your value
units: Union[StrictFloat, StrictInt] = # Replace with your value
transaction_price: Optional[TransactionPrice] = # Replace with your value
total_consideration: CurrencyAndAmount = # Replace with your value
exchange_rate: Optional[Union[StrictFloat, StrictInt]] = # Replace with your value
transaction_currency: Optional[StrictStr] = "example_transaction_currency"
properties: Optional[Dict[str, PerpetualProperty]] = # Replace with your value
counterparty_id: Optional[StrictStr] = "example_counterparty_id"
source: Optional[StrictStr] = "example_source"
entry_date_time: Optional[datetime] = # Replace with your value
otc_confirmation: Optional[OtcConfirmation] = # Replace with your value
transaction_status: Optional[StrictStr] = "example_transaction_status"
cancel_date_time: Optional[datetime] = # Replace with your value
order_id: Optional[ResourceId] = # Replace with your value
allocation_id: Optional[ResourceId] = # Replace with your value
custodian_account: Optional[CustodianAccount] = # Replace with your value
transaction_group_id: Optional[StrictStr] = "example_transaction_group_id"
strategy_tag: Optional[List[Strategy]] = # Replace with your value
resolved_transaction_type_details: Optional[TransactionTypeDetails] = # Replace with your value
data_model_membership: Optional[DataModelMembership] = # Replace with your value
transaction_instance = Transaction(transaction_id=transaction_id, type=type, instrument_identifiers=instrument_identifiers, instrument_scope=instrument_scope, instrument_uid=instrument_uid, transaction_date=transaction_date, settlement_date=settlement_date, units=units, transaction_price=transaction_price, total_consideration=total_consideration, exchange_rate=exchange_rate, transaction_currency=transaction_currency, properties=properties, counterparty_id=counterparty_id, source=source, entry_date_time=entry_date_time, otc_confirmation=otc_confirmation, transaction_status=transaction_status, cancel_date_time=cancel_date_time, order_id=order_id, allocation_id=allocation_id, custodian_account=custodian_account, transaction_group_id=transaction_group_id, strategy_tag=strategy_tag, resolved_transaction_type_details=resolved_transaction_type_details, data_model_membership=data_model_membership)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

