# CheckDefinition

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | [**ResourceId**](ResourceId.md) |  | 
**display_name** | **str** | The name of the Check Definition. | [optional] 
**description** | **str** | A description for the Check Definition. | [optional] 
**dataset_schema** | [**CheckDefinitionDatasetSchema**](CheckDefinitionDatasetSchema.md) |  | [optional] 
**rule_sets** | [**List[CheckDefinitionRuleSet]**](CheckDefinitionRuleSet.md) | A collection of rule sets for the Check Definition. | [optional] 
**href** | **str** | The specific Uniform Resource Identifier (URI) for this resource at the requested effective and asAt datetime. | [optional] 
**version** | [**Version**](Version.md) |  | [optional] 
**properties** | [**Dict[str, ModelProperty]**](ModelProperty.md) | A set of properties for the Check Definition. | [optional] 
**links** | [**List[Link]**](Link.md) |  | [optional] 
## Example

```python
from lusid.models.check_definition import CheckDefinition
from typing import Any, Dict, List, Optional
from pydantic.v1 import BaseModel, Field, StrictStr, conlist, constr, validator

id: ResourceId = # Replace with your value
display_name: Optional[StrictStr] = "example_display_name"
description: Optional[StrictStr] = "example_description"
dataset_schema: Optional[CheckDefinitionDatasetSchema] = # Replace with your value
rule_sets: Optional[conlist(CheckDefinitionRuleSet)] = # Replace with your value
href: Optional[StrictStr] = "example_href"
version: Optional[Version] = None
properties: Optional[Dict[str, ModelProperty]] = # Replace with your value
links: Optional[conlist(Link)] = None
check_definition_instance = CheckDefinition(id=id, display_name=display_name, description=description, dataset_schema=dataset_schema, rule_sets=rule_sets, href=href, version=version, properties=properties, links=links)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

