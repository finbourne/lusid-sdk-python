# Premium

A class containing information for a given premium payment.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | **float** | Premium amount. | 
**currency** | **str** | Premium currency. | 
**var_date** | **datetime** | Date when premium paid. | 

## Example

```python
from lusid.models.premium import Premium

# TODO update the JSON string below
json = "{}"
# create an instance of Premium from a JSON string
premium_instance = Premium.from_json(json)
# print the JSON string representation of the object
print Premium.to_json()

# convert the object into a dict
premium_dict = premium_instance.to_dict()
# create an instance of Premium from a dict
premium_form_dict = premium.from_dict(premium_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


