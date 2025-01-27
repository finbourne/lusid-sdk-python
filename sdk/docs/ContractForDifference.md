# ContractForDifference

LUSID representation of a Contract for Difference.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**start_date** | **datetime** | The start date of the CFD. | 
**maturity_date** | **datetime** | The maturity date for the CFD. If CFDType is Futures, this should be set to be the maturity date of the underlying  future. If CFDType is Cash, this should not be set. | [optional] 
**code** | **str** | The code of the underlying. | [optional] 
**contract_size** | **float** | The size of the CFD contract, this should represent the total number of stocks that the CFD represents.   This field is optional, if not set it will default to 1. | [optional] 
**pay_ccy** | **str** | The currency that this CFD pays out, this can be different to the UnderlyingCcy. | 
**reference_rate** | **float** | The reference rate of the CFD, this can be set to 0 but not negative values.  This field is optional, if not set it will default to 0. | [optional] 
**type** | **str** | The type of CFD.    Supported string (enumeration) values are: [Cash, Futures]. | 
**underlying_ccy** | **str** | The currency of the underlying | [optional] 
**underlying_identifier** | **str** | External market codes and identifiers for the CFD, e.g. RIC.    Supported string (enumeration) values are: [LusidInstrumentId, Isin, Sedol, Cusip, ClientInternal, Figi, RIC, QuotePermId, REDCode, BBGId, ICECode]. | [optional] 
**lot_size** | **int** | CFD LotSize, the minimum number of shares that can be bought or sold at once.  Optional, if set must be non-negative, if not set defaults to 1. | [optional] 
**underlying** | [**LusidInstrument**](LusidInstrument.md) |  | [optional] 
**instrument_type** | **str** | The available values are: QuotedSecurity, InterestRateSwap, FxForward, Future, ExoticInstrument, FxOption, CreditDefaultSwap, InterestRateSwaption, Bond, EquityOption, FixedLeg, FloatingLeg, BespokeCashFlowsLeg, Unknown, TermDeposit, ContractForDifference, EquitySwap, CashPerpetual, CapFloor, CashSettled, CdsIndex, Basket, FundingLeg, FxSwap, ForwardRateAgreement, SimpleInstrument, Repo, Equity, ExchangeTradedOption, ReferenceInstrument, ComplexBond, InflationLinkedBond, InflationSwap, SimpleCashFlowLoan, TotalReturnSwap, InflationLeg, FundShareClass, FlexibleLoan, UnsettledCash, Cash, MasteredInstrument, LoanFacility, FlexibleDeposit | 

## Example

```python
from lusid.models.contract_for_difference import ContractForDifference

# TODO update the JSON string below
json = "{}"
# create an instance of ContractForDifference from a JSON string
contract_for_difference_instance = ContractForDifference.from_json(json)
# print the JSON string representation of the object
print ContractForDifference.to_json()

# convert the object into a dict
contract_for_difference_dict = contract_for_difference_instance.to_dict()
# create an instance of ContractForDifference from a dict
contract_for_difference_form_dict = contract_for_difference.from_dict(contract_for_difference_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


