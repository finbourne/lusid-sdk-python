# Transfer

A transfer and both of the transactions it booked.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**transfer_id** | [**ResourceId**](ResourceId.md) |  | [optional] 
**transfer_type** | **str** | The derived type of the transfer: &#39;Transfer&#39; when the position moves between portfolios, &#39;Switch&#39; when one instrument is exchanged for another within a portfolio, and &#39;Twitch&#39; when the position moves between portfolios and changes instrument at the same time. | [optional] 
**portfolio_id_out** | [**ResourceId**](ResourceId.md) |  | [optional] 
**portfolio_id_in** | [**ResourceId**](ResourceId.md) |  | [optional] 
**pricing_method** | **str** | How the legs were priced: &#39;AtCost&#39; or &#39;AtPrice&#39;. | [optional] 
**tax_lot_structure** | **str** | What happened to the tax lots of the outgoing position: &#39;Consolidate&#39; or &#39;Preserve&#39;. | [optional] 
**weight_out** | **float** | The weighting factor recorded against the outgoing leg. | [optional] 
**accounting_method** | **str** | The accounting method recorded against the transfer. | [optional] 
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
pricing_method: Optional[StrictStr] = "example_pricing_method"
tax_lot_structure: Optional[StrictStr] = "example_tax_lot_structure"
weight_out: Optional[Union[StrictFloat, StrictInt]] = # Replace with your value
accounting_method: Optional[StrictStr] = "example_accounting_method"
transaction_out: Optional[Transaction] = # Replace with your value
transaction_in: Optional[Transaction] = # Replace with your value
properties: Optional[Dict[str, ModelProperty]] = # Replace with your value
href: Optional[StrictStr] = "example_href"
version: Optional[Version] = None
links: Optional[List[Link]] = None
transfer_instance = Transfer(transfer_id=transfer_id, transfer_type=transfer_type, portfolio_id_out=portfolio_id_out, portfolio_id_in=portfolio_id_in, pricing_method=pricing_method, tax_lot_structure=tax_lot_structure, weight_out=weight_out, accounting_method=accounting_method, transaction_out=transaction_out, transaction_in=transaction_in, properties=properties, href=href, version=version, links=links)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

