# UpsertQuoteAccessMetadataRuleRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | [**QuoteAccessMetadataRuleId**](QuoteAccessMetadataRuleId.md) |  | 
**metadata** | **Dict[str, List[AccessMetadataValue]]** | The access control metadata to assign to quotes that match the identifier | 

## Example

```python
from lusid.models.upsert_quote_access_metadata_rule_request import UpsertQuoteAccessMetadataRuleRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpsertQuoteAccessMetadataRuleRequest from a JSON string
upsert_quote_access_metadata_rule_request_instance = UpsertQuoteAccessMetadataRuleRequest.from_json(json)
# print the JSON string representation of the object
print UpsertQuoteAccessMetadataRuleRequest.to_json()

# convert the object into a dict
upsert_quote_access_metadata_rule_request_dict = upsert_quote_access_metadata_rule_request_instance.to_dict()
# create an instance of UpsertQuoteAccessMetadataRuleRequest from a dict
upsert_quote_access_metadata_rule_request_form_dict = upsert_quote_access_metadata_rule_request.from_dict(upsert_quote_access_metadata_rule_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


