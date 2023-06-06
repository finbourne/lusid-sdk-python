# ResourceListOfAggregatedReturn


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**values** | [**List[AggregatedReturn]**](AggregatedReturn.md) |  | 
**href** | **str** |  | [optional] 
**links** | [**List[Link]**](Link.md) |  | [optional] 
**next_page** | **str** |  | [optional] 
**previous_page** | **str** |  | [optional] 

## Example

```python
from lusid.models.resource_list_of_aggregated_return import ResourceListOfAggregatedReturn

# TODO update the JSON string below
json = "{}"
# create an instance of ResourceListOfAggregatedReturn from a JSON string
resource_list_of_aggregated_return_instance = ResourceListOfAggregatedReturn.from_json(json)
# print the JSON string representation of the object
print ResourceListOfAggregatedReturn.to_json()

# convert the object into a dict
resource_list_of_aggregated_return_dict = resource_list_of_aggregated_return_instance.to_dict()
# create an instance of ResourceListOfAggregatedReturn from a dict
resource_list_of_aggregated_return_form_dict = resource_list_of_aggregated_return.from_dict(resource_list_of_aggregated_return_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


