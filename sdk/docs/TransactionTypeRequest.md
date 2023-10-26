# TransactionTypeRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**aliases** | [**List[TransactionTypeAlias]**](TransactionTypeAlias.md) | List of transaction types that map to this specific transaction configuration | 
**movements** | [**List[TransactionTypeMovement]**](TransactionTypeMovement.md) | Movement data for the transaction type | 
**properties** | [**Dict[str, PerpetualProperty]**](PerpetualProperty.md) | Properties attached to the transaction type | [optional] 
**calculations** | [**List[TransactionTypeCalculation]**](TransactionTypeCalculation.md) | Calculations to be performed for the transaction type | [optional] 

## Example

```python
from lusid.models.transaction_type_request import TransactionTypeRequest

# TODO update the JSON string below
json = "{}"
# create an instance of TransactionTypeRequest from a JSON string
transaction_type_request_instance = TransactionTypeRequest.from_json(json)
# print the JSON string representation of the object
print TransactionTypeRequest.to_json()

# convert the object into a dict
transaction_type_request_dict = transaction_type_request_instance.to_dict()
# create an instance of TransactionTypeRequest from a dict
transaction_type_request_form_dict = transaction_type_request.from_dict(transaction_type_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


