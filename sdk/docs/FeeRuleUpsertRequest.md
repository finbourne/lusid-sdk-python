# FeeRuleUpsertRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** |  | [optional] 
**transaction_property_key** | **str** |  | 
**transaction_type** | **str** |  | 
**country** | **str** |  | 
**counterparty** | **str** |  | 
**transaction_currency** | **str** |  | 
**settlement_currency** | **str** |  | 
**execution_broker** | **str** |  | 
**custodian** | **str** |  | 
**exchange** | **str** |  | 
**fee** | [**CalculationInfo**](CalculationInfo.md) |  | 
**min_fee** | [**CalculationInfo**](CalculationInfo.md) |  | [optional] 
**max_fee** | [**CalculationInfo**](CalculationInfo.md) |  | [optional] 
**additional_keys** | **Dict[str, str]** |  | [optional] 
**description** | **str** |  | [optional] 
## Example

```python
from lusid.models.fee_rule_upsert_request import FeeRuleUpsertRequest
from typing import Any, Dict, Optional
from pydantic.v1 import BaseModel, Field, StrictStr, constr, validator

code: Optional[StrictStr] = "example_code"
transaction_property_key: StrictStr = "example_transaction_property_key"
transaction_type: StrictStr = "example_transaction_type"
country: StrictStr = "example_country"
counterparty: StrictStr = "example_counterparty"
transaction_currency: StrictStr = "example_transaction_currency"
settlement_currency: StrictStr = "example_settlement_currency"
execution_broker: StrictStr = "example_execution_broker"
custodian: StrictStr = "example_custodian"
exchange: StrictStr = "example_exchange"
fee: CalculationInfo = # Replace with your value
min_fee: Optional[CalculationInfo] = # Replace with your value
max_fee: Optional[CalculationInfo] = # Replace with your value
additional_keys: Optional[Dict[str, StrictStr]] = # Replace with your value
description: Optional[StrictStr] = "example_description"
fee_rule_upsert_request_instance = FeeRuleUpsertRequest(code=code, transaction_property_key=transaction_property_key, transaction_type=transaction_type, country=country, counterparty=counterparty, transaction_currency=transaction_currency, settlement_currency=settlement_currency, execution_broker=execution_broker, custodian=custodian, exchange=exchange, fee=fee, min_fee=min_fee, max_fee=max_fee, additional_keys=additional_keys, description=description)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

