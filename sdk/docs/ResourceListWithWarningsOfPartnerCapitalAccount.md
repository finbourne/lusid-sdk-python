# ResourceListWithWarningsOfPartnerCapitalAccount

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**values** | [**List[PartnerCapitalAccount]**](PartnerCapitalAccount.md) | The resources to list. | 
**href** | **str** | The URI of the resource list. | [optional] 
**next_page** | **str** | The next page of results. | [optional] 
**previous_page** | **str** | The previous page of results. | [optional] 
**warnings** | [**List[Warning]**](Warning.md) |  | [optional] 
**links** | [**List[Link]**](Link.md) |  | [optional] 
## Example

```python
from lusid.models.resource_list_with_warnings_of_partner_capital_account import ResourceListWithWarningsOfPartnerCapitalAccount
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

values: List[PartnerCapitalAccount] = # Replace with your value
href: Optional[StrictStr] = "example_href"
next_page: Optional[StrictStr] = "example_next_page"
previous_page: Optional[StrictStr] = "example_previous_page"
warnings: Optional[List[Warning]] = None
links: Optional[List[Link]] = None
resource_list_with_warnings_of_partner_capital_account_instance = ResourceListWithWarningsOfPartnerCapitalAccount(values=values, href=href, next_page=next_page, previous_page=previous_page, warnings=warnings, links=links)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

