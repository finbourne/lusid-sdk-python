# BlockSetRequest

A request to create or update multiple Blocks.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**requests** | [**List[BlockRequest]**](BlockRequest.md) | A collection of BlockRequests. | [optional] 

## Example

```python
from lusid.models.block_set_request import BlockSetRequest

# TODO update the JSON string below
json = "{}"
# create an instance of BlockSetRequest from a JSON string
block_set_request_instance = BlockSetRequest.from_json(json)
# print the JSON string representation of the object
print BlockSetRequest.to_json()

# convert the object into a dict
block_set_request_dict = block_set_request_instance.to_dict()
# create an instance of BlockSetRequest from a dict
block_set_request_form_dict = block_set_request.from_dict(block_set_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


