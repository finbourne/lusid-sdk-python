# AmortisationRuleSet

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**href** | **str** | The specific Uniform Resource Identifier (URI) for this resource at the requested effective and asAt datetime. | [optional] 
**id** | [**ResourceId**](ResourceId.md) |  | 
**display_name** | **str** | A user-friendly name. | 
**description** | **str** | A description of what this rule set is for. | [optional] 
**rules_interval** | [**RulesInterval**](RulesInterval.md) |  | 
**version** | [**Version**](Version.md) |  | [optional] 
**links** | [**List[Link]**](Link.md) |  | [optional] 
## Example

```python
from lusid.models.amortisation_rule_set import AmortisationRuleSet
from typing import Any, Dict, List, Optional
from pydantic.v1 import BaseModel, Field, StrictStr, conlist, constr, validator

href: Optional[StrictStr] = "example_href"
id: ResourceId = # Replace with your value
display_name: StrictStr = "example_display_name"
description: Optional[StrictStr] = "example_description"
rules_interval: RulesInterval = # Replace with your value
version: Optional[Version] = None
links: Optional[conlist(Link)] = None
amortisation_rule_set_instance = AmortisationRuleSet(href=href, id=id, display_name=display_name, description=description, rules_interval=rules_interval, version=version, links=links)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

