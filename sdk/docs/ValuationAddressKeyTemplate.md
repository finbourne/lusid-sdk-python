# ValuationAddressKeyTemplate

A set of valuation metrics and grouping keys. Funds and NAV Types reference a template by its id.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**href** | **str** | The specific Uniform Resource Identifier (URI) for this resource at the requested effective and asAt datetime. | [optional] 
**id** | [**ResourceId**](ResourceId.md) |  | 
**display_name** | **str** | The name of the Valuation Template. | [optional] 
**description** | **str** | A description of the Valuation Template. | [optional] 
**metrics** | [**List[AggregateSpec]**](AggregateSpec.md) | The metrics to calculate in a valuation that uses this template. Each metric is an address key, an operation and optional key options. Valuation Templates do not support returnAs. | [optional] 
**is_default** | **bool** | True if this is the default Valuation Template, which applies when neither the Fund nor the NAV Type references a template. A domain has one default. Set isDefault on UpsertValuationAddressKeyTemplate to change it. | [optional] 
**version** | [**Version**](Version.md) |  | [optional] 
**links** | [**List[Link]**](Link.md) |  | [optional] 
## Example

```python
from lusid.models.valuation_address_key_template import ValuationAddressKeyTemplate
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

href: Optional[StrictStr] = "example_href"
id: ResourceId
display_name: Optional[StrictStr] = "example_display_name"
description: Optional[StrictStr] = "example_description"
metrics: Optional[List[AggregateSpec]] = # Replace with your value
is_default: Optional[StrictBool] = # Replace with your value
is_default:Optional[StrictBool] = None
version: Optional[Version] = None
links: Optional[List[Link]] = None
valuation_address_key_template_instance = ValuationAddressKeyTemplate(href=href, id=id, display_name=display_name, description=description, metrics=metrics, is_default=is_default, version=version, links=links)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

