# ChartOfAccounts

A chart of account.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**href** | **str** | The specific Uniform Resource Identifier (URI) for this resource at the requested effective and asAt datetime. | [optional] 
**id** | [**ResourceId**](ResourceId.md) |  | 
**display_name** | **str** | The name of the Chart of Account. | [optional] 
**description** | **str** | A description of the Chart of Accounts. | [optional] 
**properties** | [**Dict[str, ModelProperty]**](ModelProperty.md) | A set of properties for the Chart of Accounts. | [optional] 
**version** | [**Version**](Version.md) |  | [optional] 
**links** | [**List[Link]**](Link.md) |  | [optional] 
## Example

```python
from lusid.models.chart_of_accounts import ChartOfAccounts
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

href: Optional[StrictStr] = "example_href"
id: ResourceId
display_name: Optional[StrictStr] = "example_display_name"
description: Optional[StrictStr] = "example_description"
properties: Optional[Dict[str, ModelProperty]] = # Replace with your value
version: Optional[Version] = None
links: Optional[List[Link]] = None
chart_of_accounts_instance = ChartOfAccounts(href=href, id=id, display_name=display_name, description=description, properties=properties, version=version, links=links)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

