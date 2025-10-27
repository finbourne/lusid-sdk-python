# RulesInterval

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**effective_range** | [**DateRange**](DateRange.md) |  | 
**rules** | [**List[AmortisationRule]**](AmortisationRule.md) | The rules of this rule set. | 
## Example

```python
from lusid.models.rules_interval import RulesInterval
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

effective_range: DateRange = # Replace with your value
rules: List[AmortisationRule] = # Replace with your value
rules_interval_instance = RulesInterval(effective_range=effective_range, rules=rules)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

