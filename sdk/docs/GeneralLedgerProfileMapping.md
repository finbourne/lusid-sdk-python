# GeneralLedgerProfileMapping


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**mapping_filter** | **str** | The filter syntax for the Mapping filter. See https://support.lusid.com/knowledgebase/article/KA-02140 for more information on filter syntax | 
**levels** | **List[str]** | References fields and properties on the associated Journal Entry Line and graph of associated objects. | 

## Example

```python
from lusid.models.general_ledger_profile_mapping import GeneralLedgerProfileMapping

# TODO update the JSON string below
json = "{}"
# create an instance of GeneralLedgerProfileMapping from a JSON string
general_ledger_profile_mapping_instance = GeneralLedgerProfileMapping.from_json(json)
# print the JSON string representation of the object
print GeneralLedgerProfileMapping.to_json()

# convert the object into a dict
general_ledger_profile_mapping_dict = general_ledger_profile_mapping_instance.to_dict()
# create an instance of GeneralLedgerProfileMapping from a dict
general_ledger_profile_mapping_form_dict = general_ledger_profile_mapping.from_dict(general_ledger_profile_mapping_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


