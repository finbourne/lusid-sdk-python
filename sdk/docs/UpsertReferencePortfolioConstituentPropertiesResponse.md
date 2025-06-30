# UpsertReferencePortfolioConstituentPropertiesResponse

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**href** | **str** | The specific Uniform Resource Identifier (URI) for this resource at the requested effective and asAt datetime. | [optional] 
**version** | [**Version**](Version.md) |  | [optional] 
**properties** | [**Dict[str, PerpetualProperty]**](PerpetualProperty.md) | The updated collection of properties of the constituent. | [optional] 
**links** | [**List[Link]**](Link.md) |  | [optional] 
## Example

```python
from lusid.models.upsert_reference_portfolio_constituent_properties_response import UpsertReferencePortfolioConstituentPropertiesResponse
from typing import Any, Dict, List, Optional
from pydantic.v1 import BaseModel, Field, StrictStr, conlist

href: Optional[StrictStr] = "example_href"
version: Optional[Version] = None
properties: Optional[Dict[str, PerpetualProperty]] = # Replace with your value
links: Optional[conlist(Link)] = None
upsert_reference_portfolio_constituent_properties_response_instance = UpsertReferencePortfolioConstituentPropertiesResponse(href=href, version=version, properties=properties, links=links)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

