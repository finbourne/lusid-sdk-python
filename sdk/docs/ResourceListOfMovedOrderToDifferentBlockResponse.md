# ResourceListOfMovedOrderToDifferentBlockResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**values** | [**List[MovedOrderToDifferentBlockResponse]**](MovedOrderToDifferentBlockResponse.md) |  | 
**href** | **str** |  | [optional] 
**links** | [**List[Link]**](Link.md) |  | [optional] 
**next_page** | **str** |  | [optional] 
**previous_page** | **str** |  | [optional] 

## Example

```python
from lusid.models.resource_list_of_moved_order_to_different_block_response import ResourceListOfMovedOrderToDifferentBlockResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ResourceListOfMovedOrderToDifferentBlockResponse from a JSON string
resource_list_of_moved_order_to_different_block_response_instance = ResourceListOfMovedOrderToDifferentBlockResponse.from_json(json)
# print the JSON string representation of the object
print ResourceListOfMovedOrderToDifferentBlockResponse.to_json()

# convert the object into a dict
resource_list_of_moved_order_to_different_block_response_dict = resource_list_of_moved_order_to_different_block_response_instance.to_dict()
# create an instance of ResourceListOfMovedOrderToDifferentBlockResponse from a dict
resource_list_of_moved_order_to_different_block_response_form_dict = resource_list_of_moved_order_to_different_block_response.from_dict(resource_list_of_moved_order_to_different_block_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


