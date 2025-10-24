# FlexibleRepo

Lusid representation of a repurchase agreement, where one party sells some collateral and agrees to re-buy it at a later date for some given price.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**start_date** | **datetime** | The start date of the instrument. This is normally synonymous with the trade-date. | 
**maturity_date** | **datetime** | The maturity date of the instrument. This is the date at which the repurchase will occur for a TermRepo.  Optional for OpenRepo, but if not provided, defaults to the StartDate plus a long period (e.g. 2099-12-31). | [optional] 
**buyer_or_seller** | **str** | Is the user the Buyer or the Seller of this repo?  Every repo agreement has two sides, a buyer and a seller.  The Buyer pays the PurchasePrice to the Seller in exchange for legal ownership of the collateral.  At Maturity, the Buyer then receives the RepurchasePrice in exchange for returning legal ownership of the collateral.  Controls the direction of purchase and repurchase cashflows, as well as the recipient of cashflows from the collateral.    Supported string (enumeration) values are: [Buyer, Seller]. | 
**repo_ccy** | **str** | Currency of the purchase and repurchase prices. May differ from the currencies on any collateral. | 
**repo_type** | **str** | The type of the repurchase agreement, Open or Term.  If Term, the repurchase automatically takes place at Maturity.  If Open, the agreement is rolled by the given tenor, and an interest cashflow is paid out with each roll,  unless manually triggered by a FlexibleRepoFullClosureEvent.    Supported string (enumeration) values are: [OpenRepo, TermRepo]. | 
**accrual_basis** | **str** | For calculation of interest, the accrual day count to be used.  Required if no RepoRateSchedules are provided.  If both RepoRateSchedules and AccrualBasis are provided,  then AccrualBasis will take precedence.    Supported string (enumeration) values are: [Actual360, Act360, MoneyMarket, Actual365, Act365, Thirty360, ThirtyU360, Bond, ThirtyE360, EuroBond, ActualActual, ActAct, ActActIsda, ActActIsma, ActActIcma, OneOne, Act364, Act365F, Act365L, Act365_25, Act252, Bus252, NL360, NL365, ActActAFB, Act365Cad, ThirtyActIsda, Thirty365Isda, ThirtyEActIsda, ThirtyE360Isda, ThirtyE365Isda, ThirtyU360EOM]. | [optional] 
**collateral** | [**Collateral**](Collateral.md) |  | [optional] 
**haircut** | **float** | Haircut on the value of the collateral, used to calculate PurchasePrice if not provided directly.  Haircut or Margin should be specified if PurchasePrice is not specified. | [optional] 
**margin** | **float** | Initial margin on the value of the collateral, used to calculate PurchasePrice if not provided directly.  Haircut or Margin should be specified if PurchasePrice is not specified. | [optional] 
**open_repo_rolling_period** | **str** | Required if the RepoType is Open.  The tenor representing the mandatory roll period if the FlexibleRepo is not manually matured.  If a user matures the FlexibleRepo via an instrument event, then the repurchase will delay until the end of this rolling period.  Generally this is set to 1D (one day), i.e. the repurchase will occur on the same day as the instrument event,  though any valid tenor is accepted with TenorUnit set to Day, Week, Month, or Year.  Note that TenorUnit T is not accepted here. | [optional] 
**purchase_price** | **float** | The initial purchase price of the collateral.  If provided directly in this field, then Collateral.CollateralValue,  Haircut, and Margin should not be provided. | [optional] 
**repo_rate_schedules** | [**List[Schedule]**](Schedule.md) | Schedules used to calculate the repurchase price and any interest payments on the FlexibleRepo.  Only one schedule may be provided, and must be of type FixedSchedule or FloatSchedule.  If RepoType is OpenRepo, a FixedSchedule or FloatSchedule must be provided to calculate the expected Repo Rate,  and RepurchasePrice must be omitted.  If RepoType is TermRepo, only one of RepurchasePrice and RepoRateSchedules should be provided.  If a RepoRateSchedule is provided on a TermRepo, the PaymentFrequency in the FlowConventions should be 1T.  StubType must be set to None, and no ExDividend configuration should be provided. | [optional] 
**repurchase_price** | **float** | The repurchase price of the repo, if known.  Only one of RepurchasePrice and RepoRateSchedules should be provided.  In the case of an OpenRepo, RepurchasePrice should not be provided,  and RepoRateSchedules should be provided instead in order to calculate the RepoRate. | [optional] 
**time_zone_conventions** | [**TimeZoneConventions**](TimeZoneConventions.md) |  | [optional] 
**trading_conventions** | [**TradingConventions**](TradingConventions.md) |  | [optional] 
**is_collateral_transfer_activated** | **bool** | Indicates whether the FlexibleRepoCollateralTransfer event is activated.  Determines the behavior of manufactured coupons and related boolean parameters.  Defaults to false.  When true:  - Generates the FlexibleRepoCollateralTransfer event  - Processes collateral transfer transactions into holding changes  - Generates manufactured payments when due to be paid                When false:  - Does not generate the event  - Generates manufactured payments when due to be received | [optional] 
**instrument_type** | **str** | The available values are: QuotedSecurity, InterestRateSwap, FxForward, Future, ExoticInstrument, FxOption, CreditDefaultSwap, InterestRateSwaption, Bond, EquityOption, FixedLeg, FloatingLeg, BespokeCashFlowsLeg, Unknown, TermDeposit, ContractForDifference, EquitySwap, CashPerpetual, CapFloor, CashSettled, CdsIndex, Basket, FundingLeg, FxSwap, ForwardRateAgreement, SimpleInstrument, Repo, Equity, ExchangeTradedOption, ReferenceInstrument, ComplexBond, InflationLinkedBond, InflationSwap, SimpleCashFlowLoan, TotalReturnSwap, InflationLeg, FundShareClass, FlexibleLoan, UnsettledCash, Cash, MasteredInstrument, LoanFacility, FlexibleDeposit, FlexibleRepo | 
## Example

```python
from lusid.models.flexible_repo import FlexibleRepo
from typing import Any, Dict, List, Optional, Union
from pydantic.v1 import Field, StrictBool, StrictFloat, StrictInt, StrictStr, conlist, constr, validator
from datetime import datetime
start_date: datetime = # Replace with your value
maturity_date: Optional[datetime] = # Replace with your value
buyer_or_seller: StrictStr = "example_buyer_or_seller"
repo_ccy: StrictStr = "example_repo_ccy"
repo_type: StrictStr = "example_repo_type"
accrual_basis: Optional[StrictStr] = "example_accrual_basis"
collateral: Optional[Collateral] = None
haircut: Optional[Union[StrictFloat, StrictInt]] = # Replace with your value
margin: Optional[Union[StrictFloat, StrictInt]] = # Replace with your value
open_repo_rolling_period: Optional[StrictStr] = "example_open_repo_rolling_period"
purchase_price: Optional[Union[StrictFloat, StrictInt]] = # Replace with your value
repo_rate_schedules: Optional[conlist(Schedule)] = # Replace with your value
repurchase_price: Optional[Union[StrictFloat, StrictInt]] = # Replace with your value
time_zone_conventions: Optional[TimeZoneConventions] = # Replace with your value
trading_conventions: Optional[TradingConventions] = # Replace with your value
is_collateral_transfer_activated: Optional[StrictBool] = # Replace with your value
is_collateral_transfer_activated:Optional[StrictBool] = None
instrument_type: StrictStr = "example_instrument_type"
flexible_repo_instance = FlexibleRepo(start_date=start_date, maturity_date=maturity_date, buyer_or_seller=buyer_or_seller, repo_ccy=repo_ccy, repo_type=repo_type, accrual_basis=accrual_basis, collateral=collateral, haircut=haircut, margin=margin, open_repo_rolling_period=open_repo_rolling_period, purchase_price=purchase_price, repo_rate_schedules=repo_rate_schedules, repurchase_price=repurchase_price, time_zone_conventions=time_zone_conventions, trading_conventions=trading_conventions, is_collateral_transfer_activated=is_collateral_transfer_activated, instrument_type=instrument_type)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

