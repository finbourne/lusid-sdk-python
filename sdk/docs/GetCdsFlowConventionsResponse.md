# GetCdsFlowConventionsResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**href** | **str** | The specific Uniform Resource Identifier (URI) for this resource at the requested effective and asAt datetime. | [optional] 
**value** | [**CdsFlowConventions**](CdsFlowConventions.md) |  | [optional] 
**failed** | [**Dict[str, ErrorDetail]**](ErrorDetail.md) | The identifiers that did not resolve to a conventions along with the nature of the failure. | [optional] 
**links** | [**List[Link]**](Link.md) |  | [optional] 

## Example

```python
from lusid.models.get_cds_flow_conventions_response import GetCdsFlowConventionsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetCdsFlowConventionsResponse from a JSON string
get_cds_flow_conventions_response_instance = GetCdsFlowConventionsResponse.from_json(json)
# print the JSON string representation of the object
print GetCdsFlowConventionsResponse.to_json()

# convert the object into a dict
get_cds_flow_conventions_response_dict = get_cds_flow_conventions_response_instance.to_dict()
# create an instance of GetCdsFlowConventionsResponse from a dict
get_cds_flow_conventions_response_form_dict = get_cds_flow_conventions_response.from_dict(get_cds_flow_conventions_response_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


