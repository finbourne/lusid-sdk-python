# UpsertLegalEntityRequest

Request to create or update an legal entity

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**identifiers** | [**dict(str, ModelProperty)**](ModelProperty.md) | The identifiers the legal entity will be upserted with.The provided keys should be idTypeScope, idTypeCode, code | 
**properties** | [**dict(str, ModelProperty)**](ModelProperty.md) | A set of properties associated to the Legal Entity. | [optional] 
**display_name** | **str** | The display name of the Legal Entity | 
**description** | **str** | The description of the Legal Entity | [optional] 
**counterparty_risk_information** | [**CounterpartyRiskInformation**](CounterpartyRiskInformation.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


