# BlockAndOrderIdRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**destination_block_id** | [**ResourceId**](ResourceId.md) |  | 
**order_id** | [**ResourceId**](ResourceId.md) |  | 

## Example

```python
from lusid.models.block_and_order_id_request import BlockAndOrderIdRequest

# TODO update the JSON string below
json = "{}"
# create an instance of BlockAndOrderIdRequest from a JSON string
block_and_order_id_request_instance = BlockAndOrderIdRequest.from_json(json)
# print the JSON string representation of the object
print BlockAndOrderIdRequest.to_json()

# convert the object into a dict
block_and_order_id_request_dict = block_and_order_id_request_instance.to_dict()
# create an instance of BlockAndOrderIdRequest from a dict
block_and_order_id_request_form_dict = block_and_order_id_request.from_dict(block_and_order_id_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


