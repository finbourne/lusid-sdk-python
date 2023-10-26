# ResourceListOfTransaction


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**values** | [**List[Transaction]**](Transaction.md) |  | 
**href** | **str** |  | [optional] 
**links** | [**List[Link]**](Link.md) |  | [optional] 
**next_page** | **str** |  | [optional] 
**previous_page** | **str** |  | [optional] 

## Example

```python
from lusid.models.resource_list_of_transaction import ResourceListOfTransaction

# TODO update the JSON string below
json = "{}"
# create an instance of ResourceListOfTransaction from a JSON string
resource_list_of_transaction_instance = ResourceListOfTransaction.from_json(json)
# print the JSON string representation of the object
print ResourceListOfTransaction.to_json()

# convert the object into a dict
resource_list_of_transaction_dict = resource_list_of_transaction_instance.to_dict()
# create an instance of ResourceListOfTransaction from a dict
resource_list_of_transaction_form_dict = resource_list_of_transaction.from_dict(resource_list_of_transaction_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


