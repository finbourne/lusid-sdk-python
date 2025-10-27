# MasteredInstrument

LUSID representation of a reference to another instrument that has already been upserted (Mastered)
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**identifiers** | **Dict[str, Optional[str]]** | Dictionary of identifiers of the mastered instrument | 
**mastered_dom_ccy** | **str** | DomCcy of the Instrument that Mastered Instrument points to - read only field | [optional] [readonly] 
**mastered_instrument_type** | **str** | Type of the Instrument that Mastered Instrument points to - read only field | [optional] [readonly] 
**mastered_lusid_instrument_id** | **str** | Luid of the Instrument that Mastered Instrument points to - read only field | [optional] [readonly] 
**mastered_name** | **str** | Name of the Instrument that Mastered Instrument points to - read only field | [optional] [readonly] 
**mastered_scope** | **str** | Scope of the Instrument that Mastered Instrument points to - read only field | [optional] [readonly] 
**mastered_asset_class** | **str** | Asset class of the underlying mastered instrument - read only field    Supported string (enumeration) values are: [InterestRates, FX, Inflation, Equities, Credit, Commodities, Money].  Defaults to \&quot;Unknown\&quot; if not set. | [optional] [readonly] 
**instrument_type** | **str** | The available values are: QuotedSecurity, InterestRateSwap, FxForward, Future, ExoticInstrument, FxOption, CreditDefaultSwap, InterestRateSwaption, Bond, EquityOption, FixedLeg, FloatingLeg, BespokeCashFlowsLeg, Unknown, TermDeposit, ContractForDifference, EquitySwap, CashPerpetual, CapFloor, CashSettled, CdsIndex, Basket, FundingLeg, FxSwap, ForwardRateAgreement, SimpleInstrument, Repo, Equity, ExchangeTradedOption, ReferenceInstrument, ComplexBond, InflationLinkedBond, InflationSwap, SimpleCashFlowLoan, TotalReturnSwap, InflationLeg, FundShareClass, FlexibleLoan, UnsettledCash, Cash, MasteredInstrument, LoanFacility, FlexibleDeposit, FlexibleRepo | 
## Example

```python
from lusid.models.mastered_instrument import MasteredInstrument
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

identifiers: Dict[str, Optional[StrictStr]] = # Replace with your value
mastered_dom_ccy: Optional[StrictStr] = "example_mastered_dom_ccy"
mastered_instrument_type: Optional[StrictStr] = "example_mastered_instrument_type"
mastered_lusid_instrument_id: Optional[StrictStr] = "example_mastered_lusid_instrument_id"
mastered_name: Optional[StrictStr] = "example_mastered_name"
mastered_scope: Optional[StrictStr] = "example_mastered_scope"
mastered_asset_class: Optional[StrictStr] = "example_mastered_asset_class"
instrument_type: StrictStr = "example_instrument_type"
mastered_instrument_instance = MasteredInstrument(identifiers=identifiers, mastered_dom_ccy=mastered_dom_ccy, mastered_instrument_type=mastered_instrument_type, mastered_lusid_instrument_id=mastered_lusid_instrument_id, mastered_name=mastered_name, mastered_scope=mastered_scope, mastered_asset_class=mastered_asset_class, instrument_type=instrument_type)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

