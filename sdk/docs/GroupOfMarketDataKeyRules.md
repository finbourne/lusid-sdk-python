# GroupOfMarketDataKeyRules

Represents a collection of MarketDataKeyRules that should be resolved together when resolving market data.  That is, market data resolution will always attempt to resolve with all rules in the group  before deciding what market data to return.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**market_data_key_rule_group_operation** | **str** | The operation that will be used to process the collection of market data items and failures found on resolution  into a single market data item or failure to be used.  Supported values: [FirstLatest, AverageOfQuotesFound, AverageOfAllQuotes, FirstMinimum, FirstMaximum] | 
**market_rules** | [**List[MarketDataKeyRule]**](MarketDataKeyRule.md) | The rules that should be grouped together in market data resolution. | 

## Example

```python
from lusid.models.group_of_market_data_key_rules import GroupOfMarketDataKeyRules

# TODO update the JSON string below
json = "{}"
# create an instance of GroupOfMarketDataKeyRules from a JSON string
group_of_market_data_key_rules_instance = GroupOfMarketDataKeyRules.from_json(json)
# print the JSON string representation of the object
print GroupOfMarketDataKeyRules.to_json()

# convert the object into a dict
group_of_market_data_key_rules_dict = group_of_market_data_key_rules_instance.to_dict()
# create an instance of GroupOfMarketDataKeyRules from a dict
group_of_market_data_key_rules_form_dict = group_of_market_data_key_rules.from_dict(group_of_market_data_key_rules_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


