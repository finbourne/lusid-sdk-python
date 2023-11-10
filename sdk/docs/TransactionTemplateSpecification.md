# TransactionTemplateSpecification


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**instrument_event_type** | **str** |  | 
**supported_participation_types** | **List[str]** |  | 
**supported_election_types** | [**List[ElectionSpecification]**](ElectionSpecification.md) |  | 
**supported_template_fields** | [**List[TemplateField]**](TemplateField.md) |  | 

## Example

```python
from lusid.models.transaction_template_specification import TransactionTemplateSpecification

# TODO update the JSON string below
json = "{}"
# create an instance of TransactionTemplateSpecification from a JSON string
transaction_template_specification_instance = TransactionTemplateSpecification.from_json(json)
# print the JSON string representation of the object
print TransactionTemplateSpecification.to_json()

# convert the object into a dict
transaction_template_specification_dict = transaction_template_specification_instance.to_dict()
# create an instance of TransactionTemplateSpecification from a dict
transaction_template_specification_form_dict = transaction_template_specification.from_dict(transaction_template_specification_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


