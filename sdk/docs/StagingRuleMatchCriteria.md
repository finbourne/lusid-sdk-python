# StagingRuleMatchCriteria

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action_in** | **List[str]** |  | [optional] 
**requesting_user** | **str** |  | [optional] 
**entity_attributes** | **str** |  | [optional] 
**changed_attribute_name_in** | **List[str]** |  | [optional] 
## Example

```python
from lusid.models.staging_rule_match_criteria import StagingRuleMatchCriteria
from typing import Any, Dict, List, Optional
from pydantic.v1 import BaseModel, Field, StrictStr, conlist, constr

action_in: Optional[conlist(StrictStr)] = # Replace with your value
requesting_user: Optional[StrictStr] = "example_requesting_user"
entity_attributes: Optional[StrictStr] = "example_entity_attributes"
changed_attribute_name_in: Optional[conlist(StrictStr)] = # Replace with your value
staging_rule_match_criteria_instance = StagingRuleMatchCriteria(action_in=action_in, requesting_user=requesting_user, entity_attributes=entity_attributes, changed_attribute_name_in=changed_attribute_name_in)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

