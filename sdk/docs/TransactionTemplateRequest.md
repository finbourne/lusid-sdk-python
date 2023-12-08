# TransactionTemplateRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** | The description of the transaction template. | 
**component_transactions** | [**List[ComponentTransaction]**](ComponentTransaction.md) | A set of component transactions that relate to the template to be created. | 

## Example

```python
from lusid.models.transaction_template_request import TransactionTemplateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of TransactionTemplateRequest from a JSON string
transaction_template_request_instance = TransactionTemplateRequest.from_json(json)
# print the JSON string representation of the object
print TransactionTemplateRequest.to_json()

# convert the object into a dict
transaction_template_request_dict = transaction_template_request_instance.to_dict()
# create an instance of TransactionTemplateRequest from a dict
transaction_template_request_form_dict = transaction_template_request.from_dict(transaction_template_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


