# PagedResourceListOfOrderBreachHistory


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**next_page** | **str** |  | [optional] 
**previous_page** | **str** |  | [optional] 
**values** | [**List[OrderBreachHistory]**](OrderBreachHistory.md) |  | 
**href** | **str** |  | [optional] 
**links** | [**List[Link]**](Link.md) |  | [optional] 

## Example

```python
from lusid.models.paged_resource_list_of_order_breach_history import PagedResourceListOfOrderBreachHistory

# TODO update the JSON string below
json = "{}"
# create an instance of PagedResourceListOfOrderBreachHistory from a JSON string
paged_resource_list_of_order_breach_history_instance = PagedResourceListOfOrderBreachHistory.from_json(json)
# print the JSON string representation of the object
print PagedResourceListOfOrderBreachHistory.to_json()

# convert the object into a dict
paged_resource_list_of_order_breach_history_dict = paged_resource_list_of_order_breach_history_instance.to_dict()
# create an instance of PagedResourceListOfOrderBreachHistory from a dict
paged_resource_list_of_order_breach_history_form_dict = paged_resource_list_of_order_breach_history.from_dict(paged_resource_list_of_order_breach_history_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


