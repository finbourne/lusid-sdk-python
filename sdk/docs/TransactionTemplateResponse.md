# TransactionTemplateResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**instrument_event_type** | **str** | A value that represents the instrument event type. | 
**description** | **str** | The description of the transaction template. | 
**scope** | **str** | The scope in which the transaction template resides. | 
**component_transactions** | [**List[ComponentTransaction]**](ComponentTransaction.md) | A set of component transactions that relate to the template to be created. | 
**links** | [**List[Link]**](Link.md) |  | [optional] 

## Example

```python
from lusid.models.transaction_template_response import TransactionTemplateResponse

# TODO update the JSON string below
json = "{}"
# create an instance of TransactionTemplateResponse from a JSON string
transaction_template_response_instance = TransactionTemplateResponse.from_json(json)
# print the JSON string representation of the object
print TransactionTemplateResponse.to_json()

# convert the object into a dict
transaction_template_response_dict = transaction_template_response_instance.to_dict()
# create an instance of TransactionTemplateResponse from a dict
transaction_template_response_form_dict = transaction_template_response.from_dict(transaction_template_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


