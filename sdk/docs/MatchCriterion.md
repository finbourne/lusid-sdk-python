# MatchCriterion

A condition to be evaluated.  Each supported CriterionType has a corresponding schema.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**criterion_type** | **str** | The available values are: PropertyValueEquals, PropertyValueIn, SubHoldingKeyValueEquals | 
## Example

```python
from lusid.models.match_criterion import MatchCriterion
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

criterion_type: StrictStr = "example_criterion_type"
match_criterion_instance = MatchCriterion(criterion_type=criterion_type)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

