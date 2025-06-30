# UpdateStagingRuleSetRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**display_name** | **str** | The name of the staging rule set. | 
**description** | **str** | A description for the staging rule set. | [optional] 
**rules** | [**List[StagingRule]**](StagingRule.md) | The list of staging rules that apply to a specific entity type. | 
## Example

```python
from lusid.models.update_staging_rule_set_request import UpdateStagingRuleSetRequest
from typing import Any, Dict, List, Optional
from pydantic.v1 import BaseModel, Field, conlist, constr

display_name: StrictStr = "example_display_name"
description: Optional[StrictStr] = "example_description"
rules: conlist(StagingRule) = # Replace with your value
update_staging_rule_set_request_instance = UpdateStagingRuleSetRequest(display_name=display_name, description=description, rules=rules)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

