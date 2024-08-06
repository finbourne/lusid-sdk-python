# UpdateCutLabelDefinitionRequest

This request specifies a new Cut Label Definition

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**display_name** | **str** |  | 
**description** | **str** |  | [optional] 
**cut_local_time** | [**CutLocalTime**](CutLocalTime.md) |  | 
**time_zone** | **str** |  | 

## Example

```python
from lusid.models.update_cut_label_definition_request import UpdateCutLabelDefinitionRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateCutLabelDefinitionRequest from a JSON string
update_cut_label_definition_request_instance = UpdateCutLabelDefinitionRequest.from_json(json)
# print the JSON string representation of the object
print UpdateCutLabelDefinitionRequest.to_json()

# convert the object into a dict
update_cut_label_definition_request_dict = update_cut_label_definition_request_instance.to_dict()
# create an instance of UpdateCutLabelDefinitionRequest from a dict
update_cut_label_definition_request_form_dict = update_cut_label_definition_request.from_dict(update_cut_label_definition_request_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


