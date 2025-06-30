# MatchCriterion

A condition to be evaluated.  Each supported CriterionType has a corresponding schema.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**criterion_type** | **str** | The available values are: PropertyValueEquals, PropertyValueIn, SubHoldingKeyValueEquals | 
## Example

```python
from lusid.models.match_criterion import MatchCriterion
from typing import Any, Dict, Union
from pydantic.v1 import BaseModel, Field, StrictStr, validator

criterion_type: StrictStr = "example_criterion_type"
match_criterion_instance = MatchCriterion(criterion_type=criterion_type)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

