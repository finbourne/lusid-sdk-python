# LegDefinition

Definition of the set of flow and index conventions along with other miscellaneous information required to generate an instrument leg.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**convention_name** | [**FlowConventionName**](FlowConventionName.md) |  | [optional] 
**conventions** | [**FlowConventions**](FlowConventions.md) |  | [optional] 
**index_convention** | [**IndexConvention**](IndexConvention.md) |  | [optional] 
**index_convention_name** | [**FlowConventionName**](FlowConventionName.md) |  | [optional] 
**notional_exchange_type** | **str** | what type of notional exchange does the leg have    Supported string (enumeration) values are: [None, Initial, Final, Both]. | 
**pay_receive** | **str** | Is the leg to be paid or received    Supported string (enumeration) values are: [Pay, Receive]. | 
**rate_or_spread** | **float** | Is there either a fixed rate (non-zero) or spread to be paid over the value of the leg. | 
**reset_convention** | **str** | Control how resets are generated relative to swap payment convention(s).    Supported string (enumeration) values are: [InAdvance, InArrears]. | [optional] 
**stub_type** | **str** | If a stub is required should it be at the front or back of the leg.    Supported string (enumeration) values are: [None, ShortFront, ShortBack, LongBack, LongFront, Both]. | 
**compounding** | [**Compounding**](Compounding.md) |  | [optional] 
**amortisation** | [**StepSchedule**](StepSchedule.md) |  | [optional] 
**first_regular_payment_date** | **datetime** | Optional payment date of the first regular coupon.  Must be greater than the StartDate.  If set, the regular coupon schedule will be built such that the first regular coupon  will end on this date. The start date of this coupon will be calculated as normal and  a stub coupon will be created from the StartDate to the start of the first regular coupon. | [optional] 
**first_coupon_type** | **str** | Optional coupon type setting for the first coupon, can be used with Stub coupons.  If set to \&quot;ProRata\&quot; (the default), the coupon year fraction is calculated as normal,  however if set to \&quot;Full\&quot; the year fraction is overwritten with the standard year fraction  for a regular ful\&quot; coupon. Note this does not use the day count convention but rather is defined  directly from the tenor (i.e. a quarterly leg will be set to 0.25).    Supported string (enumeration) values are: [ProRata, Full]. | [optional] 
**last_regular_payment_date** | **datetime** | Optional payment date of the last regular coupon.  Must be less than the Maturity date.  If set, the regular coupon schedule will be built up to this date and the final  coupon will be a stub between this date and the Maturity date. | [optional] 
**last_coupon_type** | **str** | Optional coupon type setting for the last coupon, can be used with Stub coupons.  If set to \&quot;ProRata\&quot; (the default), the coupon year fraction is calculated as normal,  however if set to \&quot;Full\&quot; the year fraction is overwritten with the standard year fraction  for a regular ful\&quot; coupon. Note this does not use the day count convention but rather is defined  directly from the tenor (i.e. a quarterly leg will be set to 0.25).    Supported string (enumeration) values are: [ProRata, Full]. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


