# FundPartner

A register line of a partnership fund: one partner's commitment and its capital balances at an effective date.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**investor_record_id** | **str** | The identifier of the investor record this register line belongs to. | 
**display_name** | **str** | The display name of the partner. | [optional] 
**commitment_line_id** | **str** | The identifier of the commitment (register) line. | 
**lusid_instrument_id** | **str** | The LUSID instrument identifier of the register line&#39;s capital-interest instrument. | 
**portfolio_id** | [**ResourceId**](ResourceId.md) |  | 
**is_vehicle** | **bool** | Whether the partner is a vehicle (for example a feeder or parallel fund) rather than an end investor. | 
**partner_role** | **str** | The role the partner plays in the partnership. Available values: LimitedPartner (the default), GeneralPartner, GPAffiliate, Employee, CarryVehicle. | 
**register_role** | **str** | The role of the register line. Available values: GPRegister, LPInvestment (the default). | 
**commitment_currency** | **str** | The currency of the partner&#39;s commitment. | 
**balances** | [**FundPartnerBalances**](FundPartnerBalances.md) |  | 
**share_of_commitments** | **float** | The partner&#39;s committed capital as a decimal fraction of the fund&#39;s total commitments in the same commitment currency. | 
**admitted_on** | **datetime** | The date the partner was admitted, being the date of their first commitment. | [optional] 
**totals** | [**FundPartnersTotals**](FundPartnersTotals.md) |  | 
## Example

```python
from lusid.models.fund_partner import FundPartner
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

investor_record_id: StrictStr = "example_investor_record_id"
display_name: Optional[StrictStr] = "example_display_name"
commitment_line_id: StrictStr = "example_commitment_line_id"
lusid_instrument_id: StrictStr = "example_lusid_instrument_id"
portfolio_id: ResourceId = # Replace with your value
is_vehicle: StrictBool = # Replace with your value
is_vehicle:StrictBool = True
partner_role: StrictStr = "example_partner_role"
register_role: StrictStr = "example_register_role"
commitment_currency: StrictStr = "example_commitment_currency"
balances: FundPartnerBalances
share_of_commitments: Union[StrictFloat, StrictInt] = # Replace with your value
admitted_on: Optional[datetime] = # Replace with your value
totals: FundPartnersTotals
fund_partner_instance = FundPartner(investor_record_id=investor_record_id, display_name=display_name, commitment_line_id=commitment_line_id, lusid_instrument_id=lusid_instrument_id, portfolio_id=portfolio_id, is_vehicle=is_vehicle, partner_role=partner_role, register_role=register_role, commitment_currency=commitment_currency, balances=balances, share_of_commitments=share_of_commitments, admitted_on=admitted_on, totals=totals)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

