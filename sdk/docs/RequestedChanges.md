# RequestedChanges

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attribute_count** | **int** | Number of attributes staged change applies to | [optional] 
**attribute_names** | **List[str]** | Names of the attributes the staged change applies to. | [optional] 
## Example

```python
from lusid.models.requested_changes import RequestedChanges
from typing import Any, Dict, List, Optional
from pydantic.v1 import BaseModel, Field, StrictInt, StrictStr, conlist

attribute_count: Optional[StrictInt] = # Replace with your value
attribute_count: Optional[StrictInt] = None
attribute_names: Optional[conlist(StrictStr)] = # Replace with your value
requested_changes_instance = RequestedChanges(attribute_count=attribute_count, attribute_names=attribute_names)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

