# FundingLeg

LUSID representation of a Funding Leg with variable notional.    This Funding Leg is a hybrid between a single leg swap and a loan facility; the notional is not fixed and can vary within a reset period.                 The model can be used to represent the funding leg of a basket of instruments (e.g. equities) where the contents  of the basket can change over time. The actual notional history is stored in the FundingLegHistory object.     The actual notional history is stored in the FundingLegHistory object.                The main analytic calculated for this instrument is Accrual rather than PV.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**start_date** | **datetime** | The start date of the instrument. This is normally synonymous with the trade-date. | 
**maturity_date** | **datetime** | The final maturity date of the instrument. This means the last date on which the instruments makes a payment of any amount.  For the avoidance of doubt, that is not necessarily prior to its last sensitivity date for the purposes of risk; e.g. instruments such as  Constant Maturity Swaps (CMS) often have sensitivities to rates beyond their last payment date. | 
**leg_definition** | [**LegDefinition**](LegDefinition.md) |  | 
**notional** | **float** | The initial notional of the Funding Leg instrument.  When \&quot;RequiresFundingLegHistory\&quot; property key is present in transaction key, during a GetValuation endpoint call (for instance),  this field would overriden by the Funding Leg history&#39;s notional and this notional field would not be used in the pricing and accrual calculations.  As such, we recommend setting this to 0 or not setting it at all.  Please see the following Notebook example and Knowledge Base article:  Notebook: https://github.com/finbourne/sample-notebooks/blob/master/examples/use-cases/instruments/Funding%20Leg%20Swap.ipynb  Knowledge Base article: https://support.lusid.com/knowledgebase/article/KA-01764/ | [optional] 
**instrument_type** | **str** | The available values are: QuotedSecurity, InterestRateSwap, FxForward, Future, ExoticInstrument, FxOption, CreditDefaultSwap, InterestRateSwaption, Bond, EquityOption, FixedLeg, FloatingLeg, BespokeCashFlowsLeg, Unknown, TermDeposit, ContractForDifference, EquitySwap, CashPerpetual, CapFloor, CashSettled, CdsIndex, Basket, FundingLeg, FxSwap, ForwardRateAgreement, SimpleInstrument, Repo, Equity, ExchangeTradedOption, ReferenceInstrument, ComplexBond, InflationLinkedBond, InflationSwap, SimpleCashFlowLoan, TotalReturnSwap, InflationLeg, FundShareClass, FlexibleLoan, UnsettledCash, Cash | 

## Example

```python
from lusid.models.funding_leg import FundingLeg

# TODO update the JSON string below
json = "{}"
# create an instance of FundingLeg from a JSON string
funding_leg_instance = FundingLeg.from_json(json)
# print the JSON string representation of the object
print FundingLeg.to_json()

# convert the object into a dict
funding_leg_dict = funding_leg_instance.to_dict()
# create an instance of FundingLeg from a dict
funding_leg_form_dict = funding_leg.from_dict(funding_leg_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


