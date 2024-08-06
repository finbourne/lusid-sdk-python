# VersionedResourceListOfOutputTransaction


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**version** | [**Version**](Version.md) |  | 
**values** | [**List[OutputTransaction]**](OutputTransaction.md) |  | 
**href** | **str** |  | [optional] 
**next_page** | **str** |  | [optional] 
**previous_page** | **str** |  | [optional] 
**links** | [**List[Link]**](Link.md) |  | [optional] 

## Example

```python
from lusid.models.versioned_resource_list_of_output_transaction import VersionedResourceListOfOutputTransaction

# TODO update the JSON string below
json = "{}"
# create an instance of VersionedResourceListOfOutputTransaction from a JSON string
versioned_resource_list_of_output_transaction_instance = VersionedResourceListOfOutputTransaction.from_json(json)
# print the JSON string representation of the object
print VersionedResourceListOfOutputTransaction.to_json()

# convert the object into a dict
versioned_resource_list_of_output_transaction_dict = versioned_resource_list_of_output_transaction_instance.to_dict()
# create an instance of VersionedResourceListOfOutputTransaction from a dict
versioned_resource_list_of_output_transaction_form_dict = versioned_resource_list_of_output_transaction.from_dict(versioned_resource_list_of_output_transaction_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


