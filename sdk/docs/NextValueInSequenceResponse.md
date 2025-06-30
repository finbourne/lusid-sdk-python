# NextValueInSequenceResponse

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**values** | **List[str]** | The next set of values for the specified Sequence. | 
**links** | [**List[Link]**](Link.md) |  | [optional] 
## Example

```python
from lusid.models.next_value_in_sequence_response import NextValueInSequenceResponse
from typing import Any, Dict, List, Optional
from pydantic.v1 import BaseModel, Field, StrictStr, conlist

values: conlist(StrictStr) = # Replace with your value
links: Optional[conlist(Link)] = None
next_value_in_sequence_response_instance = NextValueInSequenceResponse(values=values, links=links)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

