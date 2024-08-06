# PagedResourceListOfCustodianAccount


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**next_page** | **str** |  | [optional] 
**previous_page** | **str** |  | [optional] 
**values** | [**List[CustodianAccount]**](CustodianAccount.md) |  | 
**href** | **str** |  | [optional] 
**links** | [**List[Link]**](Link.md) |  | [optional] 

## Example

```python
from lusid.models.paged_resource_list_of_custodian_account import PagedResourceListOfCustodianAccount

# TODO update the JSON string below
json = "{}"
# create an instance of PagedResourceListOfCustodianAccount from a JSON string
paged_resource_list_of_custodian_account_instance = PagedResourceListOfCustodianAccount.from_json(json)
# print the JSON string representation of the object
print PagedResourceListOfCustodianAccount.to_json()

# convert the object into a dict
paged_resource_list_of_custodian_account_dict = paged_resource_list_of_custodian_account_instance.to_dict()
# create an instance of PagedResourceListOfCustodianAccount from a dict
paged_resource_list_of_custodian_account_form_dict = paged_resource_list_of_custodian_account.from_dict(paged_resource_list_of_custodian_account_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


