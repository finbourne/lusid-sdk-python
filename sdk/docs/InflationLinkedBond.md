# InflationLinkedBond

Inflation Linked Bond.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**start_date** | **datetime** | The start date of the bond. | 
**maturity_date** | **datetime** | The final maturity date of the instrument. This means the last date on which the instruments makes a payment of any amount.  For the avoidance of doubt, that is not necessarily prior to its last sensitivity date for the purposes of risk; e.g. instruments such as  Constant Maturity Swaps (CMS) often have sensitivities to rates that may well be observed or set prior to the maturity date, but refer to a termination date beyond it. | 
**flow_conventions** | [**FlowConventions**](FlowConventions.md) |  | 
**coupon_rate** | **float** | Simple coupon rate. | 
**identifiers** | **dict(str, str)** | External market codes and identifiers for the bond, e.g. ISIN. | [optional] 
**dom_ccy** | **str** | The domestic currency of the instrument. | 
**base_cpi** | **float** | BaseCPI value. This is optional, if not provided the BaseCPI value will be calculated from the BaseCPIDate,  If that too is not present the StartDate will be used.  Note that both BaseCPI and BaseCPIDate cannot be set.  Some bonds are issued with a BaseCPI date that does not correspond to the StartDate CPI value, in this  case the value should be provided here or with the BaseCPIDate. | [optional] 
**base_cpi_date** | **datetime** | BaseCPIDate. This is optional, if not provided the BaseCPI value will taken from the BaseCPI property,  if that too is not present than the StartDate will be used.  If present, the BaseCPI is calculated for this date, note this is an un-lagged date (similar to StartDate)  so the Bond ObservationLag will be applied to this date when calculating the CPI.  Note that both BaseCPI and BaseCPIDate cannot be set.  Some bonds are issued with a BaseCPI date that does not correspond to the StartDate CPI value, in this  case the value should be provided here or with the actual BaseCPI. | [optional] 
**calculation_type** | **str** | The calculation type applied to the bond coupon and principal amount.  The default CalculationType is &#x60;Standard&#x60; and currently this is the only value supported.    Supported string (enumeration) values are: [Standard, Quarterly, Ratio]. | [optional] 
**ex_dividend_days** | **int** | Number of Good Business Days before the next coupon payment, in which the bond goes ex-dividend.  This is not common in inflation linked bonds but has been seen with (for example) bonds issued by  the Bank of Thailand. | [optional] 
**index_precision** | **int** | Number of decimal places used to round IndexRatio. This defaults to 5 if not set. | [optional] 
**inflation_index_name** | **str** | Name of the index, e.g. UKRPI. | 
**inflation_interpolation** | **str** | Inflation Interpolation. This is optional and defaults to Linear if not set.    Supported string (enumeration) values are: [Linear, Flat]. | [optional] 
**inflation_roll_day** | **int** | Day of the month that inflation rolls from one month to the next. This is optional and defaults to 1, which is  the typically value for the majority of inflation bonds (exceptions include Japan which rolls on the 10th  and some LatAm bonds which roll on the 15th). | [optional] 
**observation_lag** | **str** | Observation lag. This is a Tenor that must have units of Month.  This field is typically 3 or 4 months, but can vary, older bonds have 8 months lag.  For Bonds with a calculation type of Ratio, this property, if set, must be 0Invalid. | [optional] 
**principal** | **float** | The face-value or principal for the bond at outset. | 
**principal_protection** | **bool** | If true then the principal is protected in that the redemption amount will be at least the face value (Principal).  This is typically set to true for inflation linked bonds issued by the United States and France (for example).  This is typically set to false for inflation linked bonds issued by the United Kingdom (post 2005).  For other sovereigns this can vary from issue to issue.  If not set this property defaults to true.  This is sometimes referred to as Deflation protection or an inflation floor of 0%. | [optional] 
**stub_type** | **str** | StubType. Most Inflation linked bonds have a ShortFront stub type so this is the default, however in some cases  with a long front stub LongFront should be selected.  StubType Both is not supported for InflationLinkedBonds.    Supported string (enumeration) values are: [ShortFront, ShortBack, LongBack, LongFront, Both]. | [optional] 
**instrument_type** | **str** | The available values are: QuotedSecurity, InterestRateSwap, FxForward, Future, ExoticInstrument, FxOption, CreditDefaultSwap, InterestRateSwaption, Bond, EquityOption, FixedLeg, FloatingLeg, BespokeCashFlowsLeg, Unknown, TermDeposit, ContractForDifference, EquitySwap, CashPerpetual, CapFloor, CashSettled, CdsIndex, Basket, FundingLeg, FxSwap, ForwardRateAgreement, SimpleInstrument, Repo, Equity, ExchangeTradedOption, ReferenceInstrument, ComplexBond, InflationLinkedBond | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


