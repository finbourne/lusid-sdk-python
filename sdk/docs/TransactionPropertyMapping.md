# TransactionPropertyMapping

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**property_key** | **str** | The key that uniquely identifies the property. It has the format {domain}/{scope}/{code} | 
**map_from** | **str** | The Property Key of the Property to map from | [optional] 
**set_to** | **object** | A pointer to the Property being mapped from | [optional] 
## Example

```python
from lusid.models.transaction_property_mapping import TransactionPropertyMapping
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

property_key: StrictStr = "example_property_key"
map_from: Optional[StrictStr] = "example_map_from"
set_to: Optional[Any] = # Replace with your value
transaction_property_mapping_instance = TransactionPropertyMapping(property_key=property_key, map_from=map_from, set_to=set_to)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

