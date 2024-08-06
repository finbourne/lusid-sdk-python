# CleardownModuleRulesUpdatedResponse

A Cleardown Module rules update response

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**rules** | [**List[CleardownModuleRule]**](CleardownModuleRule.md) | The Cleardown Rules that apply for the Cleardown Module. Rules are evaluated in the order they occur in this collection. | [optional] 
**version** | [**Version**](Version.md) |  | [optional] 
**href** | **str** | The specific Uniform Resource Identifier (URI) for this resource at the requested effective and asAt datetime. | [optional] 
**links** | [**List[Link]**](Link.md) |  | [optional] 

## Example

```python
from lusid.models.cleardown_module_rules_updated_response import CleardownModuleRulesUpdatedResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CleardownModuleRulesUpdatedResponse from a JSON string
cleardown_module_rules_updated_response_instance = CleardownModuleRulesUpdatedResponse.from_json(json)
# print the JSON string representation of the object
print CleardownModuleRulesUpdatedResponse.to_json()

# convert the object into a dict
cleardown_module_rules_updated_response_dict = cleardown_module_rules_updated_response_instance.to_dict()
# create an instance of CleardownModuleRulesUpdatedResponse from a dict
cleardown_module_rules_updated_response_form_dict = cleardown_module_rules_updated_response.from_dict(cleardown_module_rules_updated_response_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


