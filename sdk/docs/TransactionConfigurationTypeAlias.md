# TransactionConfigurationTypeAlias

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | The transaction type | 
**description** | **str** | Brief description of the transaction | 
**transaction_class** | **str** | Relates types of a similar class. E.g. Buy/Sell, StockIn/StockOut | 
**transaction_group** | **str** | Group is a set of codes related to a source, or sync. DEPRECATED: This field will be removed, use &#x60;Source&#x60; instead | [optional] 
**source** | **str** | Used to group a set of transaction types | [optional] 
**transaction_roles** | **str** | . The available values are: None, LongLonger, LongShorter, ShortShorter, Shorter, ShortLonger, Longer, AllRoles | 
**is_default** | **bool** | IsDefault is a flag that denotes the default alias for a source. There can only be, at most, one per source. | [optional] 
## Example

```python
from lusid.models.transaction_configuration_type_alias import TransactionConfigurationTypeAlias
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

type: StrictStr = "example_type"
description: StrictStr = "example_description"
transaction_class: StrictStr = "example_transaction_class"
transaction_group: Optional[StrictStr] = "example_transaction_group"
source: Optional[StrictStr] = "example_source"
transaction_roles: StrictStr = "example_transaction_roles"
is_default: Optional[StrictBool] = # Replace with your value
is_default:Optional[StrictBool] = None
transaction_configuration_type_alias_instance = TransactionConfigurationTypeAlias(type=type, description=description, transaction_class=transaction_class, transaction_group=transaction_group, source=source, transaction_roles=transaction_roles, is_default=is_default)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

