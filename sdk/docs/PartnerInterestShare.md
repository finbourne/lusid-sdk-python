# PartnerInterestShare

How a holder's partner interest in a held fund structure member flowed when the valuation point was struck: from  the member's booked partner allocation, from a dry run of it, at a provisional share of committed capital, or at  the sharing percentage the fund structure edge declares.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**holder** | **str** | The short code of the holding fund, as the fund structure names it. | 
**member** | **str** | The short code of the held fund structure member whose P&amp;L flowed. | 
**via_instrument_id** | **str** | The LUSID instrument id of the instrument the holder holds the member through: the holder&#39;s line on the member&#39;s partner register. | 
**share_source** | **str** | Where the holder&#39;s share of the member&#39;s P&amp;L came from. &#39;MemberBooked&#39;: the member&#39;s booked partner allocation to the holder&#39;s line for the period, pool by pool, which a Final valuation point requires. &#39;MemberDryRun&#39;: the member has not booked the period, so a dry run of its allocation gave the holder&#39;s line what the booking would; the point cannot be accepted until the member books and the point is struck again. &#39;Provisional&#39;: the member cannot be allocated yet, so the member&#39;s P&amp;L flowed at the line&#39;s committed capital over the register total; the point cannot be accepted until the member books and the point is struck again. &#39;Declared&#39;: the via instrument is not a line of the member&#39;s register, or the register carries no commitments, so the edge&#39;s declared sharing percentage was used; the valuation point&#39;s diagnostics name the fall-back. | 
**reason** | **str** | Why a provisional or declared share was taken. Absent when the share came from the member&#39;s allocation. | [optional] 
## Example

```python
from lusid.models.partner_interest_share import PartnerInterestShare
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

holder: StrictStr = "example_holder"
member: StrictStr = "example_member"
via_instrument_id: StrictStr = "example_via_instrument_id"
share_source: StrictStr = "example_share_source"
reason: Optional[StrictStr] = "example_reason"
partner_interest_share_instance = PartnerInterestShare(holder=holder, member=member, via_instrument_id=via_instrument_id, share_source=share_source, reason=reason)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

