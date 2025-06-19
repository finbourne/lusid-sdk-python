# OrderBreachHistory


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | [**ResourceId**](ResourceId.md) |  | 
**order_id** | [**ResourceId**](ResourceId.md) |  | 
**run_id** | [**ResourceId**](ResourceId.md) |  | 
**breaches_by_rule** | **Dict[str, List[OrderRuleBreach]]** | Compliance rule breaches associations with the order and run. | [optional] 
**as_at** | **datetime** | The asAt datetime at which the order breach was created in LUSID. | 

## Example

```python
from lusid.models.order_breach_history import OrderBreachHistory

# TODO update the JSON string below
json = "{}"
# create an instance of OrderBreachHistory from a JSON string
order_breach_history_instance = OrderBreachHistory.from_json(json)
# print the JSON string representation of the object
print OrderBreachHistory.to_json()

# convert the object into a dict
order_breach_history_dict = order_breach_history_instance.to_dict()
# create an instance of OrderBreachHistory from a dict
order_breach_history_form_dict = order_breach_history.from_dict(order_breach_history_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


