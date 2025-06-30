# SetShareClassInstrumentsRequest

The request used to create a Fund.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**share_class_instrument_scopes** | **List[str]** | The scopes in which the instruments lie, currently limited to one. | 
**share_class_instruments** | [**List[InstrumentResolutionDetail]**](InstrumentResolutionDetail.md) | Details the user-provided instrument identifiers and the instrument resolved from them. | 
## Example

```python
from lusid.models.set_share_class_instruments_request import SetShareClassInstrumentsRequest
from typing import Any, Dict, List
from pydantic.v1 import BaseModel, Field, StrictStr, conlist

share_class_instrument_scopes: conlist(StrictStr, max_items=1) = Field(..., alias="shareClassInstrumentScopes", description="The scopes in which the instruments lie, currently limited to one.")
share_class_instruments: conlist(InstrumentResolutionDetail) = # Replace with your value
set_share_class_instruments_request_instance = SetShareClassInstrumentsRequest(share_class_instrument_scopes=share_class_instrument_scopes, share_class_instruments=share_class_instruments)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

