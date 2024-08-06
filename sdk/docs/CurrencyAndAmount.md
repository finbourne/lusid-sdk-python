# CurrencyAndAmount

An amount of a specific currency, specifying a value and an associated unit

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | **float** |  | [optional] 
**currency** | **str** |  | 

## Example

```python
from lusid.models.currency_and_amount import CurrencyAndAmount

# TODO update the JSON string below
json = "{}"
# create an instance of CurrencyAndAmount from a JSON string
currency_and_amount_instance = CurrencyAndAmount.from_json(json)
# print the JSON string representation of the object
print CurrencyAndAmount.to_json()

# convert the object into a dict
currency_and_amount_dict = currency_and_amount_instance.to_dict()
# create an instance of CurrencyAndAmount from a dict
currency_and_amount_form_dict = currency_and_amount.from_dict(currency_and_amount_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


