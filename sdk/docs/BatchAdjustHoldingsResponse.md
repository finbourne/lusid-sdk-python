# BatchAdjustHoldingsResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**values** | [**dict(str, HoldingAdjustmentWithDate)**](HoldingAdjustmentWithDate.md) | The holdings which have been successfully adjusted. | [optional] 
**failed** | [**dict(str, ErrorDetail)**](ErrorDetail.md) | The holdings that could not be adjusted along with a reason for their failure. | [optional] 
**metadata** | **dict(str, list[ResponseMetaData])** | Contains warnings related to adjusted holdings | [optional] 
**links** | [**list[Link]**](Link.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


