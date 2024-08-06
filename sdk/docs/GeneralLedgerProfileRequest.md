# GeneralLedgerProfileRequest

A General Ledger Profile Definition.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**general_ledger_profile_code** | **str** | The unique code for the General Ledger Profile | 
**display_name** | **str** | The name of the General Ledger Profile | 
**description** | **str** | A description for the General Ledger Profile | [optional] 
**general_ledger_profile_mappings** | [**List[GeneralLedgerProfileMapping]**](GeneralLedgerProfileMapping.md) | Rules for mapping Account or property values to aggregation pattern definitions | 

## Example

```python
from lusid.models.general_ledger_profile_request import GeneralLedgerProfileRequest

# TODO update the JSON string below
json = "{}"
# create an instance of GeneralLedgerProfileRequest from a JSON string
general_ledger_profile_request_instance = GeneralLedgerProfileRequest.from_json(json)
# print the JSON string representation of the object
print GeneralLedgerProfileRequest.to_json()

# convert the object into a dict
general_ledger_profile_request_dict = general_ledger_profile_request_instance.to_dict()
# create an instance of GeneralLedgerProfileRequest from a dict
general_ledger_profile_request_form_dict = general_ledger_profile_request.from_dict(general_ledger_profile_request_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


