# ResourceListOfOutputTransaction


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**values** | [**List[OutputTransaction]**](OutputTransaction.md) |  | 
**href** | **str** |  | [optional] 
**links** | [**List[Link]**](Link.md) |  | [optional] 
**next_page** | **str** |  | [optional] 
**previous_page** | **str** |  | [optional] 

## Example

```python
from lusid.models.resource_list_of_output_transaction import ResourceListOfOutputTransaction

# TODO update the JSON string below
json = "{}"
# create an instance of ResourceListOfOutputTransaction from a JSON string
resource_list_of_output_transaction_instance = ResourceListOfOutputTransaction.from_json(json)
# print the JSON string representation of the object
print ResourceListOfOutputTransaction.to_json()

# convert the object into a dict
resource_list_of_output_transaction_dict = resource_list_of_output_transaction_instance.to_dict()
# create an instance of ResourceListOfOutputTransaction from a dict
resource_list_of_output_transaction_form_dict = resource_list_of_output_transaction.from_dict(resource_list_of_output_transaction_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


