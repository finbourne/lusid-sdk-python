# PreTradeConfiguration

Specification object for the pre trade configuration parameters of a compliance run

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**include_entity_types** | **str** | Controls whether Orders and Allocations orders are included in the Portfolio valuation done for this compliance run.  Valid values are:  None (to account for Transactions only), Allocations (to include Allocations and Transactions) and  OrdersAndAllocations (to include Orders, Allocations and Transactions). | 

## Example

```python
from lusid.models.pre_trade_configuration import PreTradeConfiguration

# TODO update the JSON string below
json = "{}"
# create an instance of PreTradeConfiguration from a JSON string
pre_trade_configuration_instance = PreTradeConfiguration.from_json(json)
# print the JSON string representation of the object
print PreTradeConfiguration.to_json()

# convert the object into a dict
pre_trade_configuration_dict = pre_trade_configuration_instance.to_dict()
# create an instance of PreTradeConfiguration from a dict
pre_trade_configuration_form_dict = pre_trade_configuration.from_dict(pre_trade_configuration_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


