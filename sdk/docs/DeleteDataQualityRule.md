# DeleteDataQualityRule

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**rule_set_key** | **str** |  | [optional] 
**rule_key** | **str** |  | [optional] 
## Example

```python
from lusid.models.delete_data_quality_rule import DeleteDataQualityRule
from typing import Any, Dict, Optional
from pydantic.v1 import BaseModel, Field, constr

rule_set_key: Optional[StrictStr] = "example_rule_set_key"
rule_key: Optional[StrictStr] = "example_rule_key"
delete_data_quality_rule_instance = DeleteDataQualityRule(rule_set_key=rule_set_key, rule_key=rule_key)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

