# ResourceListOfQuoteAccessMetadataRule


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**values** | [**List[QuoteAccessMetadataRule]**](QuoteAccessMetadataRule.md) |  | 
**href** | **str** |  | [optional] 
**links** | [**List[Link]**](Link.md) |  | [optional] 
**next_page** | **str** |  | [optional] 
**previous_page** | **str** |  | [optional] 

## Example

```python
from lusid.models.resource_list_of_quote_access_metadata_rule import ResourceListOfQuoteAccessMetadataRule

# TODO update the JSON string below
json = "{}"
# create an instance of ResourceListOfQuoteAccessMetadataRule from a JSON string
resource_list_of_quote_access_metadata_rule_instance = ResourceListOfQuoteAccessMetadataRule.from_json(json)
# print the JSON string representation of the object
print ResourceListOfQuoteAccessMetadataRule.to_json()

# convert the object into a dict
resource_list_of_quote_access_metadata_rule_dict = resource_list_of_quote_access_metadata_rule_instance.to_dict()
# create an instance of ResourceListOfQuoteAccessMetadataRule from a dict
resource_list_of_quote_access_metadata_rule_form_dict = resource_list_of_quote_access_metadata_rule.from_dict(resource_list_of_quote_access_metadata_rule_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


