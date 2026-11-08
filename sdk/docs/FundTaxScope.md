# FundTaxScope

The UK chargeable-gains tax scope of a fund at a point in time: the portfolios inside the regime and what the  regime's figures leave out.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**href** | **str** | The specific Uniform Resource Identifier (URI) for this resource at the requested effective and asAt datetime. | [optional] 
**portfolios** | [**List[ResourceId]**](ResourceId.md) | The portfolios within the UK chargeable-gains regime. A fund portfolio is in scope when its own details elect the regime. A NAV type that elects the regime puts its derived portfolio for each fund portfolio in scope. | 
**exclusions** | [**FundTaxScopeExclusions**](FundTaxScopeExclusions.md) |  | 
**effective_at** | **datetime** | The effective datetime at which the tax scope was read. | 
**as_at** | **datetime** | The asAt datetime at which the tax scope was read. | 
**links** | [**List[Link]**](Link.md) |  | [optional] 
## Example

```python
from lusid.models.fund_tax_scope import FundTaxScope
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

href: Optional[StrictStr] = "example_href"
portfolios: List[ResourceId] = # Replace with your value
exclusions: FundTaxScopeExclusions
effective_at: datetime = # Replace with your value
as_at: datetime = # Replace with your value
links: Optional[List[Link]] = None
fund_tax_scope_instance = FundTaxScope(href=href, portfolios=portfolios, exclusions=exclusions, effective_at=effective_at, as_at=as_at, links=links)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

