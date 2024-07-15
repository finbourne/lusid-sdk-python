# TransactionFieldMap


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**transaction_id** | **str** |  | 
**type** | **str** |  | 
**source** | **str** |  | 
**instrument** | **str** |  | 
**transaction_date** | **str** |  | 
**settlement_date** | **str** |  | 
**units** | **str** |  | 
**transaction_price** | [**TransactionPriceAndType**](TransactionPriceAndType.md) |  | 
**transaction_currency** | **str** |  | 
**exchange_rate** | **str** |  | [optional] 
**total_consideration** | [**TransactionCurrencyAndAmount**](TransactionCurrencyAndAmount.md) |  | 

## Example

```python
from lusid.models.transaction_field_map import TransactionFieldMap

# TODO update the JSON string below
json = "{}"
# create an instance of TransactionFieldMap from a JSON string
transaction_field_map_instance = TransactionFieldMap.from_json(json)
# print the JSON string representation of the object
print TransactionFieldMap.to_json()

# convert the object into a dict
transaction_field_map_dict = transaction_field_map_instance.to_dict()
# create an instance of TransactionFieldMap from a dict
transaction_field_map_form_dict = transaction_field_map.from_dict(transaction_field_map_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


