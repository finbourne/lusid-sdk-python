# CompletePortfolio

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | [**ResourceId**](ResourceId.md) |  | 
**href** | **str** | The specific Uniform Resource Identifier (URI) for this resource at the requested effective and asAt datetime. | [optional] 
**description** | **str** | The long form description of the portfolio. | [optional] 
**display_name** | **str** | The name of the portfolio. | [optional] 
**created** | **datetime** | The effective datetime at which the portfolio was created. No transactions or constituents can be added to the portfolio before this date. | [optional] 
**parent_portfolio_id** | [**ResourceId**](ResourceId.md) |  | [optional] 
**is_derived** | **bool** | Whether or not this is a derived portfolio. | [optional] [readonly] 
**type** | **str** | The type of the portfolio. The available values are: Transaction, Reference, DerivedTransaction, SimplePosition | [optional] 
**version** | [**Version**](Version.md) |  | 
**properties** | [**List[ModelProperty]**](ModelProperty.md) | The requested portfolio properties. These will be from the &#39;Portfolio&#39; domain. | [optional] 
**base_currency** | **str** | If the portfolio is a transaction portfolio or derived transaction portfolio, this is the base currency of the portfolio. | [optional] 
**sub_holding_keys** | **List[str]** | The sub holding key properties configured for the portfolio | [optional] 
**links** | [**List[Link]**](Link.md) |  | [optional] 
## Example

```python
from lusid.models.complete_portfolio import CompletePortfolio
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

id: ResourceId
href: Optional[StrictStr] = "example_href"
description: Optional[StrictStr] = "example_description"
display_name: Optional[StrictStr] = "example_display_name"
created: Optional[datetime] = # Replace with your value
parent_portfolio_id: Optional[ResourceId] = # Replace with your value
is_derived: Optional[StrictBool] = # Replace with your value
is_derived:Optional[StrictBool] = None
type: Optional[StrictStr] = "example_type"
version: Version
properties: Optional[List[ModelProperty]] = # Replace with your value
base_currency: Optional[StrictStr] = "example_base_currency"
sub_holding_keys: Optional[List[StrictStr]] = # Replace with your value
links: Optional[List[Link]] = None
complete_portfolio_instance = CompletePortfolio(id=id, href=href, description=description, display_name=display_name, created=created, parent_portfolio_id=parent_portfolio_id, is_derived=is_derived, type=type, version=version, properties=properties, base_currency=base_currency, sub_holding_keys=sub_holding_keys, links=links)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

