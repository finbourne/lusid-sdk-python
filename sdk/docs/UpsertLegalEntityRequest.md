# UpsertLegalEntityRequest

Request to create or update an legal entity

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**identifiers** | [**Dict[str, ModelProperty]**](ModelProperty.md) | The identifiers the legal entity will be upserted with.The provided keys should be idTypeScope, idTypeCode, code | 
**properties** | [**Dict[str, ModelProperty]**](ModelProperty.md) | A set of properties associated to the Legal Entity. | [optional] 
**display_name** | **str** | The display name of the Legal Entity | 
**description** | **str** | The description of the Legal Entity | [optional] 
**counterparty_risk_information** | [**CounterpartyRiskInformation**](CounterpartyRiskInformation.md) |  | [optional] 

## Example

```python
from lusid.models.upsert_legal_entity_request import UpsertLegalEntityRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpsertLegalEntityRequest from a JSON string
upsert_legal_entity_request_instance = UpsertLegalEntityRequest.from_json(json)
# print the JSON string representation of the object
print UpsertLegalEntityRequest.to_json()

# convert the object into a dict
upsert_legal_entity_request_dict = upsert_legal_entity_request_instance.to_dict()
# create an instance of UpsertLegalEntityRequest from a dict
upsert_legal_entity_request_form_dict = upsert_legal_entity_request.from_dict(upsert_legal_entity_request_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


