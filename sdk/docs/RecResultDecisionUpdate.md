# RecResultDecisionUpdate

The decision update within a batch review item. Omitting the object leaves the existing decision  untouched; a null value nullifies it (dissolving any group).
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | **str** | The decision value. Null nullifies the decision. Available values: Acknowledge, FixAtSource, FixAsGroup, Accept, ForceMatch, Tolerate. | [optional] 
**affirm** | **bool** | Whether to affirm an existing decision (e.g. after revisions were requested). | [optional] 
**core_rules_excused** | **List[str]** | The ruleNames of the core rules excused by a ForceMatch. Identical on every group member; non-null only for ForceMatch. | [optional] 
## Example

```python
from lusid.models.rec_result_decision_update import RecResultDecisionUpdate
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

value: Optional[StrictStr] = "example_value"
affirm: Optional[StrictBool] = # Replace with your value
affirm:Optional[StrictBool] = None
core_rules_excused: Optional[List[StrictStr]] = # Replace with your value
rec_result_decision_update_instance = RecResultDecisionUpdate(value=value, affirm=affirm, core_rules_excused=core_rules_excused)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

