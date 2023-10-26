# CreateCutLabelDefinitionRequest

This request specifies a new Cut Label Definition

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** |  | 
**display_name** | **str** |  | 
**description** | **str** |  | [optional] 
**cut_local_time** | [**CutLocalTime**](CutLocalTime.md) |  | 
**time_zone** | **str** |  | 

## Example

```python
from lusid.models.create_cut_label_definition_request import CreateCutLabelDefinitionRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateCutLabelDefinitionRequest from a JSON string
create_cut_label_definition_request_instance = CreateCutLabelDefinitionRequest.from_json(json)
# print the JSON string representation of the object
print CreateCutLabelDefinitionRequest.to_json()

# convert the object into a dict
create_cut_label_definition_request_dict = create_cut_label_definition_request_instance.to_dict()
# create an instance of CreateCutLabelDefinitionRequest from a dict
create_cut_label_definition_request_form_dict = create_cut_label_definition_request.from_dict(create_cut_label_definition_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


