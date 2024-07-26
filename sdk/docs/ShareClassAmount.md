# ShareClassAmount


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**MultiCurrencyAmounts**](MultiCurrencyAmounts.md) |  | [optional] 

## Example

```python
from lusid.models.share_class_amount import ShareClassAmount

# TODO update the JSON string below
json = "{}"
# create an instance of ShareClassAmount from a JSON string
share_class_amount_instance = ShareClassAmount.from_json(json)
# print the JSON string representation of the object
print ShareClassAmount.to_json()

# convert the object into a dict
share_class_amount_dict = share_class_amount_instance.to_dict()
# create an instance of ShareClassAmount from a dict
share_class_amount_form_dict = share_class_amount.from_dict(share_class_amount_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


