# CapitalInterest

LUSID representation of a CapitalInterest.  A CapitalInterest represents an investor's interest in a single commitment line to a  private-markets fund: one instrument per (fund, investor, commitment line). Units act as  a liveness flag (1 while the line is open, 0 once closed) and the economics are carried  by cost, fair value and the running capital balances rather than by quantity.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**quantity_basis** | **str** | How the quantity of the holding is interpreted. Under the &#39;Anchored&#39; basis, units act as a  liveness flag: 1 while the commitment line is open and 0 once it is closed. Only &#39;Anchored&#39;  is currently supported.                Supported string (enumeration) values are: [Anchored, Unitless]. Available values: Anchored, Unitless. | 
**commitment_currency** | **str** | The currency the commitment is denominated in. May differ from both the fund currency  and the portfolio base currency. | 
**fund_entity_id** | **str** | The identifier of the fund entity the commitment is made to. | 
**investor_entity_id** | **str** | The identifier of the investor entity holding the commitment. | 
**commitment_line_id** | **str** | The identifier of the commitment line, unique for a given fund and investor. | 
**original_commitment** | **float** | The committed amount at inception, in the commitment currency. May be zero for evergreen  funds. This is the original value only; subsequent amendments are carried by the running  capital balances, not by the instrument. | 
**commitment_date** | **datetime** | The date the commitment closed. | 
**vintage** | **int** | The vintage year of the commitment. Defaults to the year of the commitment date. | [optional] 
**capital_interest_asset_class** | **str** | The private-markets asset class of the fund the commitment is made to,  for example private equity, venture capital or infrastructure.                Supported string (enumeration) values are: [PrivateEquity, VentureCapital, PrivateCredit, RealAssets, Infrastructure, FundOfFunds, Secondary, CoInvestment, DirectEquity, ShareholderLoan, Other]. Available values: PrivateEquity, VentureCapital, PrivateCredit, RealAssets, Infrastructure, FundOfFunds, Secondary, CoInvestment, DirectEquity, ShareholderLoan, Other. | [optional] 
**relief_policy** | **str** | How distributions from the commitment line are relieved against the cost of the holding.  Defaults to &#39;InstructedCharacter&#39;.                Supported string (enumeration) values are: [InstructedCharacter, CostRecovery, ProportionalToFairValue, ProportionalToPercentageInterest, NoRelief]. Available values: InstructedCharacter, CostRecovery, ProportionalToFairValue, ProportionalToPercentageInterest, NoRelief. | [optional] 
**relief_revision_mode** | **str** | How revisions to previously applied distribution relief are handled.  Defaults to &#39;ProspectiveTrueUp&#39;.                Supported string (enumeration) values are: [ProspectiveTrueUp, Restate, Final]. Available values: ProspectiveTrueUp, Restate, Final. | [optional] 
**fair_value_source_precedence** | **List[str]** | The order of precedence of the sources a fair value for the interest can be taken from.  Defaults to the reported NAV rolled forward for subsequent capital activity, then cost.                Supported string (enumeration) values for each entry are: [ReportedNav, RollForward, Independent, Cost]. | [optional] 
**termination_date** | **datetime** | The expected end of the fund&#39;s life, if known. This is expected rather than contractual  and does not act as a maturity date for the instrument. | [optional] 
**instrument_type** | **str** | Available values: QuotedSecurity, InterestRateSwap, FxForward, Future, ExoticInstrument, FxOption, CreditDefaultSwap, InterestRateSwaption, Bond, EquityOption, FixedLeg, FloatingLeg, BespokeCashFlowsLeg, Unknown, TermDeposit, ContractForDifference, EquitySwap, CashPerpetual, CapFloor, CashSettled, CdsIndex, Basket, FundingLeg, FxSwap, ForwardRateAgreement, SimpleInstrument, Repo, Equity, ExchangeTradedOption, ReferenceInstrument, ComplexBond, InflationLinkedBond, InflationSwap, SimpleCashFlowLoan, TotalReturnSwap, InflationLeg, FundShareClass, FlexibleLoan, UnsettledCash, Cash, MasteredInstrument, LoanFacility, FlexibleDeposit, FlexibleRepo, ToBeAnnounced, VolatilitySwap, ToBeAnnouncedOption, CommodityForward, BondOption, CdsOption, CommodityCalendarSwap, BondForward, PreferredShare, CapitalInterest. | 
## Example

```python
from lusid.models.capital_interest import CapitalInterest
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

quantity_basis: StrictStr = "example_quantity_basis"
commitment_currency: StrictStr = "example_commitment_currency"
fund_entity_id: StrictStr = "example_fund_entity_id"
investor_entity_id: StrictStr = "example_investor_entity_id"
commitment_line_id: StrictStr = "example_commitment_line_id"
original_commitment: Union[StrictFloat, StrictInt] = # Replace with your value
commitment_date: datetime = # Replace with your value
vintage: Optional[StrictInt] = # Replace with your value
vintage: Optional[StrictInt] = None
capital_interest_asset_class: Optional[StrictStr] = "example_capital_interest_asset_class"
relief_policy: Optional[StrictStr] = "example_relief_policy"
relief_revision_mode: Optional[StrictStr] = "example_relief_revision_mode"
fair_value_source_precedence: Optional[List[StrictStr]] = # Replace with your value
termination_date: Optional[datetime] = # Replace with your value
instrument_type: StrictStr = "example_instrument_type"
capital_interest_instance = CapitalInterest(quantity_basis=quantity_basis, commitment_currency=commitment_currency, fund_entity_id=fund_entity_id, investor_entity_id=investor_entity_id, commitment_line_id=commitment_line_id, original_commitment=original_commitment, commitment_date=commitment_date, vintage=vintage, capital_interest_asset_class=capital_interest_asset_class, relief_policy=relief_policy, relief_revision_mode=relief_revision_mode, fair_value_source_precedence=fair_value_source_precedence, termination_date=termination_date, instrument_type=instrument_type)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

