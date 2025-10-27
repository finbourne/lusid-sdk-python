# CapFloor

LUSID representation of Cap, Floor, or Collar.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cap_floor_type** | **str** | Determine if it&#39;s CAP, FLOOR, or COLLAR.    Supported string (enumeration) values are: [Cap, Floor, Collar]. | 
**cap_strike** | **float** | Strike rate of the Cap. | [optional] 
**floor_strike** | **float** | Strike rate of the Floor. | [optional] 
**include_first_caplet** | **bool** | Include first caplet flag. | 
**underlying_floating_leg** | [**FloatingLeg**](FloatingLeg.md) |  | 
**additional_payments** | [**List[AdditionalPayment]**](AdditionalPayment.md) | Optional additional payments at a given date e.g. to level off an uneven equity swap.  The dates must be distinct and either all payments are Pay or all payments are Receive. | [optional] 
**time_zone_conventions** | [**TimeZoneConventions**](TimeZoneConventions.md) |  | [optional] 
**instrument_type** | **str** | The available values are: QuotedSecurity, InterestRateSwap, FxForward, Future, ExoticInstrument, FxOption, CreditDefaultSwap, InterestRateSwaption, Bond, EquityOption, FixedLeg, FloatingLeg, BespokeCashFlowsLeg, Unknown, TermDeposit, ContractForDifference, EquitySwap, CashPerpetual, CapFloor, CashSettled, CdsIndex, Basket, FundingLeg, FxSwap, ForwardRateAgreement, SimpleInstrument, Repo, Equity, ExchangeTradedOption, ReferenceInstrument, ComplexBond, InflationLinkedBond, InflationSwap, SimpleCashFlowLoan, TotalReturnSwap, InflationLeg, FundShareClass, FlexibleLoan, UnsettledCash, Cash, MasteredInstrument, LoanFacility, FlexibleDeposit, FlexibleRepo | 
## Example

```python
from lusid.models.cap_floor import CapFloor
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

cap_floor_type: StrictStr = "example_cap_floor_type"
cap_strike: Optional[Union[StrictFloat, StrictInt]] = # Replace with your value
floor_strike: Optional[Union[StrictFloat, StrictInt]] = # Replace with your value
include_first_caplet: StrictBool = # Replace with your value
include_first_caplet:StrictBool = True
underlying_floating_leg: FloatingLeg = # Replace with your value
additional_payments: Optional[List[AdditionalPayment]] = # Replace with your value
time_zone_conventions: Optional[TimeZoneConventions] = # Replace with your value
instrument_type: StrictStr = "example_instrument_type"
cap_floor_instance = CapFloor(cap_floor_type=cap_floor_type, cap_strike=cap_strike, floor_strike=floor_strike, include_first_caplet=include_first_caplet, underlying_floating_leg=underlying_floating_leg, additional_payments=additional_payments, time_zone_conventions=time_zone_conventions, instrument_type=instrument_type)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

