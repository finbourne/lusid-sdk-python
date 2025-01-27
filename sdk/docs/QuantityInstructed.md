# QuantityInstructed


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**amount** | **float** |  | 

## Example

```python
from lusid.models.quantity_instructed import QuantityInstructed

# TODO update the JSON string below
json = "{}"
# create an instance of QuantityInstructed from a JSON string
quantity_instructed_instance = QuantityInstructed.from_json(json)
# print the JSON string representation of the object
print QuantityInstructed.to_json()

# convert the object into a dict
quantity_instructed_dict = quantity_instructed_instance.to_dict()
# create an instance of QuantityInstructed from a dict
quantity_instructed_form_dict = quantity_instructed.from_dict(quantity_instructed_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


