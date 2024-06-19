# OrderFlowConfiguration


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**include_entity_types** | **str** | Controls whether Orders and Allocations orders are included in the Portfolio valuation.  Valid values are  None (to account for Transactions only), Allocations (to include Allocations and Transactions) and  OrdersAndAllocations (to include Orders, Allocations and Transactions). | 

## Example

```python
from lusid.models.order_flow_configuration import OrderFlowConfiguration

# TODO update the JSON string below
json = "{}"
# create an instance of OrderFlowConfiguration from a JSON string
order_flow_configuration_instance = OrderFlowConfiguration.from_json(json)
# print the JSON string representation of the object
print OrderFlowConfiguration.to_json()

# convert the object into a dict
order_flow_configuration_dict = order_flow_configuration_instance.to_dict()
# create an instance of OrderFlowConfiguration from a dict
order_flow_configuration_form_dict = order_flow_configuration.from_dict(order_flow_configuration_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


