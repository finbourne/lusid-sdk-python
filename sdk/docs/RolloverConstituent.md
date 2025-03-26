# RolloverConstituent


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**contract_details** | [**ContractDetails**](ContractDetails.md) |  | 
**balance_change** | **float** | Balance of the new contract holding. | 

## Example

```python
from lusid.models.rollover_constituent import RolloverConstituent

# TODO update the JSON string below
json = "{}"
# create an instance of RolloverConstituent from a JSON string
rollover_constituent_instance = RolloverConstituent.from_json(json)
# print the JSON string representation of the object
print RolloverConstituent.to_json()

# convert the object into a dict
rollover_constituent_dict = rollover_constituent_instance.to_dict()
# create an instance of RolloverConstituent from a dict
rollover_constituent_form_dict = rollover_constituent.from_dict(rollover_constituent_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


