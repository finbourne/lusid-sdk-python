# ResourceListOfAggregationQuery


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**values** | [**List[AggregationQuery]**](AggregationQuery.md) |  | 
**href** | **str** |  | [optional] 
**links** | [**List[Link]**](Link.md) |  | [optional] 
**next_page** | **str** |  | [optional] 
**previous_page** | **str** |  | [optional] 

## Example

```python
from lusid.models.resource_list_of_aggregation_query import ResourceListOfAggregationQuery

# TODO update the JSON string below
json = "{}"
# create an instance of ResourceListOfAggregationQuery from a JSON string
resource_list_of_aggregation_query_instance = ResourceListOfAggregationQuery.from_json(json)
# print the JSON string representation of the object
print ResourceListOfAggregationQuery.to_json()

# convert the object into a dict
resource_list_of_aggregation_query_dict = resource_list_of_aggregation_query_instance.to_dict()
# create an instance of ResourceListOfAggregationQuery from a dict
resource_list_of_aggregation_query_form_dict = resource_list_of_aggregation_query.from_dict(resource_list_of_aggregation_query_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


