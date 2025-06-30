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
from typing import Any, Dict, List, Optional
from pydantic.v1 import BaseModel, Field, StrictStr, conlist

columns: Optional[conlist(StrictStr)] = # Replace with your value
values: Optional[conlist(ResultValue)] = # Replace with your value
grouped_result_of_address_key_instance = GroupedResultOfAddressKey(columns=columns, values=values)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

