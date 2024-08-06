# PostingModuleDetails

A posting Module request definition

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**display_name** | **str** | The name of the Posting Module. | 
**description** | **str** | A description for the Posting Module. | [optional] 
**status** | **str** | The Posting Module status. Can be Active or Inactive. Defaults to Active. | 

## Example

```python
from lusid.models.posting_module_details import PostingModuleDetails

# TODO update the JSON string below
json = "{}"
# create an instance of PostingModuleDetails from a JSON string
posting_module_details_instance = PostingModuleDetails.from_json(json)
# print the JSON string representation of the object
print PostingModuleDetails.to_json()

# convert the object into a dict
posting_module_details_dict = posting_module_details_instance.to_dict()
# create an instance of PostingModuleDetails from a dict
posting_module_details_form_dict = posting_module_details.from_dict(posting_module_details_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


