# PostingModuleRequest

A Posting Module request definition

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** | The code of the Posting Module. | 
**display_name** | **str** | The name of the Posting Module. | 
**description** | **str** | A description for the Posting Module. | [optional] 
**rules** | [**List[PostingModuleRule]**](PostingModuleRule.md) | The Posting Rules that apply for the Posting Module. Rules are evaluated in the order they occur in this collection. | [optional] 

## Example

```python
from lusid.models.posting_module_request import PostingModuleRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PostingModuleRequest from a JSON string
posting_module_request_instance = PostingModuleRequest.from_json(json)
# print the JSON string representation of the object
print PostingModuleRequest.to_json()

# convert the object into a dict
posting_module_request_dict = posting_module_request_instance.to_dict()
# create an instance of PostingModuleRequest from a dict
posting_module_request_form_dict = posting_module_request.from_dict(posting_module_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


