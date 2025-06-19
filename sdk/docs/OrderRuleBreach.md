# OrderRuleBreach


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**breach_task_id** | **str** | Uniquely identifies this historical order breach workflow task. | 
**compliance_state** | **str** | The compliance state of this order breach. Possible values are &#39;Pending&#39;, &#39;Failed&#39;, &#39;Manually approved&#39;, &#39;Passed&#39; and &#39;Warning&#39;. | 

## Example

```python
from lusid.models.order_rule_breach import OrderRuleBreach

# TODO update the JSON string below
json = "{}"
# create an instance of OrderRuleBreach from a JSON string
order_rule_breach_instance = OrderRuleBreach.from_json(json)
# print the JSON string representation of the object
print OrderRuleBreach.to_json()

# convert the object into a dict
order_rule_breach_dict = order_rule_breach_instance.to_dict()
# create an instance of OrderRuleBreach from a dict
order_rule_breach_form_dict = order_rule_breach.from_dict(order_rule_breach_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


