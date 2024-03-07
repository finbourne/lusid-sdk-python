# PagedResourceListOfTransactionTemplate


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**next_page** | **str** |  | [optional] 
**previous_page** | **str** |  | [optional] 
**values** | [**List[TransactionTemplate]**](TransactionTemplate.md) |  | 
**href** | **str** |  | [optional] 
**links** | [**List[Link]**](Link.md) |  | [optional] 

## Example

```python
from lusid.models.paged_resource_list_of_transaction_template import PagedResourceListOfTransactionTemplate

# TODO update the JSON string below
json = "{}"
# create an instance of PagedResourceListOfTransactionTemplate from a JSON string
paged_resource_list_of_transaction_template_instance = PagedResourceListOfTransactionTemplate.from_json(json)
# print the JSON string representation of the object
print PagedResourceListOfTransactionTemplate.to_json()

# convert the object into a dict
paged_resource_list_of_transaction_template_dict = paged_resource_list_of_transaction_template_instance.to_dict()
# create an instance of PagedResourceListOfTransactionTemplate from a dict
paged_resource_list_of_transaction_template_form_dict = paged_resource_list_of_transaction_template.from_dict(paged_resource_list_of_transaction_template_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


