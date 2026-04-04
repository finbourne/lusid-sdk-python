# OverrideVirtualTransactionsResponse

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**version** | [**Version**](Version.md) |  | 
**href** | **str** | The specific Uniform Resource Identifier (URI) for this resource at the requested effective and asAt datetime. | [optional] 
**metadata** | **Dict[str, Optional[List[ResponseMetaData]]]** | Contains warnings related to unresolved instruments or non-existent transaction types for the override transactions. | [optional] 
**instrument_event_id** | **str** | The identifier of the instrument event that was overridden. | 
**cancel_instruction_id** | **str** | The identifier of the cancel instruction that was created for the overridden instrument event. | 
**links** | [**List[Link]**](Link.md) |  | [optional] 
## Example

```python
from lusid.models.override_virtual_transactions_response import OverrideVirtualTransactionsResponse
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

version: Version
href: Optional[StrictStr] = "example_href"
metadata: Optional[Dict[str, Optional[List[ResponseMetaData]]]] = # Replace with your value
instrument_event_id: StrictStr = "example_instrument_event_id"
cancel_instruction_id: StrictStr = "example_cancel_instruction_id"
links: Optional[List[Link]] = None
override_virtual_transactions_response_instance = OverrideVirtualTransactionsResponse(version=version, href=href, metadata=metadata, instrument_event_id=instrument_event_id, cancel_instruction_id=cancel_instruction_id, links=links)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

