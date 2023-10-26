# NextValueInSequenceResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**values** | **List[str]** | The next set of values for the specified Sequence. | 
**links** | [**List[Link]**](Link.md) |  | [optional] 

## Example

```python
from lusid.models.next_value_in_sequence_response import NextValueInSequenceResponse

# TODO update the JSON string below
json = "{}"
# create an instance of NextValueInSequenceResponse from a JSON string
next_value_in_sequence_response_instance = NextValueInSequenceResponse.from_json(json)
# print the JSON string representation of the object
print NextValueInSequenceResponse.to_json()

# convert the object into a dict
next_value_in_sequence_response_dict = next_value_in_sequence_response_instance.to_dict()
# create an instance of NextValueInSequenceResponse from a dict
next_value_in_sequence_response_form_dict = next_value_in_sequence_response.from_dict(next_value_in_sequence_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


