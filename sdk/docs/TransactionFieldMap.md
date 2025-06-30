# TransactionFieldMap

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**transaction_id** | **str** |  | 
**type** | **str** |  | 
**source** | **str** |  | 
**instrument** | **str** |  | 
**transaction_date** | **str** |  | 
**settlement_date** | **str** |  | 
**units** | **str** |  | 
**transaction_price** | [**TransactionPriceAndType**](TransactionPriceAndType.md) |  | [optional] 
**transaction_currency** | **str** |  | 
**exchange_rate** | **str** |  | [optional] 
**total_consideration** | [**TransactionCurrencyAndAmount**](TransactionCurrencyAndAmount.md) |  | 
## Example

```python
from lusid.models.transaction_field_map import TransactionFieldMap
from typing import Any, Dict, Optional
from pydantic.v1 import BaseModel, Field, constr

transaction_id: StrictStr = "example_transaction_id"
type: StrictStr = "example_type"
source: StrictStr = "example_source"
instrument: StrictStr = "example_instrument"
transaction_date: StrictStr = "example_transaction_date"
settlement_date: StrictStr = "example_settlement_date"
units: StrictStr = "example_units"
transaction_price: Optional[TransactionPriceAndType] = # Replace with your value
transaction_currency: StrictStr = "example_transaction_currency"
exchange_rate: Optional[StrictStr] = "example_exchange_rate"
total_consideration: TransactionCurrencyAndAmount = # Replace with your value
transaction_field_map_instance = TransactionFieldMap(transaction_id=transaction_id, type=type, source=source, instrument=instrument, transaction_date=transaction_date, settlement_date=settlement_date, units=units, transaction_price=transaction_price, transaction_currency=transaction_currency, exchange_rate=exchange_rate, total_consideration=total_consideration)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

