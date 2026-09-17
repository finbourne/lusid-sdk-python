# UpsertVirtualTransactionOverrideResponse

The result of upserting overrides and suppressions of virtual transactions for a single instrument event.  Returns the record as it was persisted and the new version of the record. Whether each entry currently  applies, and which virtual transactions the event still generates unmodified.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**version** | [**Version**](Version.md) |  | 
**href** | **str** | The specific Uniform Resource Identifier (URI) for this resource at the requested effective and asAt datetime. | [optional] 
**metadata** | **Dict[str, Optional[List[ResponseMetaData]]]** | Contains warnings related to unresolved instruments, non-existent transaction types, sub-holding key mismatches, or closed accounting periods for the override transactions. | [optional] 
**instrument_event_id** | **str** | The identifier of the instrument event that was overridden. | 
**overrides** | **Dict[str, Optional[List[StoredOverrideDefinition]]]** | The replacement transactions persisted for the instrument event, keyed by the virtual transaction id being overridden. | [optional] 
**suppressions** | **List[str]** | The virtual transaction ids suppressed for the instrument event. | [optional] 
**cancel_active** | **bool** | True when an active event-level Cancel instruction also exists for this instrument event, taking precedence over the entries in this record. | [optional] 
**links** | [**List[Link]**](Link.md) |  | [optional] 
## Example

```python
from lusid.models.upsert_virtual_transaction_override_response import UpsertVirtualTransactionOverrideResponse
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

version: Version
href: Optional[StrictStr] = "example_href"
metadata: Optional[Dict[str, Optional[List[ResponseMetaData]]]] = # Replace with your value
instrument_event_id: StrictStr = "example_instrument_event_id"
overrides: Optional[Dict[str, Optional[List[StoredOverrideDefinition]]]] = # Replace with your value
suppressions: Optional[List[StrictStr]] = # Replace with your value
cancel_active: Optional[StrictBool] = # Replace with your value
cancel_active:Optional[StrictBool] = None
links: Optional[List[Link]] = None
upsert_virtual_transaction_override_response_instance = UpsertVirtualTransactionOverrideResponse(version=version, href=href, metadata=metadata, instrument_event_id=instrument_event_id, overrides=overrides, suppressions=suppressions, cancel_active=cancel_active, links=links)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

