# PortfolioCashLadder


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**currency** | **str** | The currency of the cash-flows. | 
**sub_holding_keys** | [**dict(str, PerpetualProperty)**](PerpetualProperty.md) | The sub-holding properties which identify the holding. Each property will be from the &#39;Transaction&#39; domain. These are configured on a transaction portfolio. | [optional] 
**records** | [**list[CashLadderRecord]**](CashLadderRecord.md) | A record of cash flows on a specific date. | 
**failed** | [**dict(str, ErrorDetail)**](ErrorDetail.md) | The records that could not be returned along with a reason for their failure. | [optional] 
**links** | [**list[Link]**](Link.md) | Collection of links. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


