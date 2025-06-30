# GroupReconciliationComparisonRuleset

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | [**ResourceId**](ResourceId.md) |  | 
**display_name** | **str** | The name of the ruleset | 
**reconciliation_type** | **str** | The type of reconciliation to perform. \&quot;Holding\&quot; | \&quot;Transaction\&quot; | \&quot;Valuation\&quot; | 
**core_attribute_rules** | [**List[GroupReconciliationCoreAttributeRule]**](GroupReconciliationCoreAttributeRule.md) | The core comparison rules | 
**aggregate_attribute_rules** | [**List[GroupReconciliationAggregateAttributeRule]**](GroupReconciliationAggregateAttributeRule.md) | The aggregate comparison rules | 
**href** | **str** | The specific Uniform Resource Identifier (URI) for this resource at the requested effective and asAt datetime. | [optional] 
**version** | [**Version**](Version.md) |  | [optional] 
**links** | [**List[Link]**](Link.md) |  | [optional] 
## Example

```python
from lusid.models.group_reconciliation_comparison_ruleset import GroupReconciliationComparisonRuleset
from typing import Any, Dict, List, Optional
from pydantic.v1 import BaseModel, Field, StrictStr, conlist, constr

id: ResourceId = # Replace with your value
display_name: StrictStr = "example_display_name"
reconciliation_type: StrictStr = "example_reconciliation_type"
core_attribute_rules: conlist(GroupReconciliationCoreAttributeRule) = # Replace with your value
aggregate_attribute_rules: conlist(GroupReconciliationAggregateAttributeRule) = # Replace with your value
href: Optional[StrictStr] = "example_href"
version: Optional[Version] = None
links: Optional[conlist(Link)] = None
group_reconciliation_comparison_ruleset_instance = GroupReconciliationComparisonRuleset(id=id, display_name=display_name, reconciliation_type=reconciliation_type, core_attribute_rules=core_attribute_rules, aggregate_attribute_rules=aggregate_attribute_rules, href=href, version=version, links=links)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

