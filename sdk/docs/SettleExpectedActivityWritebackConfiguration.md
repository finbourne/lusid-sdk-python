# SettleExpectedActivityWritebackConfiguration

Suggests settlement instructions where settlement on the origin side confirms expected settlement activity  on the target side. Only valid on a ruleset whose recType is SettlementActivity.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**mandatory_rule_names** | [**SettleExpectedActivityRuleNames**](SettleExpectedActivityRuleNames.md) |  | 
**result_patterns** | [**List[WritebackResultPattern]**](WritebackResultPattern.md) | The combinations of units difference and result cardinality for which writeback is suggested. A combination that is not present never produces a suggestion. Each combination may appear once, and the collection is returned in a canonical order regardless of the order supplied. | 
**writeback_type** | **str** | Polymorphic discriminator, naming the change the writeback makes to LUSID. Supported types: SettleExpectedActivity, which is only valid when recType is SettlementActivity. Available values: SettleExpectedActivity. | 
**target_side** | **str** | The side the writeback changes, the other being the source of truth. One of: Left, Right. As the writeback changes LUSID, this side must draw on a native LUSID dataset rather than relational data. Available values: Left, Right. | 
## Example

```python
from lusid.models.settle_expected_activity_writeback_configuration import SettleExpectedActivityWritebackConfiguration
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

mandatory_rule_names: SettleExpectedActivityRuleNames = # Replace with your value
result_patterns: List[WritebackResultPattern] = # Replace with your value
writeback_type: StrictStr = "example_writeback_type"
target_side: StrictStr = "example_target_side"
settle_expected_activity_writeback_configuration_instance = SettleExpectedActivityWritebackConfiguration(mandatory_rule_names=mandatory_rule_names, result_patterns=result_patterns, writeback_type=writeback_type, target_side=target_side)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

