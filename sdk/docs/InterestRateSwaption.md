# InterestRateSwaption

LUSID representation of an Interest Rate Swaption.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**start_date** | **datetime** | The start date of the instrument. This is normally synonymous with the trade-date. | 
**pay_or_receive_fixed** | **str** | True if on exercise the holder of the option enters the swap paying fixed, false if floating.    Supported string (enumeration) values are: [Pay, Receive]. | 
**premium** | [**Premium**](Premium.md) |  | [optional] 
**delivery_method** | **str** | How does the option settle    Supported string (enumeration) values are: [Cash, Physical]. | 
**swap** | [**InterestRateSwap**](InterestRateSwap.md) |  | 
**instrument_type** | **str** | The available values are: QuotedSecurity, InterestRateSwap, FxForward, Future, ExoticInstrument, FxOption, CreditDefaultSwap, InterestRateSwaption, Bond, EquityOption, FixedLeg, FloatingLeg, BespokeCashFlowsLeg, Unknown, TermDeposit, ContractForDifference, EquitySwap, CashPerpetual, CapFloor, CashSettled, CdsIndex, Basket, FundingLeg, FxSwap, ForwardRateAgreement, SimpleInstrument, Repo, Equity, ExchangeTradedOption, ReferenceInstrument, ComplexBond, InflationLinkedBond, InflationSwap, SimpleCashFlowLoan, TotalReturnSwap, InflationLeg, FundShareClass, FlexibleLoan, UnsettledCash, Cash, MasteredInstrument, LoanFacility | 

## Example

```python
from lusid.models.interest_rate_swaption import InterestRateSwaption

# TODO update the JSON string below
json = "{}"
# create an instance of InterestRateSwaption from a JSON string
interest_rate_swaption_instance = InterestRateSwaption.from_json(json)
# print the JSON string representation of the object
print InterestRateSwaption.to_json()

# convert the object into a dict
interest_rate_swaption_dict = interest_rate_swaption_instance.to_dict()
# create an instance of InterestRateSwaption from a dict
interest_rate_swaption_form_dict = interest_rate_swaption.from_dict(interest_rate_swaption_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


