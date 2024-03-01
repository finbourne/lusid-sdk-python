# FxOption

LUSID representation of an FX Option.  Including Vanilla, American, European, and Digital (Binary) options.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**start_date** | **datetime** | The start date of the instrument. This is normally synonymous with the trade-date. | 
**dom_ccy** | **str** | The domestic currency of the instrument. | 
**dom_amount** | **float** | The Amount of DomCcy that will be exchanged if the option is exercised.  This amount should be a positive number, with the Call/Put flag used to indicate direction.  The corresponding amount of FgnCcy that will be exchanged is this amount times the strike.  Note there is no rounding performed on this computed value.  This is an optional field, if not set the option ContractSize will default to 1. | [optional] 
**fgn_ccy** | **str** | The foreign currency of the FX. | 
**fgn_amount** | **float** | For a vanilla FxOption contract, FgnAmount cannot be set.  In case of a digital FxOption (IsPayoffDigital&#x3D;&#x3D;true)  a payoff (if the option is in the money) can be either  in domestic or in foreign currency - for the latter  FgnAmount must be set.  Note: It is invalid to have FgnAmount and DomAmount  at the same time. | [optional] 
**strike** | **float** | The strike of the option. | [optional] 
**barriers** | [**List[Barrier]**](Barrier.md) | For a barrier option the list should not be empty. Up to two barriers are supported.  An option cannot be at the same time barrier- and touch-option.  One (or both) of the lists must be empty. | [optional] 
**exercise_type** | **str** | Type of optionality that is present; European, American.    Supported string (enumeration) values are: [European, American]. | [optional] 
**is_call_not_put** | **bool** | True if the option is a call, false if the option is a put. | 
**is_delivery_not_cash** | **bool** | True if the option delivers the FX underlying, False if the option is settled in cash. | 
**is_payoff_digital** | **bool** | By default IsPayoffDigital is false. If IsPayoffDigital&#x3D;true,  the option is &#39;digital&#39;, and the option payoff is 0 or 1 unit of currency,  instead of a vanilla CallPayoff&#x3D;max(spot-strike,0) or PutPayoff&#x3D;max(strike-spot,0). | [optional] 
**option_maturity_date** | **datetime** | The maturity date of the option. | 
**option_settlement_date** | **datetime** | The settlement date of the option. | 
**payout_style** | **str** | PayoutStyle for touch options.                For options without touch optionality, payoutStyle should not be set.  For options with touch optionality (where the touches data has been set), payoutStyle must be defined and cannot be None.    Supported string (enumeration) values are: [Deferred, Immediate]. | [optional] 
**premium** | [**Premium**](Premium.md) |  | [optional] 
**touches** | [**List[Touch]**](Touch.md) | For a touch option the list should not be empty. Up to two touches are supported.  An option cannot be at the same time barrier- and touch-option.  One (or both) of the lists must be empty. | [optional] 
**instrument_type** | **str** | The available values are: QuotedSecurity, InterestRateSwap, FxForward, Future, ExoticInstrument, FxOption, CreditDefaultSwap, InterestRateSwaption, Bond, EquityOption, FixedLeg, FloatingLeg, BespokeCashFlowsLeg, Unknown, TermDeposit, ContractForDifference, EquitySwap, CashPerpetual, CapFloor, CashSettled, CdsIndex, Basket, FundingLeg, FxSwap, ForwardRateAgreement, SimpleInstrument, Repo, Equity, ExchangeTradedOption, ReferenceInstrument, ComplexBond, InflationLinkedBond, InflationSwap, SimpleCashFlowLoan, TotalReturnSwap, InflationLeg, FundShareClass, FlexibleLoan | 

## Example

```python
from lusid.models.fx_option import FxOption

# TODO update the JSON string below
json = "{}"
# create an instance of FxOption from a JSON string
fx_option_instance = FxOption.from_json(json)
# print the JSON string representation of the object
print FxOption.to_json()

# convert the object into a dict
fx_option_dict = fx_option_instance.to_dict()
# create an instance of FxOption from a dict
fx_option_form_dict = fx_option.from_dict(fx_option_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


