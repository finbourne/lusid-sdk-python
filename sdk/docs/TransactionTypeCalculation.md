# TransactionTypeCalculation


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | The type of calculation to perform | 
**side** | **str** | The side to which the calculation is applied | [optional] 
**formula** | **str** | The formula used to derive the total consideration amount when it is not provided on the transaction | [optional] 

## Example

```python
from lusid.models.transaction_type_calculation import TransactionTypeCalculation

# TODO update the JSON string below
json = "{}"
# create an instance of TransactionTypeCalculation from a JSON string
transaction_type_calculation_instance = TransactionTypeCalculation.from_json(json)
# print the JSON string representation of the object
print TransactionTypeCalculation.to_json()

# convert the object into a dict
transaction_type_calculation_dict = transaction_type_calculation_instance.to_dict()
# create an instance of TransactionTypeCalculation from a dict
transaction_type_calculation_form_dict = transaction_type_calculation.from_dict(transaction_type_calculation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


