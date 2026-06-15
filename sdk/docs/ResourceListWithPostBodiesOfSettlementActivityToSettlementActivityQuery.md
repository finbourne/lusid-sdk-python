# ResourceListWithPostBodiesOfSettlementActivityToSettlementActivityQuery

A version of the resource list for use with list endpoints that use the POST verb instead of GET, allowing  the endpoint to return the POST body(s) that can be sent in conjunction with the Next Page and/or Previous  Page links to retrieve the next/previous page of results. This should make it easier for SDK consumers to  fluently page through results. The PagedResourceList only exposes a page token string, typically for use in  a query parameter, and thus is more suited to GET endpoints.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**values** | [**List[SettlementActivity]**](SettlementActivity.md) | The resources to list. | 
**href** | **str** | The URI of the resource list. | [optional] 
**post_body** | [**SettlementActivityQuery**](SettlementActivityQuery.md) |  | [optional] 
**next_page** | [**SettlementActivityQuery**](SettlementActivityQuery.md) |  | [optional] 
**previous_page** | [**SettlementActivityQuery**](SettlementActivityQuery.md) |  | [optional] 
**links** | [**List[Link]**](Link.md) |  | [optional] 
## Example

```python
from lusid.models.resource_list_with_post_bodies_of_settlement_activity_to_settlement_activity_query import ResourceListWithPostBodiesOfSettlementActivityToSettlementActivityQuery
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

values: List[SettlementActivity] = # Replace with your value
href: Optional[StrictStr] = "example_href"
post_body: Optional[SettlementActivityQuery] = # Replace with your value
next_page: Optional[SettlementActivityQuery] = # Replace with your value
previous_page: Optional[SettlementActivityQuery] = # Replace with your value
links: Optional[List[Link]] = None
resource_list_with_post_bodies_of_settlement_activity_to_settlement_activity_query_instance = ResourceListWithPostBodiesOfSettlementActivityToSettlementActivityQuery(values=values, href=href, post_body=post_body, next_page=next_page, previous_page=previous_page, links=links)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

