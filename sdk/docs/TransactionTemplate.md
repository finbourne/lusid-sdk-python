# TransactionTemplate


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**instrument_type** | **str** | A value that represents the instrument type. | 
**instrument_event_type** | **str** | A value that represents the instrument event type. | 
**description** | **str** | The description of the transaction template. | 
**scope** | **str** | The scope in which the transaction template resides. | 
**component_transactions** | [**List[ComponentTransaction]**](ComponentTransaction.md) | A set of component transactions that relate to the template to be created. | 
**links** | [**List[Link]**](Link.md) |  | [optional] 

## Example

```python
from lusid.models.transaction_template import TransactionTemplate

# TODO update the JSON string below
json = "{}"
# create an instance of TransactionTemplate from a JSON string
transaction_template_instance = TransactionTemplate.from_json(json)
# print the JSON string representation of the object
print TransactionTemplate.to_json()

# convert the object into a dict
transaction_template_dict = transaction_template_instance.to_dict()
# create an instance of TransactionTemplate from a dict
transaction_template_form_dict = transaction_template.from_dict(transaction_template_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


