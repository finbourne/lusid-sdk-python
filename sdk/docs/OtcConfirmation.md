# OtcConfirmation

For the storage of any information pertinent to the confirmation of an OTC trade. e.g the Counterparty Agreement Code
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**counterparty_agreement_id** | [**ResourceId**](ResourceId.md) |  | [optional] 
## Example

```python
from lusid.models.otc_confirmation import OtcConfirmation
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

counterparty_agreement_id: Optional[ResourceId] = # Replace with your value
otc_confirmation_instance = OtcConfirmation(counterparty_agreement_id=counterparty_agreement_id)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

