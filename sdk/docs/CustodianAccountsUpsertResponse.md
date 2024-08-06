# CustodianAccountsUpsertResponse

The upsert accounts response

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**href** | **str** | The specific Uniform Resource Identifier (URI) for this resource at the requested effective and asAt datetime. | [optional] 
**version** | [**Version**](Version.md) |  | [optional] 
**custodian_accounts** | [**List[CustodianAccount]**](CustodianAccount.md) | The Custodian Accounts which have been upserted. | [optional] 
**links** | [**List[Link]**](Link.md) |  | [optional] 

## Example

```python
from lusid.models.custodian_accounts_upsert_response import CustodianAccountsUpsertResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CustodianAccountsUpsertResponse from a JSON string
custodian_accounts_upsert_response_instance = CustodianAccountsUpsertResponse.from_json(json)
# print the JSON string representation of the object
print CustodianAccountsUpsertResponse.to_json()

# convert the object into a dict
custodian_accounts_upsert_response_dict = custodian_accounts_upsert_response_instance.to_dict()
# create an instance of CustodianAccountsUpsertResponse from a dict
custodian_accounts_upsert_response_form_dict = custodian_accounts_upsert_response.from_dict(custodian_accounts_upsert_response_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


