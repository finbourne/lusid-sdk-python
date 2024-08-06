# FeeTransactionTemplateSpecification


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**specification_type_name** | **str** |  | 
**supported_template_fields** | [**List[TemplateField]**](TemplateField.md) |  | 

## Example

```python
from lusid.models.fee_transaction_template_specification import FeeTransactionTemplateSpecification

# TODO update the JSON string below
json = "{}"
# create an instance of FeeTransactionTemplateSpecification from a JSON string
fee_transaction_template_specification_instance = FeeTransactionTemplateSpecification.from_json(json)
# print the JSON string representation of the object
print FeeTransactionTemplateSpecification.to_json()

# convert the object into a dict
fee_transaction_template_specification_dict = fee_transaction_template_specification_instance.to_dict()
# create an instance of FeeTransactionTemplateSpecification from a dict
fee_transaction_template_specification_form_dict = fee_transaction_template_specification.from_dict(fee_transaction_template_specification_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


