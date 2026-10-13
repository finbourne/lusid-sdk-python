# AllocationEventComponent

One component of an Allocation Event: a part of the amount shared on its own basis and booked to its own slot.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**component** | **str** | The component. For a CapitalCall one of Investment, MgmtFee, OtherFee, PartnershipExpense, OrgCost, Recall, EqualisationInterest or LatePaymentInterest; for a Distribution one of ROC, RealisedGain, Dividend, Interest, OtherIncome, CarryPaid, Withholding or ReturnOfExcess. | 
**amount** | **float** | The part of the event amount this component carries, in the event currency. May be zero, in which case the component allocates nothing. | 
**origin_member_short_code** | **str** | The member of the structure the component originates from, for a basis measured per deal such as PaidInForDeal. Absent means the map&#39;s own member. | [optional] 
**waterfall_tier** | **str** | For a distribution component, the tier of the waterfall it was paid under: ReturnOfContributions, PreferredReturn, CatchUp, CarriedInterest or Residual. | [optional] 
**tax_character** | **str** | For a distribution component, the tax character of the amount: ROC, Gain, Income or Deemed. | [optional] 
## Example

```python
from lusid.models.allocation_event_component import AllocationEventComponent
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

component: StrictStr = "example_component"
amount: Union[StrictFloat, StrictInt] = # Replace with your value
origin_member_short_code: Optional[StrictStr] = "example_origin_member_short_code"
waterfall_tier: Optional[StrictStr] = "example_waterfall_tier"
tax_character: Optional[StrictStr] = "example_tax_character"
allocation_event_component_instance = AllocationEventComponent(component=component, amount=amount, origin_member_short_code=origin_member_short_code, waterfall_tier=waterfall_tier, tax_character=tax_character)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

