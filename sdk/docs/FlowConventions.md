# FlowConventions

A flow convention defines the specification for generation of the date schedule for a leg or set of cashflows.  It determines the tenor of these and, how to map the unadjusted set of dates to dates which are 'good business  days'. For example, if an unadjusted date falls on a Saturday or a bank holiday, should it be rolled forward  or backward to obtain the adjusted date.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**currency** | **str** | Currency of the flow convention. | 
**payment_frequency** | [**Tenor**](Tenor.md) |  | 
**day_count_convention** | **str** | when calculating the fraction of a year between two dates, what convention is used to represent the number of days in a year  and difference between them. | 
**roll_convention** | **str** | when generating a set of dates, what convention should be used for adjusting dates that coincide with a non-business day. | 
**holiday_calendars** | **list[str]** | An array of strings denoting holiday calendars that apply to generation and payment. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


