# A2BCategory

A2B Category - one of the five major categories in the A2BDataRecord

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**holding_currency** | [**A2BBreakdown**](A2BBreakdown.md) |  | [optional] 
**portfolio_currency** | [**A2BBreakdown**](A2BBreakdown.md) |  | [optional] 

## Example

```python
from lusid.models.a2_b_category import A2BCategory

# TODO update the JSON string below
json = "{}"
# create an instance of A2BCategory from a JSON string
a2_b_category_instance = A2BCategory.from_json(json)
# print the JSON string representation of the object
print A2BCategory.to_json()

# convert the object into a dict
a2_b_category_dict = a2_b_category_instance.to_dict()
# create an instance of A2BCategory from a dict
a2_b_category_form_dict = a2_b_category.from_dict(a2_b_category_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


