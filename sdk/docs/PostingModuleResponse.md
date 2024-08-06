# PostingModuleResponse

A Posting Module definition

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**href** | **str** | The specific Uniform Resource Identifier (URI) for this resource at the requested effective and asAt datetime. | [optional] 
**posting_module_code** | **str** | The code of the Posting Module. | 
**chart_of_accounts_id** | [**ResourceId**](ResourceId.md) |  | 
**display_name** | **str** | The name of the Posting Module. | 
**description** | **str** | A description for the Posting Module. | [optional] 
**rules** | [**List[PostingModuleRule]**](PostingModuleRule.md) | The Posting Rules that apply for the Posting Module. Rules are evaluated in the order they occur in this collection. | [optional] 
**status** | **str** | The Posting Module status. Can be Active, Inactive or Deleted. Defaults to Active. | 
**version** | [**Version**](Version.md) |  | [optional] 
**links** | [**List[Link]**](Link.md) |  | [optional] 

## Example

```python
from lusid.models.posting_module_response import PostingModuleResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PostingModuleResponse from a JSON string
posting_module_response_instance = PostingModuleResponse.from_json(json)
# print the JSON string representation of the object
print PostingModuleResponse.to_json()

# convert the object into a dict
posting_module_response_dict = posting_module_response_instance.to_dict()
# create an instance of PostingModuleResponse from a dict
posting_module_response_form_dict = posting_module_response.from_dict(posting_module_response_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


