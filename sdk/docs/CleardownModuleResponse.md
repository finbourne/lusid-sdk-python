# CleardownModuleResponse

A Cleardown Module definition

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**href** | **str** | The specific Uniform Resource Identifier (URI) for this resource at the requested effective and asAt datetime. | [optional] 
**cleardown_module_code** | **str** | The code of the Cleardown Module. | 
**chart_of_accounts_id** | [**ResourceId**](ResourceId.md) |  | 
**display_name** | **str** | The name of the Cleardown Module. | 
**description** | **str** | A description for the Cleardown Module. | [optional] 
**rules** | [**List[CleardownModuleRule]**](CleardownModuleRule.md) | The Cleardown Rules that apply for the Cleardown Module. Rules are evaluated in the order they occur in this collection. | [optional] 
**status** | **str** | The Cleardown Module status. Can be Active, Inactive or Deleted. Defaults to Active. | 
**version** | [**Version**](Version.md) |  | [optional] 
**links** | [**List[Link]**](Link.md) |  | [optional] 

## Example

```python
from lusid.models.cleardown_module_response import CleardownModuleResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CleardownModuleResponse from a JSON string
cleardown_module_response_instance = CleardownModuleResponse.from_json(json)
# print the JSON string representation of the object
print CleardownModuleResponse.to_json()

# convert the object into a dict
cleardown_module_response_dict = cleardown_module_response_instance.to_dict()
# create an instance of CleardownModuleResponse from a dict
cleardown_module_response_form_dict = cleardown_module_response.from_dict(cleardown_module_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


