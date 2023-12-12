# InflationSwap

LUSID representation of an Inflation Swap.  The implementation supports the following swap types:  * Zero Coupon inflation swap, with a single payment at maturity.  * LPI Swap (capped and floored)  * Year on Year inflation swap                This instrument has multiple legs, to see how legs are used in LUSID see https://support.lusid.com/knowledgebase/article/KA-02252.                | Leg Index | Leg Identifier | Description |  | --------- | -------------- | ----------- |  | 1 | InflationLeg | Cash flows with a rate relating to an underlying inflation index. |  | 2 | FixedLeg | Cash flows with a fixed rate. |

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**start_date** | **datetime** | The start date of the instrument. This is normally synonymous with the trade-date. | 
**maturity_date** | **datetime** | The final maturity date of the instrument. This means the last date on which the instruments makes a payment of any amount.  For the avoidance of doubt, that is not necessarily prior to its last sensitivity date for the purposes of risk; e.g. instruments such as  Constant Maturity Swaps (CMS) often have sensitivities to rates that may well be observed or set prior to the maturity date, but refer to a termination date beyond it. | 
**inflation_leg** | [**InflationLeg**](InflationLeg.md) |  | 
**fixed_leg** | [**FixedLeg**](FixedLeg.md) |  | 
**instrument_type** | **str** | The available values are: QuotedSecurity, InterestRateSwap, FxForward, Future, ExoticInstrument, FxOption, CreditDefaultSwap, InterestRateSwaption, Bond, EquityOption, FixedLeg, FloatingLeg, BespokeCashFlowsLeg, Unknown, TermDeposit, ContractForDifference, EquitySwap, CashPerpetual, CapFloor, CashSettled, CdsIndex, Basket, FundingLeg, FxSwap, ForwardRateAgreement, SimpleInstrument, Repo, Equity, ExchangeTradedOption, ReferenceInstrument, ComplexBond, InflationLinkedBond, InflationSwap, SimpleCashFlowLoan, TotalReturnSwap, InflationLeg | 

## Example

```python
from lusid.models.inflation_swap import InflationSwap

# TODO update the JSON string below
json = "{}"
# create an instance of InflationSwap from a JSON string
inflation_swap_instance = InflationSwap.from_json(json)
# print the JSON string representation of the object
print InflationSwap.to_json()

# convert the object into a dict
inflation_swap_dict = inflation_swap_instance.to_dict()
# create an instance of InflationSwap from a dict
inflation_swap_form_dict = inflation_swap.from_dict(inflation_swap_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


