# TransactionTypePropertyMapping

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**property_key** | **str** | The key that uniquely identifies the property. It has the format {domain}/{scope}/{code} | 
**map_from** | **str** | The Property Key of the Property to map from | [optional] 
**set_to** | **str** | A pointer to the Property being mapped from | [optional] 
**template_from** | **str** | The template that defines how the property value is constructed from transaction, instrument and portfolio details. | [optional] 
**nullify** | **bool** | Flag to unset the Property Key for the mapping | [optional] 
## Example

```python
from lusid.models.transaction_type_property_mapping import TransactionTypePropertyMapping
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

property_key: StrictStr = "example_property_key"
map_from: Optional[StrictStr] = "example_map_from"
set_to: Optional[StrictStr] = "example_set_to"
template_from: Optional[StrictStr] = "example_template_from"
nullify: Optional[StrictBool] = # Replace with your value
nullify:Optional[StrictBool] = None
transaction_type_property_mapping_instance = TransactionTypePropertyMapping(property_key=property_key, map_from=map_from, set_to=set_to, template_from=template_from, nullify=nullify)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

