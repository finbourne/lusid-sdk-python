# TransactionType


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**aliases** | [**List[TransactionTypeAlias]**](TransactionTypeAlias.md) | List of transaction types that map to this specific transaction configuration | 
**movements** | [**List[TransactionTypeMovement]**](TransactionTypeMovement.md) | Movement data for the transaction type | 
**properties** | [**Dict[str, PerpetualProperty]**](PerpetualProperty.md) | Properties attached to the transaction type | [optional] 
**calculations** | [**List[TransactionTypeCalculation]**](TransactionTypeCalculation.md) | Calculations to be performed for the transaction type | [optional] 
**links** | [**List[Link]**](Link.md) |  | [optional] 

## Example

```python
from lusid.models.transaction_type import TransactionType

# TODO update the JSON string below
json = "{}"
# create an instance of TransactionType from a JSON string
transaction_type_instance = TransactionType.from_json(json)
# print the JSON string representation of the object
print TransactionType.to_json()

# convert the object into a dict
transaction_type_dict = transaction_type_instance.to_dict()
# create an instance of TransactionType from a dict
transaction_type_form_dict = transaction_type.from_dict(transaction_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


