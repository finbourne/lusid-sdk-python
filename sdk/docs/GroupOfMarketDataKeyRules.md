# GroupOfMarketDataKeyRules

Represents a collection of MarketDataKeyRules that should be resolved together when resolving market data. That is, market data resolution will always attempt to resolve with all rules in the group before deciding what market data to return.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**market_data_key_rule_group_operation** | **str** | The operation that will be used to process the collection of market data items and failures found on resolution into a single market data item or failure to be used. Supported values: [FirstLatest, AverageOfQuotesFound, AverageOfAllQuotes, FirstMinimum, FirstMaximum] | 
**market_rules** | [**List[MarketDataKeyRule]**](MarketDataKeyRule.md) | The rules that should be grouped together in market data resolution. | 
## Example

```python
from lusid.models.group_of_market_data_key_rules import GroupOfMarketDataKeyRules
from typing import Any, Dict, List
from pydantic.v1 import BaseModel, Field, conlist, constr

market_data_key_rule_group_operation: StrictStr = "example_market_data_key_rule_group_operation"
market_rules: conlist(MarketDataKeyRule) = # Replace with your value
group_of_market_data_key_rules_instance = GroupOfMarketDataKeyRules(market_data_key_rule_group_operation=market_data_key_rule_group_operation, market_rules=market_rules)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

