# PortfolioEntity

A list of portfolios.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**href** | **str** | The specific Uniform Resource Identifier (URI) for this resource at the requested effective and asAt datetime. | 
**entity_unique_id** | **str** | The unique id of the entity. | 
**as_at_version_number** | **int** | The integer version number for the entity (the entity was created at version 1) | [optional] 
**status** | **str** | The status of the entity at the current time. | 
**as_at_deleted** | **datetime** | The asAt datetime at which the entity was deleted. | [optional] 
**user_id_deleted** | **str** | The unique id of the user who deleted the entity. | [optional] 
**request_id_deleted** | **str** | The unique request id of the command that deleted the entity. | [optional] 
**effective_at_created** | **datetime** | The EffectiveAt this Entity is created, if entity does not currently exist in EffectiveAt. | [optional] 
**prevailing_portfolio** | [**PortfolioWithoutHref**](PortfolioWithoutHref.md) |  | [optional] 
**deleted_portfolio** | [**PortfolioWithoutHref**](PortfolioWithoutHref.md) |  | [optional] 
**previewed_status** | **str** | The status of the previewed entity. | [optional] 
**previewed_portfolio** | [**PortfolioWithoutHref**](PortfolioWithoutHref.md) |  | [optional] 
**links** | [**List[Link]**](Link.md) |  | [optional] 
## Example

```python
from lusid.models.portfolio_entity import PortfolioEntity
from typing import Any, Dict, List, Optional
from pydantic.v1 import BaseModel, Field, StrictInt, StrictStr, conlist, constr
from datetime import datetime
href: StrictStr = "example_href"
entity_unique_id: StrictStr = "example_entity_unique_id"
as_at_version_number: Optional[StrictInt] = # Replace with your value
as_at_version_number: Optional[StrictInt] = None
status: StrictStr = "example_status"
as_at_deleted: Optional[datetime] = # Replace with your value
user_id_deleted: Optional[StrictStr] = "example_user_id_deleted"
request_id_deleted: Optional[StrictStr] = "example_request_id_deleted"
effective_at_created: Optional[datetime] = # Replace with your value
prevailing_portfolio: Optional[PortfolioWithoutHref] = # Replace with your value
deleted_portfolio: Optional[PortfolioWithoutHref] = # Replace with your value
previewed_status: Optional[StrictStr] = "example_previewed_status"
previewed_portfolio: Optional[PortfolioWithoutHref] = # Replace with your value
links: Optional[conlist(Link)] = None
portfolio_entity_instance = PortfolioEntity(href=href, entity_unique_id=entity_unique_id, as_at_version_number=as_at_version_number, status=status, as_at_deleted=as_at_deleted, user_id_deleted=user_id_deleted, request_id_deleted=request_id_deleted, effective_at_created=effective_at_created, prevailing_portfolio=prevailing_portfolio, deleted_portfolio=deleted_portfolio, previewed_status=previewed_status, previewed_portfolio=previewed_portfolio, links=links)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

