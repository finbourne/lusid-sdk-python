# GetFlowConventionsResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**href** | **str** | The specific Uniform Resource Identifier (URI) for this resource at the requested effective and asAt datetime. | [optional] 
**value** | [**FlowConventions**](FlowConventions.md) |  | [optional] 
**failed** | [**Dict[str, ErrorDetail]**](ErrorDetail.md) | The identifiers that did not resolve to a conventions along with the nature of the failure. | [optional] 
**links** | [**List[Link]**](Link.md) |  | [optional] 

## Example

```python
from lusid.models.get_flow_conventions_response import GetFlowConventionsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetFlowConventionsResponse from a JSON string
get_flow_conventions_response_instance = GetFlowConventionsResponse.from_json(json)
# print the JSON string representation of the object
print GetFlowConventionsResponse.to_json()

# convert the object into a dict
get_flow_conventions_response_dict = get_flow_conventions_response_instance.to_dict()
# create an instance of GetFlowConventionsResponse from a dict
get_flow_conventions_response_form_dict = get_flow_conventions_response.from_dict(get_flow_conventions_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


