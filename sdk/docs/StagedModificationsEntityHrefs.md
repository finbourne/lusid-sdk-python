# StagedModificationsEntityHrefs


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**when_staged** | **str** | The specific Uniform Resource Identifier (URI) for the staged modification change at the time when the change was requested. | [optional] 
**preview** | **str** | The specific Uniform Resource Identifier (URI) for the preview of staged modification change once applied. | [optional] 
**latest** | **str** | The specific Uniform Resource Identifier (URI) for the staged modification at latest time. | [optional] 
**links** | [**List[Link]**](Link.md) |  | [optional] 

## Example

```python
from lusid.models.staged_modifications_entity_hrefs import StagedModificationsEntityHrefs

# TODO update the JSON string below
json = "{}"
# create an instance of StagedModificationsEntityHrefs from a JSON string
staged_modifications_entity_hrefs_instance = StagedModificationsEntityHrefs.from_json(json)
# print the JSON string representation of the object
print StagedModificationsEntityHrefs.to_json()

# convert the object into a dict
staged_modifications_entity_hrefs_dict = staged_modifications_entity_hrefs_instance.to_dict()
# create an instance of StagedModificationsEntityHrefs from a dict
staged_modifications_entity_hrefs_form_dict = staged_modifications_entity_hrefs.from_dict(staged_modifications_entity_hrefs_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


