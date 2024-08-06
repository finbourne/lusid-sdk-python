# PagedResourceListOfGeneralLedgerProfileResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**next_page** | **str** |  | [optional] 
**previous_page** | **str** |  | [optional] 
**values** | [**List[GeneralLedgerProfileResponse]**](GeneralLedgerProfileResponse.md) |  | 
**href** | **str** |  | [optional] 
**links** | [**List[Link]**](Link.md) |  | [optional] 

## Example

```python
from lusid.models.paged_resource_list_of_general_ledger_profile_response import PagedResourceListOfGeneralLedgerProfileResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PagedResourceListOfGeneralLedgerProfileResponse from a JSON string
paged_resource_list_of_general_ledger_profile_response_instance = PagedResourceListOfGeneralLedgerProfileResponse.from_json(json)
# print the JSON string representation of the object
print PagedResourceListOfGeneralLedgerProfileResponse.to_json()

# convert the object into a dict
paged_resource_list_of_general_ledger_profile_response_dict = paged_resource_list_of_general_ledger_profile_response_instance.to_dict()
# create an instance of PagedResourceListOfGeneralLedgerProfileResponse from a dict
paged_resource_list_of_general_ledger_profile_response_form_dict = paged_resource_list_of_general_ledger_profile_response.from_dict(paged_resource_list_of_general_ledger_profile_response_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


