# VersionedResourceListOfTransaction


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**version** | [**Version**](Version.md) |  | 
**values** | [**List[Transaction]**](Transaction.md) |  | 
**href** | **str** |  | [optional] 
**next_page** | **str** |  | [optional] 
**previous_page** | **str** |  | [optional] 
**links** | [**List[Link]**](Link.md) |  | [optional] 

## Example

```python
from lusid.models.versioned_resource_list_of_transaction import VersionedResourceListOfTransaction

# TODO update the JSON string below
json = "{}"
# create an instance of VersionedResourceListOfTransaction from a JSON string
versioned_resource_list_of_transaction_instance = VersionedResourceListOfTransaction.from_json(json)
# print the JSON string representation of the object
print VersionedResourceListOfTransaction.to_json()

# convert the object into a dict
versioned_resource_list_of_transaction_dict = versioned_resource_list_of_transaction_instance.to_dict()
# create an instance of VersionedResourceListOfTransaction from a dict
versioned_resource_list_of_transaction_form_dict = versioned_resource_list_of_transaction.from_dict(versioned_resource_list_of_transaction_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


