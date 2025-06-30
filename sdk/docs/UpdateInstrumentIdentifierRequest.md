# UpdateInstrumentIdentifierRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | The allowable instrument identifier to update, insert or remove e.g. &#39;Figi&#39;. | 
**value** | **str** | The new value of the allowable instrument identifier. If unspecified the identifier will be removed from the instrument. | [optional] 
**effective_at** | **str** | The effective datetime from which the identifier should be updated, inserted or removed. Defaults to the current LUSID system datetime if not specified. | [optional] 
## Example

```python
from lusid.models.update_instrument_identifier_request import UpdateInstrumentIdentifierRequest
from typing import Any, Dict, Optional
from pydantic.v1 import BaseModel, Field, StrictStr, constr

type: StrictStr = "example_type"
value: Optional[StrictStr] = "example_value"
effective_at: Optional[StrictStr] = "example_effective_at"
update_instrument_identifier_request_instance = UpdateInstrumentIdentifierRequest(type=type, value=value, effective_at=effective_at)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

