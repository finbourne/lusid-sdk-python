# CounterpartyIdentifier

The legal entity a collateral agreement is made with.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id_type_scope** | **str** | The scope of the identifier type, e.g. the scope of the LEI identifier. | 
**id_type_code** | **str** | The code of the identifier type, e.g. LEI. | 
**code** | **str** | The value of the identifier. | 
## Example

```python
from lusid.models.counterparty_identifier import CounterpartyIdentifier
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

id_type_scope: StrictStr = "example_id_type_scope"
id_type_code: StrictStr = "example_id_type_code"
code: StrictStr = "example_code"
counterparty_identifier_instance = CounterpartyIdentifier(id_type_scope=id_type_scope, id_type_code=id_type_code, code=code)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

