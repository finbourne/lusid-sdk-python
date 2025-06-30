# TransactionTypeAlias

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | The transaction type | 
**description** | **str** | Brief description of the transaction | 
**transaction_class** | **str** | Relates types of a similar class. E.g. Buy/Sell, StockIn/StockOut | 
**transaction_roles** | **str** | Transactions role within a class. E.g. Increase a long position | 
**is_default** | **bool** | IsDefault is a flag that denotes the default alias for a source. There can only be, at most, one per source. | [optional] 
## Example

```python
from lusid.models.transaction_type_alias import TransactionTypeAlias
from typing import Any, Dict, Optional
from pydantic.v1 import BaseModel, Field, StrictBool, constr, validator

type: StrictStr = "example_type"
description: StrictStr = "example_description"
transaction_class: StrictStr = "example_transaction_class"
transaction_roles: StrictStr = "example_transaction_roles"
is_default: Optional[StrictBool] = # Replace with your value
is_default:Optional[StrictBool] = None
transaction_type_alias_instance = TransactionTypeAlias(type=type, description=description, transaction_class=transaction_class, transaction_roles=transaction_roles, is_default=is_default)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

