# CapFloorAllOf


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cap_floor_type** | **str** | Determine if it&#39;s CAP, FLOOR, or COLLAR.    Supported string (enumeration) values are: [Cap, Floor, Collar]. | 
**cap_strike** | **float** | Strike rate of the Cap. | 
**floor_strike** | **float** | Strike rate of the Floor. | 
**include_first_caplet** | **bool** | Include first caplet flag. | 
**underlying_floating_leg** | [**FloatingLeg**](FloatingLeg.md) |  | 
**instrument_type** | **str** | The available values are: QuotedSecurity, InterestRateSwap, FxForward, Future, ExoticInstrument, FxOption, CreditDefaultSwap, InterestRateSwaption, Bond, EquityOption, FixedLeg, FloatingLeg, BespokeCashFlowsLeg, Unknown, TermDeposit, ContractForDifference, EquitySwap, CashPerpetual, CapFloor, CashSettled, CdsIndex, Basket, FundingLeg, FxSwap, ForwardRateAgreement, SimpleInstrument, Repo, Equity, ExchangeTradedOption, ReferenceInstrument, ComplexBond, InflationLinkedBond, InflationSwap, SimpleCashFlowLoan | 

## Example

```python
from lusid.models.cap_floor_all_of import CapFloorAllOf

# TODO update the JSON string below
json = "{}"
# create an instance of CapFloorAllOf from a JSON string
cap_floor_all_of_instance = CapFloorAllOf.from_json(json)
# print the JSON string representation of the object
print CapFloorAllOf.to_json()

# convert the object into a dict
cap_floor_all_of_dict = cap_floor_all_of_instance.to_dict()
# create an instance of CapFloorAllOf from a dict
cap_floor_all_of_form_dict = cap_floor_all_of.from_dict(cap_floor_all_of_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


