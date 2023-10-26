# OrderFlowConfiguration


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**include_entity_types** | **str** |  | 

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


