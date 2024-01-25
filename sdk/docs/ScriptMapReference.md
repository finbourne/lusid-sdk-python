# ScriptMapReference

Provides information about the location of a script map within the configuration store

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**scope** | **str** | The scope of the configuration store entry where the translation map is located. | 
**code** | **str** | The code of the configuration store entry where the translation map is located. | 
**key** | **str** | The key of the configuration store entry where the translation map is located. | 

## Example

```python
from lusid.models.script_map_reference import ScriptMapReference

# TODO update the JSON string below
json = "{}"
# create an instance of ScriptMapReference from a JSON string
script_map_reference_instance = ScriptMapReference.from_json(json)
# print the JSON string representation of the object
print ScriptMapReference.to_json()

# convert the object into a dict
script_map_reference_dict = script_map_reference_instance.to_dict()
# create an instance of ScriptMapReference from a dict
script_map_reference_form_dict = script_map_reference.from_dict(script_map_reference_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


