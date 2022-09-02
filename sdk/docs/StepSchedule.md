# StepSchedule

Schedule that steps at known dated points in time.  Used in representation of a sinking bond, also called amortisation, steps in coupons for fixed bonds and spreads for floating bonds.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**level_type** | **str** | The type of shift or adjustment that the quantity represents.    Supported string (enumeration) values are: [Absolute, AbsoluteShift, Percentage, AbsolutePercentage]. | 
**schedule_type** | **str** | What type of schedule does this represent.  Supported string (enumeration) values are: [Fixed, Float, Optionality, Step, Payment, Accrual]. | 
**step_schedule_type** | **str** | The type of step that this schedule is for.  Supported string (enumeration) values are: [Coupon, Notional, Spread]. | 
**steps** | [**list[LevelStep]**](LevelStep.md) | The level steps which are applied. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


