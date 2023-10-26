# GeneralLedgerProfileResponse

A General Ledger Profile Definition.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**href** | **str** | The specific Uniform Resource Identifier (URI) for this resource at the requested effective and asAt datetime. | [optional] 
**chart_of_accounts_id** | [**ResourceId**](ResourceId.md) |  | 
**general_ledger_profile_code** | **str** | The unique code for the General Ledger Profile | 
**display_name** | **str** | The name of the General Ledger Profile | 
**description** | **str** | A description for the General Ledger Profile | [optional] 
**general_ledger_profile_mappings** | [**List[GeneralLedgerProfileMapping]**](GeneralLedgerProfileMapping.md) | Rules for mapping Account or property values to aggregation pattern definitions | 
**version** | [**Version**](Version.md) |  | [optional] 
**links** | [**List[Link]**](Link.md) |  | [optional] 

## Example

```python
from lusid.models.general_ledger_profile_response import GeneralLedgerProfileResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GeneralLedgerProfileResponse from a JSON string
general_ledger_profile_response_instance = GeneralLedgerProfileResponse.from_json(json)
# print the JSON string representation of the object
print GeneralLedgerProfileResponse.to_json()

# convert the object into a dict
general_ledger_profile_response_dict = general_ledger_profile_response_instance.to_dict()
# create an instance of GeneralLedgerProfileResponse from a dict
general_ledger_profile_response_form_dict = general_ledger_profile_response.from_dict(general_ledger_profile_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


