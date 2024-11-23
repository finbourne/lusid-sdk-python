# ContractDetails

Set of identifiers of an existing FlexibleLoan contract.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**identifiers** | **Dict[str, str]** | Unique instrument identifiers. | 
**lusid_instrument_id** | **str** | LUSID&#39;s internal unique instrument identifier - readonly field, resolved from the instrument identifiers. | [optional] [readonly] 
**instrument_scope** | **str** | The scope in which the FlexibleLoan instrument lies - readonly field, resolved from the instrument identifiers. | [optional] [readonly] 
**instrument_name** | **str** | The name of the FlexibleLoan instrument - readonly field, resolved from the instrument identifiers. | [optional] [readonly] 
**dom_ccy** | **str** | The domestic currency of the instrument - readonly field, resolved from the instrument identifiers. | [optional] [readonly] 

## Example

```python
from lusid.models.contract_details import ContractDetails

# TODO update the JSON string below
json = "{}"
# create an instance of ContractDetails from a JSON string
contract_details_instance = ContractDetails.from_json(json)
# print the JSON string representation of the object
print ContractDetails.to_json()

# convert the object into a dict
contract_details_dict = contract_details_instance.to_dict()
# create an instance of ContractDetails from a dict
contract_details_form_dict = contract_details.from_dict(contract_details_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


