# OrderBySpec


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** | The key that uniquely identifies a queryable address in Lusid. | 
**sort_order** | **str** | The available values are: Ascending, Descending | 

## Example

```python
from lusid.models.order_by_spec import OrderBySpec

# TODO update the JSON string below
json = "{}"
# create an instance of OrderBySpec from a JSON string
order_by_spec_instance = OrderBySpec.from_json(json)
# print the JSON string representation of the object
print OrderBySpec.to_json()

# convert the object into a dict
order_by_spec_dict = order_by_spec_instance.to_dict()
# create an instance of OrderBySpec from a dict
order_by_spec_form_dict = order_by_spec.from_dict(order_by_spec_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


