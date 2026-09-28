# AllocationMapParticipants

Who takes part in the allocations of an Allocation Map: the default rule that finds the participant set, and the  exceptions that exclude particular investor records or fix their share.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**rule** | **str** | How the default participant set is found. AllCommittedToMembers takes every investor record committed to any of the funds in memberIds; ExplicitList takes exactly the investor records in explicitInvestorRecordIds. Available values: AllCommittedToMembers, ExplicitList. | [optional] 
**member_ids** | [**List[ResourceId]**](ResourceId.md) | Under the AllCommittedToMembers rule, the member funds whose committed investor records participate, as scope and code. At least one is required under that rule. | [optional] 
**explicit_investor_record_ids** | **List[str]** | Under the ExplicitList rule, the investor records that participate. At least one is required under that rule. | [optional] 
**exceptions** | [**List[AllocationMapException]**](AllocationMapException.md) | Departures from the default participation for particular investor records. Each names the investor record, what happens to it, and why. | [optional] 
## Example

```python
from lusid.models.allocation_map_participants import AllocationMapParticipants
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

rule: Optional[StrictStr] = "example_rule"
member_ids: Optional[List[ResourceId]] = # Replace with your value
explicit_investor_record_ids: Optional[List[StrictStr]] = # Replace with your value
exceptions: Optional[List[AllocationMapException]] = # Replace with your value
allocation_map_participants_instance = AllocationMapParticipants(rule=rule, member_ids=member_ids, explicit_investor_record_ids=explicit_investor_record_ids, exceptions=exceptions)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

