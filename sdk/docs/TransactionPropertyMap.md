# TransactionPropertyMap

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**property_key** | **str** | The key that uniquely identifies the property. It has the format {domain}/{scope}/{code}. | [optional] 
**value** | **str** |  | [optional] 
## Example

```python
from lusid.models.transaction_property_map import TransactionPropertyMap
from typing import Any, Dict, Optional
from pydantic.v1 import BaseModel, Field, StrictStr, constr

property_key: Optional[StrictStr] = "example_property_key"
value: Optional[StrictStr] = "example_value"
transaction_property_map_instance = TransactionPropertyMap(property_key=property_key, value=value)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

