# TransactionEntity

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**href** | **str** | The link to the transaction entity. | 
**entity_unique_id** | **str** | The unique id of the transaction, combining the portfolio and transaction identifiers. | 
**as_at_version_number** | **int** | The version number of the transaction entity at the requested asAt. | [optional] 
**status** | **str** | The status of the transaction entity. &#39;Prevailing&#39; when the transaction exists — including a cancelled transaction, whose cancellation is reflected in its own status rather than here; &#39;Deleted&#39; when the transaction&#39;s portfolio has been deleted; &#39;DoesNotExist&#39; when the transaction does not yet exist (e.g. staged creation preview). Available values: Prevailing, Deleted, DoesNotExist. | 
**as_at_deleted** | **datetime** | The asAt datetime at which the portfolio (and by extension, the transaction) was deleted. | [optional] 
**user_id_deleted** | **str** | The unique id of the user who deleted the portfolio. | [optional] 
**request_id_deleted** | **str** | The unique request id of the command that deleted the portfolio. | [optional] 
**prevailing_portfolio** | [**PortfolioWithoutHref**](PortfolioWithoutHref.md) |  | [optional] 
**prevailing_input_transaction** | [**Transaction**](Transaction.md) |  | [optional] 
**deleted_portfolio** | [**PortfolioWithoutHref**](PortfolioWithoutHref.md) |  | [optional] 
**deleted_input_transaction** | [**Transaction**](Transaction.md) |  | [optional] 
**previewed_status** | **str** | The status of the transaction after the staged modification is applied. Always &#39;Prevailing&#39; for transaction previews. Available values: Prevailing, Deleted, DoesNotExist. | [optional] 
**previewed_portfolio** | [**PortfolioWithoutHref**](PortfolioWithoutHref.md) |  | [optional] 
**previewed_input_transaction** | [**Transaction**](Transaction.md) |  | [optional] 
**links** | [**List[Link]**](Link.md) |  | [optional] 
## Example

```python
from lusid.models.transaction_entity import TransactionEntity
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

href: StrictStr = "example_href"
entity_unique_id: StrictStr = "example_entity_unique_id"
as_at_version_number: Optional[StrictInt] = # Replace with your value
as_at_version_number: Optional[StrictInt] = None
status: StrictStr = "example_status"
as_at_deleted: Optional[datetime] = # Replace with your value
user_id_deleted: Optional[StrictStr] = "example_user_id_deleted"
request_id_deleted: Optional[StrictStr] = "example_request_id_deleted"
prevailing_portfolio: Optional[PortfolioWithoutHref] = # Replace with your value
prevailing_input_transaction: Optional[Transaction] = # Replace with your value
deleted_portfolio: Optional[PortfolioWithoutHref] = # Replace with your value
deleted_input_transaction: Optional[Transaction] = # Replace with your value
previewed_status: Optional[StrictStr] = "example_previewed_status"
previewed_portfolio: Optional[PortfolioWithoutHref] = # Replace with your value
previewed_input_transaction: Optional[Transaction] = # Replace with your value
links: Optional[List[Link]] = None
transaction_entity_instance = TransactionEntity(href=href, entity_unique_id=entity_unique_id, as_at_version_number=as_at_version_number, status=status, as_at_deleted=as_at_deleted, user_id_deleted=user_id_deleted, request_id_deleted=request_id_deleted, prevailing_portfolio=prevailing_portfolio, prevailing_input_transaction=prevailing_input_transaction, deleted_portfolio=deleted_portfolio, deleted_input_transaction=deleted_input_transaction, previewed_status=previewed_status, previewed_portfolio=previewed_portfolio, previewed_input_transaction=previewed_input_transaction, links=links)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

