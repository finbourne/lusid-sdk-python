# Repo

LUSID representation of a sale and repurchase agreement, supporting haircut, margin or repo rate methods.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**start_date** | **datetime** | The start date of the instrument. This is normally synonymous with the trade-date. | 
**maturity_date** | **datetime** | The final maturity date of the instrument. This means the last date on which the instruments makes a payment of any amount.  For the avoidance of doubt, that is not necessarily prior to its last sensitivity date for the purposes of risk; e.g. instruments such as  Constant Maturity Swaps (CMS) often have sensitivities to rates that may well be observed or set prior to the maturity date, but refer to a termination date beyond it. | 
**dom_ccy** | **str** | The domestic currency of the instrument. | 
**accrual_basis** | **str** | For calculation of interest, the accrual basis to be used.  For more information on day counts, see [knowledge base article KA-01798](https://support.lusid.com/knowledgebase/article/KA-01798)                Supported string (enumeration) values are: [Actual360, Act360, MoneyMarket, Actual365, Act365, Thirty360, ThirtyU360, Bond, ThirtyE360, EuroBond, ActualActual, ActAct, ActActIsda, ActActIsma, ActActIcma, OneOne, Act364, Act365F, Act365L, Act365_25, Act252, Bus252, NL360, NL365, ActActAFB, Act365Cad, ThirtyActIsda, Thirty365Isda, ThirtyEActIsda, ThirtyE360Isda, ThirtyE365Isda, ThirtyU360EOM]. | 
**collateral** | [**List[LusidInstrument]**](LusidInstrument.md) | The actual collateral in the Repo.  This property is for informational purposes only, Lusid pricing is not affected. | [optional] 
**collateral_value** | **float** | The full market value of the collateral in domestic currency, before any margin or haircut is applied. | [optional] 
**haircut** | **float** | The haircut (or margin percentage) applied to the collateral, this should be a number between 0 and 1, i.e. for a 5% haircut this should be 0.05.  This is defined as (CollateralValue - PurchasePrice) / CollateralValue.  If this property is specified, so too must CollateralValue.  While this property is optional, one, and only one, of PurchasePrice, Margin and Haircut must be specified. | [optional] 
**margin** | **float** | The initial margin (or margin ratio) applied to the collateral, this should be a number greater than or equal to 1.0,  i.e. for a 102% margin this should be 1.02. A value of 1.0 means no margin (100%).  This is defined as CollateralValue / PurchasePrice.  If this property is specified, so too must CollateralValue.  While this property is optional, one, and only one, of PurchasePrice, Margin and Haircut must be specified. | [optional] 
**purchase_price** | **float** | The price the collateral is initially purchased for, this property can be used to explicitly set the purchase price and not require  collateral value and a margin or haircut.  While this property is optional, one, and only one, of PurchasePrice, Margin and Haircut must be specified. | [optional] 
**repo_rate** | **float** | The rate at which interest is to be accrue and be paid upon redemption of the collateral at maturity.  This field is used to calculate the Repurchase price.  While this property is optional, one, and only one, of the RepoRate and RepurchasePrice must be specified. | [optional] 
**repurchase_price** | **float** | The price at which the collateral is repurchased, this field is optional and can be explicitly set here or will be calculated  from the PurchasePrice and RepoRate.  One, and only one, of the RepoRate and RepurchasePrice must be specified. | [optional] 
**time_zone_conventions** | [**TimeZoneConventions**](TimeZoneConventions.md) |  | [optional] 
**instrument_type** | **str** | The available values are: QuotedSecurity, InterestRateSwap, FxForward, Future, ExoticInstrument, FxOption, CreditDefaultSwap, InterestRateSwaption, Bond, EquityOption, FixedLeg, FloatingLeg, BespokeCashFlowsLeg, Unknown, TermDeposit, ContractForDifference, EquitySwap, CashPerpetual, CapFloor, CashSettled, CdsIndex, Basket, FundingLeg, FxSwap, ForwardRateAgreement, SimpleInstrument, Repo, Equity, ExchangeTradedOption, ReferenceInstrument, ComplexBond, InflationLinkedBond, InflationSwap, SimpleCashFlowLoan, TotalReturnSwap, InflationLeg, FundShareClass, FlexibleLoan, UnsettledCash, Cash, MasteredInstrument, LoanFacility, FlexibleDeposit, FlexibleRepo | 
## Example

```python
from lusid.models.repo import Repo
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

start_date: datetime = # Replace with your value
maturity_date: datetime = # Replace with your value
dom_ccy: StrictStr = "example_dom_ccy"
accrual_basis: StrictStr = "example_accrual_basis"
collateral: Optional[List[LusidInstrument]] = # Replace with your value
collateral_value: Optional[Union[StrictFloat, StrictInt]] = # Replace with your value
haircut: Optional[Union[StrictFloat, StrictInt]] = # Replace with your value
margin: Optional[Union[StrictFloat, StrictInt]] = # Replace with your value
purchase_price: Optional[Union[StrictFloat, StrictInt]] = # Replace with your value
repo_rate: Optional[Union[StrictFloat, StrictInt]] = # Replace with your value
repurchase_price: Optional[Union[StrictFloat, StrictInt]] = # Replace with your value
time_zone_conventions: Optional[TimeZoneConventions] = # Replace with your value
instrument_type: StrictStr = "example_instrument_type"
repo_instance = Repo(start_date=start_date, maturity_date=maturity_date, dom_ccy=dom_ccy, accrual_basis=accrual_basis, collateral=collateral, collateral_value=collateral_value, haircut=haircut, margin=margin, purchase_price=purchase_price, repo_rate=repo_rate, repurchase_price=repurchase_price, time_zone_conventions=time_zone_conventions, instrument_type=instrument_type)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

