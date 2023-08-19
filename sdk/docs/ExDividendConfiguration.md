# ExDividendConfiguration

Configure the ex-dividend periods for the instrument.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**use_business_days** | **bool** | Is the ex-dividend period counted in business days or calendar days.  Defaults to true if not set. | [optional] 
**ex_dividend_days** | **int** | Number of days in the ex-dividend period.  If the settlement date falls in the ex-dividend period then the coupon paid is zero and the accrued interest is negative.  If set, this must be a non-negative number.  If not set, or set to 0, than there is no ex-dividend period. | 
**return_negative_accrued** | **bool** | Does the accrued interest go negative in the ex-dividend period, or does it go to zero.  Defaults to true if not set. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


