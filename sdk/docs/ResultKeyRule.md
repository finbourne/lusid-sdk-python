# ResultKeyRule

Base class for representing result key rules in LUSID, which describe how to resolve (unit) result data.  This base class should not be directly instantiated; each supported ResultKeyRuleType has a corresponding inherited class.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**result_key_rule_type** | **str** | The available values are: Invalid, ResultDataKeyRule, PortfolioResultDataKeyRule | 
## Example

```python
from lusid.models.result_key_rule import ResultKeyRule
from typing import Any, Dict, Union
from pydantic.v1 import BaseModel, Field, StrictStr, validator

result_key_rule_type: StrictStr = "example_result_key_rule_type"
result_key_rule_instance = ResultKeyRule(result_key_rule_type=result_key_rule_type)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

