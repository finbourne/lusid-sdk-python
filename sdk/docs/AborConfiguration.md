# AborConfiguration

An AborConfiguration entity.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**href** | **str** | The specific Uniform Resource Identifier (URI) for this resource at the requested effective and asAt datetime. | [optional] 
**id** | [**ResourceId**](ResourceId.md) |  | 
**display_name** | **str** | The name of the Abor Configuration. | [optional] 
**description** | **str** | A description for the Abor Configuration. | [optional] 
**recipe_id** | [**ResourceId**](ResourceId.md) |  | [optional] 
**chart_of_accounts_id** | [**ResourceId**](ResourceId.md) |  | 
**posting_module_codes** | **List[str]** | The Posting Module Codes from which the rules to be applied are retrieved. | [optional] 
**cleardown_module_codes** | **List[str]** | The Cleardown Module Codes from which the rules to be applied are retrieved. | [optional] 
**properties** | [**Dict[str, ModelProperty]**](ModelProperty.md) | A set of properties for the Abor Configuration. | [optional] 
**version** | [**Version**](Version.md) |  | [optional] 
**links** | [**List[Link]**](Link.md) |  | [optional] 
## Example

```python
from lusid.models.abor_configuration import AborConfiguration
from typing import Any, Dict, List, Optional
from pydantic.v1 import BaseModel, Field, StrictStr, conlist

href: Optional[StrictStr] = "example_href"
id: ResourceId = # Replace with your value
display_name: Optional[StrictStr] = "example_display_name"
description: Optional[StrictStr] = "example_description"
recipe_id: Optional[ResourceId] = # Replace with your value
chart_of_accounts_id: ResourceId = # Replace with your value
posting_module_codes: Optional[conlist(StrictStr)] = # Replace with your value
cleardown_module_codes: Optional[conlist(StrictStr)] = # Replace with your value
properties: Optional[Dict[str, ModelProperty]] = # Replace with your value
version: Optional[Version] = None
links: Optional[conlist(Link)] = None
abor_configuration_instance = AborConfiguration(href=href, id=id, display_name=display_name, description=description, recipe_id=recipe_id, chart_of_accounts_id=chart_of_accounts_id, posting_module_codes=posting_module_codes, cleardown_module_codes=cleardown_module_codes, properties=properties, version=version, links=links)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

