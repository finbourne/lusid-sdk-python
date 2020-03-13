# AdjustHoldingRequest

This request specifies target holdings. i.e. holding data that the  system should match. When processed by the movement  engine, it will create 'true-up' adjustments on the fly.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**instrument_identifiers** | **dict(str, str)** | A set of instrument identifiers to use to resolve the holding adjustment to a unique instrument. | 
**sub_holding_keys** | [**dict(str, PerpetualProperty)**](PerpetualProperty.md) | Set of unique transaction properties and associated values to store with the holding adjustment transaction automatically created by LUSID. Each property must be from the &#39;Transaction&#39; domain. | [optional] 
**properties** | [**dict(str, PerpetualProperty)**](PerpetualProperty.md) | Set of unique holding properties and associated values to store with the target holding. Each property must be from the &#39;Holding&#39; domain. | [optional] 
**tax_lots** | [**list[TargetTaxLotRequest]**](TargetTaxLotRequest.md) | The tax-lots that together make up the target holding. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


