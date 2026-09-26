# SettleExpectedActivityRuleNames

Names the matching rules that carry the settlement semantics a SettleExpectedActivity writeback depends  upon. Each named rule's target-side formula must be the unmodified settlement activity field; the origin  side is unconstrained.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**activity_type** | **str** | The core rule whose target-side formula is the unmodified &#39;activityType&#39;. Settlement instructions are suggested where the origin-side value is Settled and the target-side value is Expected. | 
**activity_date** | **str** | The core rule whose target-side formula is the unmodified &#39;activityDate&#39;. The origin side supplies the actual settlement date. | 
**units** | **str** | The aggregate rule whose target-side formula is the unmodified &#39;units&#39;. The origin side supplies the units, and the tolerance on this rule classifies the units difference. | 
## Example

```python
from lusid.models.settle_expected_activity_rule_names import SettleExpectedActivityRuleNames
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

activity_type: StrictStr = "example_activity_type"
activity_date: StrictStr = "example_activity_date"
units: StrictStr = "example_units"
settle_expected_activity_rule_names_instance = SettleExpectedActivityRuleNames(activity_type=activity_type, activity_date=activity_date, units=units)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

