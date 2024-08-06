# PostingModuleRulesUpdatedResponse

A Posting Module rules update response

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**rules** | [**List[PostingModuleRule]**](PostingModuleRule.md) | The Posting Rules that apply for the Posting Module. Rules are evaluated in the order they occur in this collection. | [optional] 
**version** | [**Version**](Version.md) |  | [optional] 
**href** | **str** | The specific Uniform Resource Identifier (URI) for this resource at the requested effective and asAt datetime. | [optional] 
**links** | [**List[Link]**](Link.md) |  | [optional] 

## Example

```python
from lusid.models.posting_module_rules_updated_response import PostingModuleRulesUpdatedResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PostingModuleRulesUpdatedResponse from a JSON string
posting_module_rules_updated_response_instance = PostingModuleRulesUpdatedResponse.from_json(json)
# print the JSON string representation of the object
print PostingModuleRulesUpdatedResponse.to_json()

# convert the object into a dict
posting_module_rules_updated_response_dict = posting_module_rules_updated_response_instance.to_dict()
# create an instance of PostingModuleRulesUpdatedResponse from a dict
posting_module_rules_updated_response_form_dict = posting_module_rules_updated_response.from_dict(posting_module_rules_updated_response_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


