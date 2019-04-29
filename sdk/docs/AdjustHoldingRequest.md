# AdjustHoldingRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**instrument_identifiers** | **dict(str, str)** | Unique instrument identifiers. | 
**sub_holding_keys** | [**dict(str, PerpetualPropertyValue)**](PerpetualPropertyValue.md) | Key fields to uniquely index the sub holdings of a instrument | [optional] 
**properties** | [**dict(str, PerpetualPropertyValue)**](PerpetualPropertyValue.md) | Arbitrary properties to store with the holding | [optional] 
**tax_lots** | [**list[TargetTaxLotRequest]**](TargetTaxLotRequest.md) | 1 or more quantity amounts | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


