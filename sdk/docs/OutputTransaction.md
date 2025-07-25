# OutputTransaction

A list of output transactions.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**transaction_id** | **str** | The unique identifier for the transaction. | 
**type** | **str** | The type of the transaction e.g. &#39;Buy&#39;, &#39;Sell&#39;. The transaction type should have been pre-configured via the System Configuration API endpoint. | 
**description** | **str** | The description of the transaction. This only exists on transactions generated by LUSID e.g. a holdings adjustment transaction. | [optional] 
**instrument_identifiers** | **Dict[str, str]** | A set of instrument identifiers that can resolve the transaction to a unique instrument. | [optional] 
**instrument_scope** | **str** | The scope in which the instrument lies. | [optional] 
**instrument_uid** | **str** | The unique Lusid Instrument Id (LUID) of the instrument that the transaction is in. | 
**transaction_date** | **datetime** | The date of the transaction. | 
**settlement_date** | **datetime** | The settlement date of the transaction. | 
**units** | **float** | The number of units transacted in the associated instrument. | 
**transaction_amount** | **float** | The total value of the transaction in the transaction currency. | [optional] 
**transaction_price** | [**TransactionPrice**](TransactionPrice.md) |  | [optional] 
**total_consideration** | [**CurrencyAndAmount**](CurrencyAndAmount.md) |  | [optional] 
**exchange_rate** | **float** | The exchange rate between the transaction and settlement currency (settlement currency being represented by the TotalConsideration.Currency). For example if the transaction currency is in USD and the settlement currency is in GBP this this the USD/GBP rate. | [optional] 
**transaction_to_portfolio_rate** | **float** | The exchange rate between the transaction and portfolio currency. For example if the transaction currency is in USD and the portfolio currency is in GBP this this the USD/GBP rate. | [optional] 
**transaction_currency** | **str** | The transaction currency. | [optional] 
**properties** | [**Dict[str, PerpetualProperty]**](PerpetualProperty.md) | Set of unique transaction properties and associated values to stored with the transaction. Each property will be from the &#39;Transaction&#39; domain. | [optional] 
**counterparty_id** | **str** | The identifier for the counterparty of the transaction. | [optional] 
**source** | **str** | The source of the transaction. This is used to look up the appropriate transaction group set in the transaction type configuration. | [optional] 
**transaction_status** | **str** | The status of the transaction. The available values are: Active, Amended, Cancelled, ActiveReversal, ActiveTrueUp, CancelledTrueUp | [optional] 
**entry_date_time** | **datetime** | The asAt datetime that the transaction was added to LUSID. | [optional] 
**cancel_date_time** | **datetime** | If the transaction has been cancelled, the asAt datetime that the transaction was cancelled. | [optional] 
**realised_gain_loss** | [**List[RealisedGainLoss]**](RealisedGainLoss.md) | The collection of realised gains or losses resulting from relevant transactions e.g. a sale transaction. The cost used in calculating the realised gain or loss is determined by the accounting method defined when the transaction portfolio is created. | [optional] 
**holding_ids** | **List[int]** | The collection of single identifiers for the holding within the portfolio. The holdingId is constructed from the LusidInstrumentId, sub-holding keys and currrency and is unique within the portfolio. | [optional] 
**source_type** | **str** | The type of source that the transaction originated from, eg: InputTransaction, InstrumentEvent, HoldingAdjustment | [optional] 
**source_instrument_event_id** | **str** | The unique ID of the instrument event that the transaction is related to. | [optional] 
**custodian_account** | [**CustodianAccount**](CustodianAccount.md) |  | [optional] 
**transaction_group_id** | **str** | The identifier for grouping economic events across multiple transactions | [optional] 
**resolved_transaction_type_details** | [**TransactionTypeDetails**](TransactionTypeDetails.md) |  | [optional] 
**gross_transaction_amount** | **float** | The total gross value of the transaction in the transaction currency. | [optional] 
**otc_confirmation** | [**OtcConfirmation**](OtcConfirmation.md) |  | [optional] 
**order_id** | [**ResourceId**](ResourceId.md) |  | [optional] 
**allocation_id** | [**ResourceId**](ResourceId.md) |  | [optional] 
**accounting_date** | **datetime** | The accounting date of the transaction. | [optional] 
**economics** | [**List[Economics]**](Economics.md) | Set of economic data related with the transaction impacts. | [optional] 
## Example

```python
from lusid.models.output_transaction import OutputTransaction
from typing import Any, Dict, List, Optional, Union
from pydantic.v1 import BaseModel, Field, StrictFloat, StrictInt, StrictStr, conlist, constr, validator
from datetime import datetime
transaction_id: StrictStr = "example_transaction_id"
type: StrictStr = "example_type"
description: Optional[StrictStr] = "example_description"
instrument_identifiers: Optional[Dict[str, StrictStr]] = # Replace with your value
instrument_scope: Optional[StrictStr] = "example_instrument_scope"
instrument_uid: StrictStr = "example_instrument_uid"
transaction_date: datetime = # Replace with your value
settlement_date: datetime = # Replace with your value
units: Union[StrictFloat, StrictInt] = # Replace with your value
transaction_amount: Optional[Union[StrictFloat, StrictInt]] = # Replace with your value
transaction_price: Optional[TransactionPrice] = # Replace with your value
total_consideration: Optional[CurrencyAndAmount] = # Replace with your value
exchange_rate: Optional[Union[StrictFloat, StrictInt]] = # Replace with your value
transaction_to_portfolio_rate: Optional[Union[StrictFloat, StrictInt]] = # Replace with your value
transaction_currency: Optional[StrictStr] = "example_transaction_currency"
properties: Optional[Dict[str, PerpetualProperty]] = # Replace with your value
counterparty_id: Optional[StrictStr] = "example_counterparty_id"
source: Optional[StrictStr] = "example_source"
transaction_status: Optional[StrictStr] = "example_transaction_status"
entry_date_time: Optional[datetime] = # Replace with your value
cancel_date_time: Optional[datetime] = # Replace with your value
realised_gain_loss: Optional[conlist(RealisedGainLoss)] = # Replace with your value
holding_ids: Optional[conlist(StrictInt)] = # Replace with your value
source_type: Optional[StrictStr] = "example_source_type"
source_instrument_event_id: Optional[StrictStr] = "example_source_instrument_event_id"
custodian_account: Optional[CustodianAccount] = # Replace with your value
transaction_group_id: Optional[StrictStr] = "example_transaction_group_id"
resolved_transaction_type_details: Optional[TransactionTypeDetails] = # Replace with your value
gross_transaction_amount: Optional[Union[StrictFloat, StrictInt]] = # Replace with your value
otc_confirmation: Optional[OtcConfirmation] = # Replace with your value
order_id: Optional[ResourceId] = # Replace with your value
allocation_id: Optional[ResourceId] = # Replace with your value
accounting_date: Optional[datetime] = # Replace with your value
economics: Optional[conlist(Economics)] = # Replace with your value
output_transaction_instance = OutputTransaction(transaction_id=transaction_id, type=type, description=description, instrument_identifiers=instrument_identifiers, instrument_scope=instrument_scope, instrument_uid=instrument_uid, transaction_date=transaction_date, settlement_date=settlement_date, units=units, transaction_amount=transaction_amount, transaction_price=transaction_price, total_consideration=total_consideration, exchange_rate=exchange_rate, transaction_to_portfolio_rate=transaction_to_portfolio_rate, transaction_currency=transaction_currency, properties=properties, counterparty_id=counterparty_id, source=source, transaction_status=transaction_status, entry_date_time=entry_date_time, cancel_date_time=cancel_date_time, realised_gain_loss=realised_gain_loss, holding_ids=holding_ids, source_type=source_type, source_instrument_event_id=source_instrument_event_id, custodian_account=custodian_account, transaction_group_id=transaction_group_id, resolved_transaction_type_details=resolved_transaction_type_details, gross_transaction_amount=gross_transaction_amount, otc_confirmation=otc_confirmation, order_id=order_id, allocation_id=allocation_id, accounting_date=accounting_date, economics=economics)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

