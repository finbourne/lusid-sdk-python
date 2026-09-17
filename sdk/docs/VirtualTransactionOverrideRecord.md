# VirtualTransactionOverrideRecord

The overrides and suppressions stored against a single instrument event in a single portfolio, together  with their statuses as resolved against the requested portfolio's currently generated virtual  transactions.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**instrument_event_id** | **str** | The identifier of the instrument event this record is stored against. | [optional] 
**source_portfolio_id** | [**ResourceId**](ResourceId.md) |  | [optional] 
**overrides** | [**Dict[str, OverrideEntryResponse]**](OverrideEntryResponse.md) | The overrides stored in this record, keyed by the virtual transaction id being overridden as it appears in the portfolio holding the record. | [optional] 
**suppressions** | [**Dict[str, SuppressionEntryResponse]**](SuppressionEntryResponse.md) | The suppressions stored in this record, keyed by the virtual transaction id being suppressed as it appears in the portfolio holding the record. | [optional] 
**override_match_status** | **str** | Whether every override and suppression entry in this record still matches a virtual transaction the event currently generates. Available values: Matched, Orphaned. | [optional] 
**override_application_status** | **str** | Whether all, some, or none of this record&#39;s override and suppression entries are currently applied. Available values: Full, Partial, Orphaned. | [optional] 
**cancel_active** | **bool** | True when an active event-level Cancel instruction also exists for this instrument event, taking precedence over the entries in this record. | [optional] 
**version** | [**Version**](Version.md) |  | [optional] 
## Example

```python
from lusid.models.virtual_transaction_override_record import VirtualTransactionOverrideRecord
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

instrument_event_id: Optional[StrictStr] = "example_instrument_event_id"
source_portfolio_id: Optional[ResourceId] = # Replace with your value
overrides: Optional[Dict[str, OverrideEntryResponse]] = # Replace with your value
suppressions: Optional[Dict[str, SuppressionEntryResponse]] = # Replace with your value
override_match_status: Optional[StrictStr] = "example_override_match_status"
override_application_status: Optional[StrictStr] = "example_override_application_status"
cancel_active: Optional[StrictBool] = # Replace with your value
cancel_active:Optional[StrictBool] = None
version: Optional[Version] = None
virtual_transaction_override_record_instance = VirtualTransactionOverrideRecord(instrument_event_id=instrument_event_id, source_portfolio_id=source_portfolio_id, overrides=overrides, suppressions=suppressions, override_match_status=override_match_status, override_application_status=override_application_status, cancel_active=cancel_active, version=version)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

