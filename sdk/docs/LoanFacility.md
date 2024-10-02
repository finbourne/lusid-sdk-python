# LoanFacility

Loan Facility. This is a very lightweight instrument which acts as a placeholder for the events occurring within  the related facility Portfolio. This Portfolio is identified by its Scope and Code, which is recorded on the  instrument definition. The instrument acts as an agreement between a single borrower and many lenders (investors).  Several contracts may be drawn up to enable the lending of funds to the borrower. These contracts are modelled via  FlexibleLoan instruments in LUSID. The events occurring within the linked Portfolio may be related  to the facility as a whole (for example to define a global commitment amount), or they may relate to a single  contract (such as a paydown transaction on a particular contract).

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**start_date** | **datetime** | The start date of the instrument. This is normally synonymous with the trade-date. | 
**dom_ccy** | **str** | The domestic currency of the instrument. | 
**facility_portfolio_scope** | **str** | The Scope of the Transaction Portfolio to which the Loan Facility instrument is linked. | 
**facility_portfolio_code** | **str** | The Code of the Transaction Portfolio to which the Loan Facility instrument is linked. | 
**instrument_type** | **str** | The available values are: QuotedSecurity, InterestRateSwap, FxForward, Future, ExoticInstrument, FxOption, CreditDefaultSwap, InterestRateSwaption, Bond, EquityOption, FixedLeg, FloatingLeg, BespokeCashFlowsLeg, Unknown, TermDeposit, ContractForDifference, EquitySwap, CashPerpetual, CapFloor, CashSettled, CdsIndex, Basket, FundingLeg, FxSwap, ForwardRateAgreement, SimpleInstrument, Repo, Equity, ExchangeTradedOption, ReferenceInstrument, ComplexBond, InflationLinkedBond, InflationSwap, SimpleCashFlowLoan, TotalReturnSwap, InflationLeg, FundShareClass, FlexibleLoan, UnsettledCash, Cash, MasteredInstrument, LoanFacility | 

## Example

```python
from lusid.models.loan_facility import LoanFacility

# TODO update the JSON string below
json = "{}"
# create an instance of LoanFacility from a JSON string
loan_facility_instance = LoanFacility.from_json(json)
# print the JSON string representation of the object
print LoanFacility.to_json()

# convert the object into a dict
loan_facility_dict = loan_facility_instance.to_dict()
# create an instance of LoanFacility from a dict
loan_facility_form_dict = loan_facility.from_dict(loan_facility_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


