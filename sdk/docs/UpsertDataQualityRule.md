# UpsertDataQualityRule

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**rule_set_key** | **str** |  | [optional] 
**rule** | [**CheckDefinitionRule**](CheckDefinitionRule.md) |  | [optional] 
## Example

```python
from lusid.models.upsert_data_quality_rule import UpsertDataQualityRule
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

rule_set_key: Optional[StrictStr] = "example_rule_set_key"
rule: Optional[CheckDefinitionRule] = None
upsert_data_quality_rule_instance = UpsertDataQualityRule(rule_set_key=rule_set_key, rule=rule)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

