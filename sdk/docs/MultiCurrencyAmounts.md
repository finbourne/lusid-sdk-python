# MultiCurrencyAmounts


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**local_amount** | **float** |  | 
**base_amount** | **float** |  | 

## Example

```python
from lusid.models.multi_currency_amounts import MultiCurrencyAmounts

# TODO update the JSON string below
json = "{}"
# create an instance of MultiCurrencyAmounts from a JSON string
multi_currency_amounts_instance = MultiCurrencyAmounts.from_json(json)
# print the JSON string representation of the object
print MultiCurrencyAmounts.to_json()

# convert the object into a dict
multi_currency_amounts_dict = multi_currency_amounts_instance.to_dict()
# create an instance of MultiCurrencyAmounts from a dict
multi_currency_amounts_form_dict = multi_currency_amounts.from_dict(multi_currency_amounts_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


