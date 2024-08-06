# Change

The time an entity was modified (amendment and/or historical correction).

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**href** | **str** |  | [optional] 
**entity_id** | [**ResourceId**](ResourceId.md) |  | 
**corrected** | **bool** |  | 
**correction_effective_at** | **datetime** |  | [optional] 
**correction_as_at** | **datetime** |  | [optional] 
**amended** | **bool** |  | 
**amendment_effective_at** | **datetime** |  | [optional] 
**amendment_as_at** | **datetime** |  | [optional] 
**links** | [**List[Link]**](Link.md) |  | [optional] 

## Example

```python
from lusid.models.change import Change

# TODO update the JSON string below
json = "{}"
# create an instance of Change from a JSON string
change_instance = Change.from_json(json)
# print the JSON string representation of the object
print Change.to_json()

# convert the object into a dict
change_dict = change_instance.to_dict()
# create an instance of Change from a dict
change_form_dict = change.from_dict(change_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


