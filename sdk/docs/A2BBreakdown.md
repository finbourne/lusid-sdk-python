# A2BBreakdown

A2B Breakdown - Shows the total, and each sub-element within an A2B Category

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total** | **float** | The total value of all the components within this category. | [optional] 
**currency** | **str** | The currency. Applies to the Total, as well as all the componenents. | [optional] 
**components** | **Dict[str, float]** | The individual components that make up the category. For example, the Start category may have Cost, Unrealised gains and accrued interest components. | [optional] 

## Example

```python
from lusid.models.a2_b_breakdown import A2BBreakdown

# TODO update the JSON string below
json = "{}"
# create an instance of A2BBreakdown from a JSON string
a2_b_breakdown_instance = A2BBreakdown.from_json(json)
# print the JSON string representation of the object
print A2BBreakdown.to_json()

# convert the object into a dict
a2_b_breakdown_dict = a2_b_breakdown_instance.to_dict()
# create an instance of A2BBreakdown from a dict
a2_b_breakdown_form_dict = a2_b_breakdown.from_dict(a2_b_breakdown_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


