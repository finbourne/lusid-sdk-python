# TransactionPropertyMap

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**property_key** | **str** | The key that uniquely identifies the property. It has the format {domain}/{scope}/{code}. | [optional] 
**value** | **str** |  | [optional] 
## Example

```python
from lusid.models.transaction_property_map import TransactionPropertyMap
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

property_key: Optional[StrictStr] = "example_property_key"
value: Optional[StrictStr] = "example_value"
transaction_property_map_instance = TransactionPropertyMap(property_key=property_key, value=value)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

