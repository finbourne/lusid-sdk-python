# Transfer

A transfer and both of the transactions it booked.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**transfer_id** | [**ResourceId**](ResourceId.md) |  | [optional] 
**transfer_type** | **str** | The derived type of the transfer: &#39;Transfer&#39; when the position moves between portfolios, &#39;Switch&#39; when one instrument is exchanged for another within a portfolio, and &#39;Twitch&#39; when the position moves between portfolios and changes instrument at the same time. | [optional] 
**portfolio_id_out** | [**ResourceId**](ResourceId.md) |  | [optional] 
**portfolio_id_in** | [**ResourceId**](ResourceId.md) |  | [optional] 
**transaction_out** | [**Transaction**](Transaction.md) |  | [optional] 
**transaction_in** | [**Transaction**](Transaction.md) |  | [optional] 
**properties** | [**Dict[str, ModelProperty]**](ModelProperty.md) | The properties of the transfer, for the requested PropertyKeys. | [optional] 
**href** | **str** | The specifc Uniform Resource Identifier (URI) for this resource at the requested effective and asAt datetime. | [optional] 
**version** | [**Version**](Version.md) |  | [optional] 
**links** | [**List[Link]**](Link.md) |  | [optional] 
## Example

```python
from lusid.models.transfer import Transfer
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

transfer_id: Optional[ResourceId] = # Replace with your value
transfer_type: Optional[StrictStr] = "example_transfer_type"
portfolio_id_out: Optional[ResourceId] = # Replace with your value
portfolio_id_in: Optional[ResourceId] = # Replace with your value
transaction_out: Optional[Transaction] = # Replace with your value
transaction_in: Optional[Transaction] = # Replace with your value
properties: Optional[Dict[str, ModelProperty]] = # Replace with your value
href: Optional[StrictStr] = "example_href"
version: Optional[Version] = None
links: Optional[List[Link]] = None
transfer_instance = Transfer(transfer_id=transfer_id, transfer_type=transfer_type, portfolio_id_out=portfolio_id_out, portfolio_id_in=portfolio_id_in, transaction_out=transaction_out, transaction_in=transaction_in, properties=properties, href=href, version=version, links=links)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

