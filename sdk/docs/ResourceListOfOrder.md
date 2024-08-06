# ResourceListOfOrder


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**values** | [**List[Order]**](Order.md) |  | 
**href** | **str** |  | [optional] 
**links** | [**List[Link]**](Link.md) |  | [optional] 
**next_page** | **str** |  | [optional] 
**previous_page** | **str** |  | [optional] 

## Example

```python
from lusid.models.resource_list_of_order import ResourceListOfOrder

# TODO update the JSON string below
json = "{}"
# create an instance of ResourceListOfOrder from a JSON string
resource_list_of_order_instance = ResourceListOfOrder.from_json(json)
# print the JSON string representation of the object
print ResourceListOfOrder.to_json()

# convert the object into a dict
resource_list_of_order_dict = resource_list_of_order_instance.to_dict()
# create an instance of ResourceListOfOrder from a dict
resource_list_of_order_form_dict = resource_list_of_order.from_dict(resource_list_of_order_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


