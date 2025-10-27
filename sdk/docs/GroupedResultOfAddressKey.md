# GroupedResultOfAddressKey

Holder class for a group of results. It consists of a list of columns and values for that column.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**columns** | **List[str]** | The columns, or keys, for a particular group of results | [optional] 
**values** | [**List[ResultValue]**](ResultValue.md) | The values for the list of results | [optional] 
## Example

```python
from lusid.models.grouped_result_of_address_key import GroupedResultOfAddressKey
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

columns: Optional[List[StrictStr]] = # Replace with your value
values: Optional[List[ResultValue]] = # Replace with your value
grouped_result_of_address_key_instance = GroupedResultOfAddressKey(columns=columns, values=values)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

