# BlockAndOrderCreateRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**requests** | [**List[BlockAndOrderRequest]**](BlockAndOrderRequest.md) | A collection of BlockAndOrderRequest. | 

## Example

```python
from lusid.models.block_and_order_create_request import BlockAndOrderCreateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of BlockAndOrderCreateRequest from a JSON string
block_and_order_create_request_instance = BlockAndOrderCreateRequest.from_json(json)
# print the JSON string representation of the object
print BlockAndOrderCreateRequest.to_json()

# convert the object into a dict
block_and_order_create_request_dict = block_and_order_create_request_instance.to_dict()
# create an instance of BlockAndOrderCreateRequest from a dict
block_and_order_create_request_form_dict = block_and_order_create_request.from_dict(block_and_order_create_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


