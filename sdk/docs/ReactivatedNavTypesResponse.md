# ReactivatedNavTypesResponse

The response from reactivating NAV types on a fund. Contains the updated fund and, for each  reactivated follower, the number of valuation points finalised while the follower was dormant.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**href** | **str** | The specific Uniform Resource Identifier (URI) for this resource at the requested effective and asAt datetime. | [optional] 
**fund** | [**Fund**](Fund.md) |  | 
**catch_up_counts** | [**List[NavTypeCatchUp]**](NavTypeCatchUp.md) | For each reactivated follower, the number of valuation points the leader finalised while the follower was dormant. Leaders are not included (they have no catch-up). | [optional] 
**links** | [**List[Link]**](Link.md) |  | [optional] 
## Example

```python
from lusid.models.reactivated_nav_types_response import ReactivatedNavTypesResponse
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

href: Optional[StrictStr] = "example_href"
fund: Fund
catch_up_counts: Optional[List[NavTypeCatchUp]] = # Replace with your value
links: Optional[List[Link]] = None
reactivated_nav_types_response_instance = ReactivatedNavTypesResponse(href=href, fund=fund, catch_up_counts=catch_up_counts, links=links)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

