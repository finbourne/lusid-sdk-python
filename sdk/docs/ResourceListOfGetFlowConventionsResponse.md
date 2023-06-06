# ResourceListOfGetFlowConventionsResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**values** | [**List[GetFlowConventionsResponse]**](GetFlowConventionsResponse.md) |  | 
**href** | **str** |  | [optional] 
**links** | [**List[Link]**](Link.md) |  | [optional] 
**next_page** | **str** |  | [optional] 
**previous_page** | **str** |  | [optional] 

## Example

```python
from lusid.models.resource_list_of_get_flow_conventions_response import ResourceListOfGetFlowConventionsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ResourceListOfGetFlowConventionsResponse from a JSON string
resource_list_of_get_flow_conventions_response_instance = ResourceListOfGetFlowConventionsResponse.from_json(json)
# print the JSON string representation of the object
print ResourceListOfGetFlowConventionsResponse.to_json()

# convert the object into a dict
resource_list_of_get_flow_conventions_response_dict = resource_list_of_get_flow_conventions_response_instance.to_dict()
# create an instance of ResourceListOfGetFlowConventionsResponse from a dict
resource_list_of_get_flow_conventions_response_form_dict = resource_list_of_get_flow_conventions_response.from_dict(resource_list_of_get_flow_conventions_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


