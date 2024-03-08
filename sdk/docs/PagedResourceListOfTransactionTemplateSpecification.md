# PagedResourceListOfTransactionTemplateSpecification


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**next_page** | **str** |  | [optional] 
**previous_page** | **str** |  | [optional] 
**values** | [**List[TransactionTemplateSpecification]**](TransactionTemplateSpecification.md) |  | 
**href** | **str** |  | [optional] 
**links** | [**List[Link]**](Link.md) |  | [optional] 

## Example

```python
from lusid.models.paged_resource_list_of_transaction_template_specification import PagedResourceListOfTransactionTemplateSpecification

# TODO update the JSON string below
json = "{}"
# create an instance of PagedResourceListOfTransactionTemplateSpecification from a JSON string
paged_resource_list_of_transaction_template_specification_instance = PagedResourceListOfTransactionTemplateSpecification.from_json(json)
# print the JSON string representation of the object
print PagedResourceListOfTransactionTemplateSpecification.to_json()

# convert the object into a dict
paged_resource_list_of_transaction_template_specification_dict = paged_resource_list_of_transaction_template_specification_instance.to_dict()
# create an instance of PagedResourceListOfTransactionTemplateSpecification from a dict
paged_resource_list_of_transaction_template_specification_form_dict = paged_resource_list_of_transaction_template_specification.from_dict(paged_resource_list_of_transaction_template_specification_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


