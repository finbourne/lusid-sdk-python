# EquityOption

LUSID representation of a plain vanilla OTC Equity Option.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**start_date** | **datetime** | The start date of the instrument. This is normally synonymous with the trade-date. | 
**option_maturity_date** | **datetime** | The maturity date of the option. | 
**option_settlement_date** | **datetime** | The settlement date of the option. | [optional] 
**delivery_type** | **str** | Is the option cash settled or physical delivery of option    Supported string (enumeration) values are: [Cash, Physical]. | 
**option_type** | **str** | Type of optionality for the option    Supported string (enumeration) values are: [Call, Put]. | 
**strike** | **float** | The strike of the option. | 
**dom_ccy** | **str** | The domestic currency of the instrument. | 
**underlying_identifier** | **str** | The market identifier type of the underlying code, e.g RIC.    Supported string (enumeration) values are: [LusidInstrumentId, Isin, Sedol, Cusip, ClientInternal, Figi, RIC, QuotePermId, REDCode, BBGId, ICECode].  Optional field, should be used in combination with the Code field.  Not compatible with the Underlying field. | [optional] 
**code** | **str** | The identifying code for the equity underlying, e.g. &#39;IBM.N&#39;.  Optional field, should be used in combination with the UnderlyingIdentifier field.  Not compatible with the Underlying field. | [optional] 
**equity_option_type** | **str** | Equity option types. E.g. Vanilla (default), RightsIssue, Warrant.    Supported string (enumeration) values are: [Vanilla, RightsIssue, Warrant]. | [optional] 
**number_of_shares** | **float** | The amount of shares to exchange if the option is exercised. | [optional] 
**premium** | [**Premium**](Premium.md) |  | [optional] 
**exercise_type** | **str** | Type of optionality that is present; European, American.    Supported string (enumeration) values are: [European, American]. | [optional] 
**underlying** | [**LusidInstrument**](LusidInstrument.md) |  | [optional] 
**delivery_days** | **int** | Number of business days between exercise date and settlement of the option payoff or underlying. | [optional] 
**business_day_convention** | **str** | Business day convention for option exercise date to settlement date calculation.  Supported string (enumeration) values are: [NoAdjustment, Previous, P, Following, F, ModifiedPrevious, MP, ModifiedFollowing, MF, HalfMonthModifiedFollowing, Nearest]. | [optional] 
**settlement_calendars** | **List[str]** | Holiday calendars for option exercise date to settlement date calculation. | [optional] 
**instrument_type** | **str** | The available values are: QuotedSecurity, InterestRateSwap, FxForward, Future, ExoticInstrument, FxOption, CreditDefaultSwap, InterestRateSwaption, Bond, EquityOption, FixedLeg, FloatingLeg, BespokeCashFlowsLeg, Unknown, TermDeposit, ContractForDifference, EquitySwap, CashPerpetual, CapFloor, CashSettled, CdsIndex, Basket, FundingLeg, FxSwap, ForwardRateAgreement, SimpleInstrument, Repo, Equity, ExchangeTradedOption, ReferenceInstrument, ComplexBond, InflationLinkedBond, InflationSwap, SimpleCashFlowLoan, TotalReturnSwap, InflationLeg, FundShareClass, FlexibleLoan, UnsettledCash, Cash, MasteredInstrument, LoanFacility, FlexibleDeposit | 

## Example

```python
from lusid.models.equity_option import EquityOption

# TODO update the JSON string below
json = "{}"
# create an instance of EquityOption from a JSON string
equity_option_instance = EquityOption.from_json(json)
# print the JSON string representation of the object
print EquityOption.to_json()

# convert the object into a dict
equity_option_dict = equity_option_instance.to_dict()
# create an instance of EquityOption from a dict
equity_option_form_dict = equity_option.from_dict(equity_option_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


