# StagingRuleSet

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**entity_type** | **str** | The entity type the staging rule set applies to. | 
**staging_rule_set_id** | **str** | System generated unique id for the staging rule set. | 
**display_name** | **str** | The name of the staging rule set. | 
**description** | **str** | A description for the staging rule set. | [optional] 
**rules** | [**List[StagingRule]**](StagingRule.md) | The list of staging rules that apply to a specific entity type. | 
**href** | **str** | The specific Uniform Resource Identifier (URI) for this resource at the requested effective and asAt datetime. | [optional] 
**version** | [**Version**](Version.md) |  | [optional] 
**links** | [**List[Link]**](Link.md) |  | [optional] 
## Example

```python
from lusid.models.staging_rule_set import StagingRuleSet
from typing import Any, Dict, List, Optional
from pydantic.v1 import BaseModel, Field, StrictStr, conlist, constr

entity_type: StrictStr = "example_entity_type"
staging_rule_set_id: StrictStr = "example_staging_rule_set_id"
display_name: StrictStr = "example_display_name"
description: Optional[StrictStr] = "example_description"
rules: conlist(StagingRule) = # Replace with your value
href: Optional[StrictStr] = "example_href"
version: Optional[Version] = None
links: Optional[conlist(Link)] = None
staging_rule_set_instance = StagingRuleSet(entity_type=entity_type, staging_rule_set_id=staging_rule_set_id, display_name=display_name, description=description, rules=rules, href=href, version=version, links=links)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

