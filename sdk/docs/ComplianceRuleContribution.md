# ComplianceRuleContribution

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**portfolio_id** | [**ResourceId**](ResourceId.md) |  | 
**order_id** | [**ResourceId**](ResourceId.md) |  | [optional] 
**instrument** | **str** | The LUSID instrument identifier (LUID) of the instrument for this contribution. | 
**instrument_type** | **str** | Optional. The economic type of the instrument for this contribution. | [optional] 
**holding_type** | **str** | Optional. The holding type of this contribution. | [optional] 
**holding_id** | **str** | Optional. The internal holding identifier encoding the detail of what the holding includes. | [optional] 
**held_by** | **str** | Optional. Where this holding sits relative to the rule&#39;s benchmark: portfolio, benchmark or both.  Meaningful only for benchmark-relative rules. | [optional] 
**keys_used** | [**List[ComplianceKeyUsed]**](ComplianceKeyUsed.md) | The keys this holding contributed to the rule: each key the rule read (plus the portfolio NAV key), with the  role(s) it played, the holding&#39;s own value for it, and which bag the value came from. | 
## Example

```python
from lusid.models.compliance_rule_contribution import ComplianceRuleContribution
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

portfolio_id: ResourceId = # Replace with your value
order_id: Optional[ResourceId] = # Replace with your value
instrument: StrictStr = "example_instrument"
instrument_type: Optional[StrictStr] = "example_instrument_type"
holding_type: Optional[StrictStr] = "example_holding_type"
holding_id: Optional[StrictStr] = "example_holding_id"
held_by: Optional[StrictStr] = "example_held_by"
keys_used: List[ComplianceKeyUsed] = # Replace with your value
compliance_rule_contribution_instance = ComplianceRuleContribution(portfolio_id=portfolio_id, order_id=order_id, instrument=instrument, instrument_type=instrument_type, holding_type=holding_type, holding_id=holding_id, held_by=held_by, keys_used=keys_used)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

