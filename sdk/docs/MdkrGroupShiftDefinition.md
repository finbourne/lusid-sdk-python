# MdkrGroupShiftDefinition

A group of keyed market data key rules (e.g. bid/mid/ask). When the scenario is used in a  valuation, each key's rule re-resolves the matching market data dependencies independently and  produces its own result column named scenario:key, alongside the base column - which continues to  resolve through the recipe's own rules in the standard waterfall, whether or not the same rules  appear here.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**rules** | [**List[KeyedMarketDataKeyRule]**](KeyedMarketDataKeyRule.md) | The keyed rules of the group. Keys must be unique within the group; each key produces one  result column. | 
**scenario_shift_type** | **str** | Available values: RateCurveShiftDefinition, FxShiftDefinition, PriceShiftDefinition, VolSurfaceShiftDefinition, MdkrGroupShiftDefinition, InflationCurveShiftDefinition. | 
## Example

```python
from lusid.models.mdkr_group_shift_definition import MdkrGroupShiftDefinition
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

rules: List[KeyedMarketDataKeyRule] = # Replace with your value
scenario_shift_type: StrictStr = "example_scenario_shift_type"
mdkr_group_shift_definition_instance = MdkrGroupShiftDefinition(rules=rules, scenario_shift_type=scenario_shift_type)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

