# VersionedResourceListWithPostBodiesOfSettlementInstructionWithTransactionToSettlementInstructionQuery

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**version** | [**Version**](Version.md) |  | 
**values** | [**List[SettlementInstructionWithTransaction]**](SettlementInstructionWithTransaction.md) | The resources to list. | 
**href** | **str** | The URI of the resource list. | [optional] 
**post_body** | [**SettlementInstructionQuery**](SettlementInstructionQuery.md) |  | [optional] 
**next_page** | [**SettlementInstructionQuery**](SettlementInstructionQuery.md) |  | [optional] 
**previous_page** | [**SettlementInstructionQuery**](SettlementInstructionQuery.md) |  | [optional] 
**links** | [**List[Link]**](Link.md) |  | [optional] 
## Example

```python
from lusid.models.versioned_resource_list_with_post_bodies_of_settlement_instruction_with_transaction_to_settlement_instruction_query import VersionedResourceListWithPostBodiesOfSettlementInstructionWithTransactionToSettlementInstructionQuery
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

version: Version
values: List[SettlementInstructionWithTransaction] = # Replace with your value
href: Optional[StrictStr] = "example_href"
post_body: Optional[SettlementInstructionQuery] = # Replace with your value
next_page: Optional[SettlementInstructionQuery] = # Replace with your value
previous_page: Optional[SettlementInstructionQuery] = # Replace with your value
links: Optional[List[Link]] = None
versioned_resource_list_with_post_bodies_of_settlement_instruction_with_transaction_to_settlement_instruction_query_instance = VersionedResourceListWithPostBodiesOfSettlementInstructionWithTransactionToSettlementInstructionQuery(version=version, values=values, href=href, post_body=post_body, next_page=next_page, previous_page=previous_page, links=links)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

