# BlockAndOrdersCreateRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**requests** | [**List[BlockAndOrdersRequest]**](BlockAndOrdersRequest.md) | A collection of BlockAndOrdersRequest. | 

## Example

```python
from lusid.models.block_and_orders_create_request import BlockAndOrdersCreateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of BlockAndOrdersCreateRequest from a JSON string
block_and_orders_create_request_instance = BlockAndOrdersCreateRequest.from_json(json)
# print the JSON string representation of the object
print BlockAndOrdersCreateRequest.to_json()

# convert the object into a dict
block_and_orders_create_request_dict = block_and_orders_create_request_instance.to_dict()
# create an instance of BlockAndOrdersCreateRequest from a dict
block_and_orders_create_request_form_dict = block_and_orders_create_request.from_dict(block_and_orders_create_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


