# CdsFlowConventions


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**roll_frequency** | **str** | The frequency at which the reference bonds are updated, this defaults to 6M, but can be 3M, exp for historically issued products | [optional] 
**currency** | **str** | Currency of the flow convention. | 
**payment_frequency** | **str** | When generating a multiperiod flow, or when the maturity of the flow is not given but the start date is,  the tenor is the time-step from the anchor-date to the nominal maturity of the flow prior to any adjustment. | 
**day_count_convention** | **str** | when calculating the fraction of a year between two dates, what convention is used to represent the number of days in a year  and difference between them.  For more information on day counts, see [knowledge base article KA-01798](https://support.lusid.com/knowledgebase/article/KA-01798)                Supported string (enumeration) values are: [Actual360, Act360, MoneyMarket, Actual365, Act365, Thirty360, ThirtyU360, Bond, ThirtyE360, EuroBond, ActualActual, ActAct, ActActIsda, ActActIsma, ActActIcma, OneOne, Act364, Act365F, Act365L, Act365_25, Act252, Bus252, NL360, NL365, ActActAFB, Act365Cad, ThirtyActIsda, Thirty365Isda, ThirtyEActIsda, ThirtyE360Isda, ThirtyE365Isda, ThirtyU360EOM]. | 
**roll_convention** | **str** | When generating a set of dates, what convention should be used for adjusting dates that coincide with a non-business day.    Supported string (enumeration) values are: [NoAdjustment, None, Previous, P, Following, F, ModifiedPrevious, MP, ModifiedFollowing, MF, EndOfMonth, EOM, EndOfMonthPrevious, EOMP, EndOfMonthFollowing, EOMF, HalfMonthModifiedFollowing]. | 
**payment_calendars** | **list[str]** | An array of strings denoting holiday calendars that apply to generation of payment schedules. | 
**reset_calendars** | **list[str]** | An array of strings denoting holiday calendars that apply to generation of reset schedules. | 
**settle_days** | **int** | Number of Good Business Days between the trade date and the effective or settlement date of the instrument. | 
**reset_days** | **int** | The number of Good Business Days between determination and payment of reset. | 
**scope** | **str** | The scope used when updating or inserting the convention. | [optional] 
**code** | **str** | The code of the convention. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


