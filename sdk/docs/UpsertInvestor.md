# UpsertInvestor

Inner dto of an Investor Record on the LUSID API

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**investor_type** | **str** | The type of the Investor | [optional] 
**investor_identifiers** | [**Dict[str, ModelProperty]**](ModelProperty.md) | The identifiers of the Investor | [optional] 

## Example

```python
from lusid.models.upsert_investor import UpsertInvestor

# TODO update the JSON string below
json = "{}"
# create an instance of UpsertInvestor from a JSON string
upsert_investor_instance = UpsertInvestor.from_json(json)
# print the JSON string representation of the object
print UpsertInvestor.to_json()

# convert the object into a dict
upsert_investor_dict = upsert_investor_instance.to_dict()
# create an instance of UpsertInvestor from a dict
upsert_investor_form_dict = upsert_investor.from_dict(upsert_investor_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


