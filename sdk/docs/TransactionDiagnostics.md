# TransactionDiagnostics

Represents a set of diagnostics per transaction, where applicable.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**transaction_display_name** | **str** |  | 
**error_details** | **List[str]** |  | 

## Example

```python
from lusid.models.transaction_diagnostics import TransactionDiagnostics

# TODO update the JSON string below
json = "{}"
# create an instance of TransactionDiagnostics from a JSON string
transaction_diagnostics_instance = TransactionDiagnostics.from_json(json)
# print the JSON string representation of the object
print TransactionDiagnostics.to_json()

# convert the object into a dict
transaction_diagnostics_dict = transaction_diagnostics_instance.to_dict()
# create an instance of TransactionDiagnostics from a dict
transaction_diagnostics_form_dict = transaction_diagnostics.from_dict(transaction_diagnostics_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


