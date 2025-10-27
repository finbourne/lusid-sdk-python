# TranslateTradeTicketsResponse

A response from a request to translate a collection of instruments to a given target dialect.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**href** | **str** | The specific Uniform Resource Identifier (URI) for this resource at the requested effective and asAt datetime. | [optional] 
**values** | [**Dict[str, TradeTicket]**](TradeTicket.md) | The instruments which have been successfully translated. | [optional] 
**failed** | [**Dict[str, ErrorDetail]**](ErrorDetail.md) | The instruments that could not be translated along with a reason for their failure. | [optional] 
**links** | [**List[Link]**](Link.md) |  | [optional] 
## Example

```python
from lusid.models.translate_trade_tickets_response import TranslateTradeTicketsResponse
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

href: Optional[StrictStr] = "example_href"
values: Optional[Dict[str, TradeTicket]] = # Replace with your value
failed: Optional[Dict[str, ErrorDetail]] = # Replace with your value
links: Optional[List[Link]] = None
translate_trade_tickets_response_instance = TranslateTradeTicketsResponse(href=href, values=values, failed=failed, links=links)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

