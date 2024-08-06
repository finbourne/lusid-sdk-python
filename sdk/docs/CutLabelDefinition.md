# CutLabelDefinition


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** |  | [optional] 
**display_name** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**cut_local_time** | [**CutLocalTime**](CutLocalTime.md) |  | [optional] 
**time_zone** | **str** |  | [optional] 
**href** | **str** |  | [optional] 
**version** | [**Version**](Version.md) |  | [optional] 
**links** | [**List[Link]**](Link.md) |  | [optional] 

## Example

```python
from lusid.models.cut_label_definition import CutLabelDefinition

# TODO update the JSON string below
json = "{}"
# create an instance of CutLabelDefinition from a JSON string
cut_label_definition_instance = CutLabelDefinition.from_json(json)
# print the JSON string representation of the object
print CutLabelDefinition.to_json()

# convert the object into a dict
cut_label_definition_dict = cut_label_definition_instance.to_dict()
# create an instance of CutLabelDefinition from a dict
cut_label_definition_form_dict = cut_label_definition.from_dict(cut_label_definition_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


