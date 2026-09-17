# StoredOverrideDefinition

A single replacement transaction definition as it was persisted against a virtual transaction.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**transaction_id** | **str** | The unique identifier of the replacement transaction. | [optional] 
**type** | **str** | The type of the replacement transaction, for example &#39;Buy&#39; or &#39;Sell&#39;. | [optional] 
**instrument_identifiers** | **Dict[str, Optional[str]]** | A set of instrument identifiers that resolve the replacement transaction to a unique instrument. | [optional] 
**trade_date** | **str** | The trade date of the replacement transaction. | [optional] 
**settlement_date** | **str** | The settlement date of the replacement transaction. | [optional] 
**units** | **float** | The number of units of the transacted instrument. | [optional] 
**trade_price** | [**TransactionPrice**](TransactionPrice.md) |  | [optional] 
**total_consideration** | [**CurrencyAndAmount**](CurrencyAndAmount.md) |  | [optional] 
**exchange_rate** | **float** | The exchange rate between the trade and settlement currency. | [optional] 
**trade_currency** | **str** | The trade currency of the replacement transaction. | [optional] 
**properties** | [**Dict[str, PerpetualProperty]**](PerpetualProperty.md) | The transaction properties stored for the replacement transaction. | [optional] 
**counterparty_id** | **str** | The identifier for the counterparty of the replacement transaction. | [optional] 
**source** | **str** | The source of the replacement transaction. | [optional] 
## Example

```python
from lusid.models.stored_override_definition import StoredOverrideDefinition
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

transaction_id: Optional[StrictStr] = "example_transaction_id"
type: Optional[StrictStr] = "example_type"
instrument_identifiers: Optional[Dict[str, Optional[StrictStr]]] = # Replace with your value
trade_date: Optional[StrictStr] = "example_trade_date"
settlement_date: Optional[StrictStr] = "example_settlement_date"
units: Optional[Union[StrictFloat, StrictInt]] = # Replace with your value
trade_price: Optional[TransactionPrice] = # Replace with your value
total_consideration: Optional[CurrencyAndAmount] = # Replace with your value
exchange_rate: Optional[Union[StrictFloat, StrictInt]] = # Replace with your value
trade_currency: Optional[StrictStr] = "example_trade_currency"
properties: Optional[Dict[str, PerpetualProperty]] = # Replace with your value
counterparty_id: Optional[StrictStr] = "example_counterparty_id"
source: Optional[StrictStr] = "example_source"
stored_override_definition_instance = StoredOverrideDefinition(transaction_id=transaction_id, type=type, instrument_identifiers=instrument_identifiers, trade_date=trade_date, settlement_date=settlement_date, units=units, trade_price=trade_price, total_consideration=total_consideration, exchange_rate=exchange_rate, trade_currency=trade_currency, properties=properties, counterparty_id=counterparty_id, source=source)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

