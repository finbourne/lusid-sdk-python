# CreateStagingRuleSetRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**display_name** | **str** | The name of the staging rule set. | 
**description** | **str** | A description for the staging rule set. | [optional] 
**rules** | [**List[StagingRule]**](StagingRule.md) | The list of staging rules that apply to a specific entity type. | 
## Example

```python
from lusid.models.create_staging_rule_set_request import CreateStagingRuleSetRequest
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

display_name: StrictStr = "example_display_name"
description: Optional[StrictStr] = "example_description"
rules: List[StagingRule] = # Replace with your value
create_staging_rule_set_request_instance = CreateStagingRuleSetRequest(display_name=display_name, description=description, rules=rules)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

