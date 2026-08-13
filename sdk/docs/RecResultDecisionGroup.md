# RecResultDecisionGroup

The group-decision detail carried on every member of a FixAsGroup or ForceMatch decision.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**group_number** | **int** | Server-allocated, monotonic group number, unique within the RecResultSet and never reused. | 
**core_rules_excused** | **List[str]** | The ruleNames of the core rules excused by a ForceMatch. Identical on every group member; non-null only for ForceMatch. | [optional] 
## Example

```python
from lusid.models.rec_result_decision_group import RecResultDecisionGroup
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

group_number: StrictInt = # Replace with your value
group_number: StrictInt = 42
core_rules_excused: Optional[List[StrictStr]] = # Replace with your value
rec_result_decision_group_instance = RecResultDecisionGroup(group_number=group_number, core_rules_excused=core_rules_excused)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

