# AccountsUpsertResponse

The upsert accounts response

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**href** | **str** | The specific Uniform Resource Identifier (URI) for this resource at the requested effective and asAt datetime. | [optional] 
**version** | [**Version**](Version.md) |  | [optional] 
**accounts** | [**List[Account]**](Account.md) | The Accounts which have been upserted. | [optional] 
**links** | [**List[Link]**](Link.md) |  | [optional] 

## Example

```python
from lusid.models.accounts_upsert_response import AccountsUpsertResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AccountsUpsertResponse from a JSON string
accounts_upsert_response_instance = AccountsUpsertResponse.from_json(json)
# print the JSON string representation of the object
print AccountsUpsertResponse.to_json()

# convert the object into a dict
accounts_upsert_response_dict = accounts_upsert_response_instance.to_dict()
# create an instance of AccountsUpsertResponse from a dict
accounts_upsert_response_form_dict = accounts_upsert_response.from_dict(accounts_upsert_response_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


