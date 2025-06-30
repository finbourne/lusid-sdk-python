# CreateAmortisationRuleSetRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** |  | 
**display_name** | **str** |  | 
**description** | **str** |  | [optional] 
## Example

```python
from lusid.models.create_amortisation_rule_set_request import CreateAmortisationRuleSetRequest
from typing import Any, Dict, Optional
from pydantic.v1 import BaseModel, Field, constr, validator

code: StrictStr = "example_code"
display_name: StrictStr = "example_display_name"
description: Optional[StrictStr] = "example_description"
create_amortisation_rule_set_request_instance = CreateAmortisationRuleSetRequest(code=code, display_name=display_name, description=description)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

