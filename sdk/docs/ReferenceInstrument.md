# ReferenceInstrument

LUSID representation of a reference to another instrument that has already been loaded (e.g. a lookthrough to a portfolio).
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**instrument_id** | **str** | The Identifier code | 
**instrument_id_type** | **str** | The type of the instrument id e.g. LusidInstrument Id | 
**scope** | **str** | Scope for the instrument (optional) | 
**instrument_type** | **str** | The available values are: QuotedSecurity, InterestRateSwap, FxForward, Future, ExoticInstrument, FxOption, CreditDefaultSwap, InterestRateSwaption, Bond, EquityOption, FixedLeg, FloatingLeg, BespokeCashFlowsLeg, Unknown, TermDeposit, ContractForDifference, EquitySwap, CashPerpetual, CapFloor, CashSettled, CdsIndex, Basket, FundingLeg, FxSwap, ForwardRateAgreement, SimpleInstrument, Repo, Equity, ExchangeTradedOption, ReferenceInstrument, ComplexBond, InflationLinkedBond, InflationSwap, SimpleCashFlowLoan, TotalReturnSwap, InflationLeg, FundShareClass, FlexibleLoan, UnsettledCash, Cash, MasteredInstrument, LoanFacility, FlexibleDeposit, FlexibleRepo | 
## Example

```python
from lusid.models.reference_instrument import ReferenceInstrument
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

instrument_id: StrictStr = "example_instrument_id"
instrument_id_type: StrictStr = "example_instrument_id_type"
scope: StrictStr = "example_scope"
instrument_type: StrictStr = "example_instrument_type"
reference_instrument_instance = ReferenceInstrument(instrument_id=instrument_id, instrument_id_type=instrument_id_type, scope=scope, instrument_type=instrument_type)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

