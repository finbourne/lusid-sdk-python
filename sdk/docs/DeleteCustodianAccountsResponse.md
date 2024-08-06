# DeleteCustodianAccountsResponse

The delete custodian accounts response

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**version** | [**Version**](Version.md) |  | [optional] 
**custodian_account_ids** | [**List[ResourceId]**](ResourceId.md) | The Custodian Accounts which have been soft/hard deleted. | [optional] 
**links** | [**List[Link]**](Link.md) |  | [optional] 

## Example

```python
from lusid.models.delete_custodian_accounts_response import DeleteCustodianAccountsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of DeleteCustodianAccountsResponse from a JSON string
delete_custodian_accounts_response_instance = DeleteCustodianAccountsResponse.from_json(json)
# print the JSON string representation of the object
print DeleteCustodianAccountsResponse.to_json()

# convert the object into a dict
delete_custodian_accounts_response_dict = delete_custodian_accounts_response_instance.to_dict()
# create an instance of DeleteCustodianAccountsResponse from a dict
delete_custodian_accounts_response_form_dict = delete_custodian_accounts_response.from_dict(delete_custodian_accounts_response_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


