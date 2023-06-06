# MarketContext

Market context node. This defines how LUSID processes parts of a request that require resolution of market data such as instrument prices or  Fx rates. It controls where the data is loaded from and which sources take precedence.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**market_rules** | [**List[MarketDataKeyRule]**](MarketDataKeyRule.md) | The set of rules that define how to resolve particular use cases. These can be relatively general or specific in nature.  Nominally any number are possible and will be processed in order where applicable. However, there is evidently a potential  for increased computational cost where many rules must be applied to resolve data. Ensuring that portfolios are structured in  such a way as to reduce the number of rules required is therefore sensible. | [optional] 
**suppliers** | [**MarketContextSuppliers**](MarketContextSuppliers.md) |  | [optional] 
**options** | [**MarketOptions**](MarketOptions.md) |  | [optional] 
**specific_rules** | [**List[MarketDataSpecificRule]**](MarketDataSpecificRule.md) | Extends market data key rules to be able to catch dependencies depending on where the dependency comes from, as opposed to what the dependency is asking for.  Using two specific rules, one could instruct rates curves requested by bonds to be retrieved from a different scope than rates curves requested by swaps.  WARNING: The use of specific rules impacts performance. Where possible, one should use MarketDataKeyRules only. | [optional] 

## Example

```python
from lusid.models.market_context import MarketContext

# TODO update the JSON string below
json = "{}"
# create an instance of MarketContext from a JSON string
market_context_instance = MarketContext.from_json(json)
# print the JSON string representation of the object
print MarketContext.to_json()

# convert the object into a dict
market_context_dict = market_context_instance.to_dict()
# create an instance of MarketContext from a dict
market_context_form_dict = market_context.from_dict(market_context_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


