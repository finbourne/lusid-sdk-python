# UpdateAmortisationRuleSetDetailsRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**display_name** | **str** |  | 
**description** | **str** |  | [optional] 
## Example

```python
from lusid.models.update_amortisation_rule_set_details_request import UpdateAmortisationRuleSetDetailsRequest
from typing import Any, Dict, Optional
from pydantic.v1 import BaseModel, Field, constr, validator

display_name: StrictStr = "example_display_name"
description: Optional[StrictStr] = "example_description"
update_amortisation_rule_set_details_request_instance = UpdateAmortisationRuleSetDetailsRequest(display_name=display_name, description=description)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

