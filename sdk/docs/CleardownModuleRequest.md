# CleardownModuleRequest

A Cleardown Module request definition

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** | The code of the Cleardown Module. | 
**display_name** | **str** | The name of the Cleardown Module. | 
**description** | **str** | A description for the Cleardown Module. | [optional] 
**rules** | [**List[CleardownModuleRule]**](CleardownModuleRule.md) | The Cleardown Rules that apply for the Cleardown Module. Rules are evaluated in the order they occur in this collection. | [optional] 

## Example

```python
from lusid.models.cleardown_module_request import CleardownModuleRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CleardownModuleRequest from a JSON string
cleardown_module_request_instance = CleardownModuleRequest.from_json(json)
# print the JSON string representation of the object
print CleardownModuleRequest.to_json()

# convert the object into a dict
cleardown_module_request_dict = cleardown_module_request_instance.to_dict()
# create an instance of CleardownModuleRequest from a dict
cleardown_module_request_form_dict = cleardown_module_request.from_dict(cleardown_module_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


