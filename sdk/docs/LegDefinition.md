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

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


