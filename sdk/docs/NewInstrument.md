# NewInstrument

Set of identifiers of an existing instrument that will be the subject or distribution of a corporate action.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**instrument_identifiers** | **Dict[str, Optional[str]]** | Unique instrument identifiers. | 
**lusid_instrument_id** | **str** | LUSID&#39;s internal unique instrument identifier, resolved from the instrument identifiers. | [optional] [readonly] 
**instrument_scope** | **str** | The scope in which the instrument lies, resolved from the instrument identifiers. | [optional] [readonly] 
**dom_ccy** | **str** | The domestic currency of the instrument, resolved from the instrument identifiers. | [optional] [readonly] 
## Example

```python
from lusid.models.new_instrument import NewInstrument
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

instrument_identifiers: Dict[str, Optional[StrictStr]] = # Replace with your value
lusid_instrument_id: Optional[StrictStr] = "example_lusid_instrument_id"
instrument_scope: Optional[StrictStr] = "example_instrument_scope"
dom_ccy: Optional[StrictStr] = "example_dom_ccy"
new_instrument_instance = NewInstrument(instrument_identifiers=instrument_identifiers, lusid_instrument_id=lusid_instrument_id, instrument_scope=instrument_scope, dom_ccy=dom_ccy)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

