# CashFlowLineage

Lineage for cash flow value

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**instrument_type** | **str** | The instrument type of the instrument to which the cash flow belongs to. When upserting CashFlowValues, this  should be null. | [optional] 
**cash_flow_type** | **str** | The cashflow type.When upserting CashFlowValues, this should be null, or one of [Unknown, Coupon, Notional,  Premium, Principal, Protection, Cash] | [optional] 
**instrument_id** | **str** | The LUID of the instrument to which the cash flow belongs to. When upserting this should be null. | [optional] 
**leg_id** | **str** | The leg id to which the cash flow belongs to. | [optional] 
**source_transaction_id** | **str** | The source transaction of the instrument to which the cash flow belongs to. When upserting this should be null | [optional] 
**pay_receive** | **str** | Does the cash flow belong to the Pay or Receive leg. When upserting this should either be null or one of [Pay, Receive, NotApplicable] | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


