# CleardownModuleDetails

A Cleardown Module request definition

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**display_name** | **str** | The name of the Cleardown Module. | 
**description** | **str** | A description for the Cleardown Module. | [optional] 
**status** | **str** | The Cleardown Module status. Can be Active or Inactive. Defaults to Active. | 

## Example

```python
from lusid.models.cleardown_module_details import CleardownModuleDetails

# TODO update the JSON string below
json = "{}"
# create an instance of CleardownModuleDetails from a JSON string
cleardown_module_details_instance = CleardownModuleDetails.from_json(json)
# print the JSON string representation of the object
print CleardownModuleDetails.to_json()

# convert the object into a dict
cleardown_module_details_dict = cleardown_module_details_instance.to_dict()
# create an instance of CleardownModuleDetails from a dict
cleardown_module_details_form_dict = cleardown_module_details.from_dict(cleardown_module_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


