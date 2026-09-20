# CurrencyGroupResponse

A currency group: a set of related currencies sharing a major unit (e.g. GBP with minor unit GBX at 100:1).
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** | The code of the currency group. This uniquely identifies the currency group within the tenant. | [optional] 
**display_name** | **str** | The name of the currency group. | [optional] 
**description** | **str** | A description for the currency group. | [optional] 
**major_unit_currency** | **str** | The three to five letter, case-sensitive currency code of the group&#39;s major unit, e.g. GBP for the sterling group. | [optional] 
**circulation_domain** | **List[str]** | The domains in which the group&#39;s currencies circulate, e.g. ISO 3166 country codes or the ISO 4217 entity names of the countries using the major unit. | [optional] 
**minor_units** | [**List[CurrencyGroupMinorUnit]**](CurrencyGroupMinorUnit.md) | The minor unit currencies belonging to this currency group. | [optional] 
**version** | [**Version**](Version.md) |  | [optional] 
**href** | **str** | The specific Uniform Resource Identifier (URI) for this resource. | [optional] 
**links** | [**List[Link]**](Link.md) |  | [optional] 
## Example

```python
from lusid.models.currency_group_response import CurrencyGroupResponse
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

code: Optional[StrictStr] = "example_code"
display_name: Optional[StrictStr] = "example_display_name"
description: Optional[StrictStr] = "example_description"
major_unit_currency: Optional[StrictStr] = "example_major_unit_currency"
circulation_domain: Optional[List[StrictStr]] = # Replace with your value
minor_units: Optional[List[CurrencyGroupMinorUnit]] = # Replace with your value
version: Optional[Version] = None
href: Optional[StrictStr] = "example_href"
links: Optional[List[Link]] = None
currency_group_response_instance = CurrencyGroupResponse(code=code, display_name=display_name, description=description, major_unit_currency=major_unit_currency, circulation_domain=circulation_domain, minor_units=minor_units, version=version, href=href, links=links)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

