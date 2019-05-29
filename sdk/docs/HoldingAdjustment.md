# HoldingAdjustment

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**instrument_identifiers** | **dict(str, str)** | Unique instrument identifiers | [optional] 
**instrument_uid** | **str** | LUSID&#39;s internal unique instrument identifier, resolved from the instrument identifiers | 
**sub_holding_keys** | [**list[PerpetualProperty]**](PerpetualProperty.md) | Key fields to uniquely index the sub holdings of a instrument | [optional] 
**properties** | [**list[PerpetualProperty]**](PerpetualProperty.md) | Arbitrary properties to store with the holding | [optional] 
**tax_lots** | [**list[TargetTaxLot]**](TargetTaxLot.md) | 1 or more quantity amounts | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


