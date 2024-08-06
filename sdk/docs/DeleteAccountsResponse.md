# DeleteAccountsResponse

The delete accounts response

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**version** | [**Version**](Version.md) |  | [optional] 
**account_ids** | **List[str]** | The Accounts which have been soft/hard deleted. | [optional] 
**links** | [**List[Link]**](Link.md) |  | [optional] 

## Example

```python
from lusid.models.delete_accounts_response import DeleteAccountsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of DeleteAccountsResponse from a JSON string
delete_accounts_response_instance = DeleteAccountsResponse.from_json(json)
# print the JSON string representation of the object
print DeleteAccountsResponse.to_json()

# convert the object into a dict
delete_accounts_response_dict = delete_accounts_response_instance.to_dict()
# create an instance of DeleteAccountsResponse from a dict
delete_accounts_response_form_dict = delete_accounts_response.from_dict(delete_accounts_response_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


