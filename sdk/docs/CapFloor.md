# CapFloor

LUSID representation of Cap, Floor, or Collar.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cap_floor_type** | **str** | Determine if it&#39;s CAP, FLOOR, or COLLAR.    Supported string (enumeration) values are: [Cap, Floor, Collar]. | 
**cap_strike** | **float** | Strike rate of the Cap. | [optional] 
**floor_strike** | **float** | Strike rate of the Floor. | [optional] 
**include_first_caplet** | **bool** | Include first caplet flag. | 
**underlying_floating_leg** | [**FloatingLeg**](FloatingLeg.md) |  | 
**additional_payments** | [**List[AdditionalPayment]**](AdditionalPayment.md) | Optional additional payments at a given date e.g. to level off an uneven equity swap.  The dates must be distinct and either all payments are Pay or all payments are Receive. | [optional] 
**instrument_type** | **str** | The available values are: QuotedSecurity, InterestRateSwap, FxForward, Future, ExoticInstrument, FxOption, CreditDefaultSwap, InterestRateSwaption, Bond, EquityOption, FixedLeg, FloatingLeg, BespokeCashFlowsLeg, Unknown, TermDeposit, ContractForDifference, EquitySwap, CashPerpetual, CapFloor, CashSettled, CdsIndex, Basket, FundingLeg, FxSwap, ForwardRateAgreement, SimpleInstrument, Repo, Equity, ExchangeTradedOption, ReferenceInstrument, ComplexBond, InflationLinkedBond, InflationSwap, SimpleCashFlowLoan, TotalReturnSwap, InflationLeg, FundShareClass, FlexibleLoan, UnsettledCash, Cash, MasteredInstrument, LoanFacility, FlexibleDeposit | 

## Example

```python
from lusid.models.cap_floor import CapFloor

# TODO update the JSON string below
json = "{}"
# create an instance of CapFloor from a JSON string
cap_floor_instance = CapFloor.from_json(json)
# print the JSON string representation of the object
print CapFloor.to_json()

# convert the object into a dict
cap_floor_dict = cap_floor_instance.to_dict()
# create an instance of CapFloor from a dict
cap_floor_form_dict = cap_floor.from_dict(cap_floor_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


