# VirtualTransactionOverridesResponse

The overrides and suppressions affecting a single instrument event in the requested portfolio. A derived  portfolio is affected by its own record and by every record held by an ancestor, so one record per  holding portfolio is returned, nearest first.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**version** | [**Version**](Version.md) |  | 
**href** | **str** | The specific Uniform Resource Identifier (URI) for this resource at the requested effective and asAt datetime. | [optional] 
**instrument_event_id** | **str** | The identifier of the instrument event whose overrides and suppressions are returned. | 
**records** | [**List[VirtualTransactionOverrideRecord]**](VirtualTransactionOverrideRecord.md) | The override and suppression records affecting the requested portfolio for this instrument event, nearest first. A derived portfolio is affected by its own record and by every record held by an ancestor. | [optional] 
**live** | **List[str]** | The virtual transaction ids the event currently generates in the requested portfolio that no returned record targets, and so keep generating unmodified. | [optional] 
**links** | [**List[Link]**](Link.md) |  | [optional] 
## Example

```python
from lusid.models.virtual_transaction_overrides_response import VirtualTransactionOverridesResponse
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

version: Version
href: Optional[StrictStr] = "example_href"
instrument_event_id: StrictStr = "example_instrument_event_id"
records: Optional[List[VirtualTransactionOverrideRecord]] = # Replace with your value
live: Optional[List[StrictStr]] = # Replace with your value
links: Optional[List[Link]] = None
virtual_transaction_overrides_response_instance = VirtualTransactionOverridesResponse(version=version, href=href, instrument_event_id=instrument_event_id, records=records, live=live, links=links)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

