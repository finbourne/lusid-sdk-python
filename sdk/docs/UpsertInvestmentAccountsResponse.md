# UpsertInvestmentAccountsResponse

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**href** | **str** | The specific Uniform Resource Identifier (URI) for this resource at the requested effective and asAt datetime. | [optional] 
**values** | [**Dict[str, InvestmentAccount]**](InvestmentAccount.md) | The investment accounts which have been successfully updated or created. | [optional] 
**failed** | [**Dict[str, ErrorDetail]**](ErrorDetail.md) | The investment accounts that could not be updated or created or were left unchanged without error along with a reason for their failure. | [optional] 
**links** | [**List[Link]**](Link.md) |  | [optional] 
## Example

```python
from lusid.models.upsert_investment_accounts_response import UpsertInvestmentAccountsResponse
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

href: Optional[StrictStr] = "example_href"
values: Optional[Dict[str, InvestmentAccount]] = # Replace with your value
failed: Optional[Dict[str, ErrorDetail]] = # Replace with your value
links: Optional[List[Link]] = None
upsert_investment_accounts_response_instance = UpsertInvestmentAccountsResponse(href=href, values=values, failed=failed, links=links)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

