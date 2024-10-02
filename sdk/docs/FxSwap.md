# FxSwap

LUSID representation of an FX Swap. Composed of two FX Forwards.                This instrument has multiple legs, to see how legs are used in LUSID see [knowledge base article KA-02252](https://support.lusid.com/knowledgebase/article/KA-02252).                | Leg Index | Leg Identifier | Description |  | --------- | -------------- | ----------- |  | 1 | FarDomesticLeg | Cash flows in the domestic currency for the far forward. |  | 2 | FarForeignLeg | Cash flows in the foreign currency for the far forward (not present for non-deliverable forwards). |  | 3 | NearDomesticLeg | Cash flows in the domestic currency for the near forward. |  | 4 | NearForeignLeg | Cash flows in the foreign currency for the near forward (not present for non-deliverable forwards). |

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**near_fx_forward** | [**FxForward**](FxForward.md) |  | 
**far_fx_forward** | [**FxForward**](FxForward.md) |  | 
**notional_symmetry** | **str** | The NotionalSymmetry allows for even and uneven FxSwaps to be supported.  An even FxSwap is one where the near and far fx forwards have the same notional value on at least one of the  legs. An uneven FxSwap is one where near and far fx forwards don&#39;t have the same notional on both the  domestic and foreign legs.  By default NotionalSymmetry will be set as even.    Supported string (enumeration) values are: [Even, Uneven]. | [optional] 
**instrument_type** | **str** | The available values are: QuotedSecurity, InterestRateSwap, FxForward, Future, ExoticInstrument, FxOption, CreditDefaultSwap, InterestRateSwaption, Bond, EquityOption, FixedLeg, FloatingLeg, BespokeCashFlowsLeg, Unknown, TermDeposit, ContractForDifference, EquitySwap, CashPerpetual, CapFloor, CashSettled, CdsIndex, Basket, FundingLeg, FxSwap, ForwardRateAgreement, SimpleInstrument, Repo, Equity, ExchangeTradedOption, ReferenceInstrument, ComplexBond, InflationLinkedBond, InflationSwap, SimpleCashFlowLoan, TotalReturnSwap, InflationLeg, FundShareClass, FlexibleLoan, UnsettledCash, Cash, MasteredInstrument, LoanFacility | 

## Example

```python
from lusid.models.fx_swap import FxSwap

# TODO update the JSON string below
json = "{}"
# create an instance of FxSwap from a JSON string
fx_swap_instance = FxSwap.from_json(json)
# print the JSON string representation of the object
print FxSwap.to_json()

# convert the object into a dict
fx_swap_dict = fx_swap_instance.to_dict()
# create an instance of FxSwap from a dict
fx_swap_form_dict = fx_swap.from_dict(fx_swap_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


