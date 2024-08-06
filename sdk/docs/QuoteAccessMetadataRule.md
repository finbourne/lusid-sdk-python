# QuoteAccessMetadataRule


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | [**QuoteAccessMetadataRuleId**](QuoteAccessMetadataRuleId.md) |  | 
**metadata** | **Dict[str, List[AccessMetadataValue]]** | The access control metadata to assign to quotes that match the identifier | 

## Example

```python
from lusid.models.quote_access_metadata_rule import QuoteAccessMetadataRule

# TODO update the JSON string below
json = "{}"
# create an instance of QuoteAccessMetadataRule from a JSON string
quote_access_metadata_rule_instance = QuoteAccessMetadataRule.from_json(json)
# print the JSON string representation of the object
print QuoteAccessMetadataRule.to_json()

# convert the object into a dict
quote_access_metadata_rule_dict = quote_access_metadata_rule_instance.to_dict()
# create an instance of QuoteAccessMetadataRule from a dict
quote_access_metadata_rule_form_dict = quote_access_metadata_rule.from_dict(quote_access_metadata_rule_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


