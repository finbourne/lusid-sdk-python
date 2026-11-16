# DeemedDisposalDefinition

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**href** | **str** | The specific Uniform Resource Identifier (URI) for this resource at the requested effective and asAt datetime. | [optional] 
**id** | [**ResourceId**](ResourceId.md) |  | 
**display_name** | **str** | The name of the deemed disposal definition. | 
**description** | **str** | The description of the deemed disposal definition. | [optional] 
**filter** | **str** | Selects the holdings the definition deems disposed of and re-acquired at market value at a valuation point. Written in the holding filter grammar of the portfolio cash flow endpoints (holdingType, holdingTypeName, instrumentUid, instrumentScope, units, settledUnits, unsettledUnits, overdueUnits, currentFace, cost.amount, cost.currency, costPortfolioCcy.amount, custodianAccountId, custodianAccount, subHoldingKeys[...] and properties[...]), for example \&quot;holdingType eq &#39;B&#39; and cost.currency eq &#39;USD&#39;\&quot;, with the additional system field &#39;InNavTypeBaseCurrency&#39; (true when the holding is in the NAV type&#39;s base currency). The GetHoldings fields &#39;currency&#39; and &#39;transaction&#39; are not accepted. | 
**version** | [**Version**](Version.md) |  | [optional] 
**links** | [**List[Link]**](Link.md) |  | [optional] 
## Example

```python
from lusid.models.deemed_disposal_definition import DeemedDisposalDefinition
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

href: Optional[StrictStr] = "example_href"
id: ResourceId
display_name: StrictStr = "example_display_name"
description: Optional[StrictStr] = "example_description"
filter: StrictStr = "example_filter"
version: Optional[Version] = None
links: Optional[List[Link]] = None
deemed_disposal_definition_instance = DeemedDisposalDefinition(href=href, id=id, display_name=display_name, description=description, filter=filter, version=version, links=links)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

