# OverrideEntryResponse

A single overrides entry on a virtual transaction override record: the replacement transaction(s) that  stand in for the overridden virtual transaction, plus its status and diagnostics.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**replacements** | [**List[OverrideDefinitionResponse]**](OverrideDefinitionResponse.md) | The replacement transactions that stand in for the overridden virtual transaction. | [optional] 
**status** | **str** | Whether this entry&#39;s target virtual transaction id still matches one the event currently generates. Available values: Applied, Orphaned, Superseded. | [optional] 
**virtual_transaction_id** | **str** | The id of the virtual transaction this entry targets, as it appears in the requested portfolio. Null when the entry targets no virtual transaction the requested portfolio currently generates. | [optional] 
## Example

```python
from lusid.models.override_entry_response import OverrideEntryResponse
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

replacements: Optional[List[OverrideDefinitionResponse]] = # Replace with your value
status: Optional[StrictStr] = "example_status"
virtual_transaction_id: Optional[StrictStr] = "example_virtual_transaction_id"
override_entry_response_instance = OverrideEntryResponse(replacements=replacements, status=status, virtual_transaction_id=virtual_transaction_id)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

