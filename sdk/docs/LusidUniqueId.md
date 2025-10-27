# LusidUniqueId

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | The type for the LUSID unique id, this will depend on the type of entity found, for instance &#39;Instrument&#39; would have a value of &#39;LusidInstrumentId&#39; | 
**value** | **str** | The value for the LUSID unique id | 
## Example

```python
from lusid.models.lusid_unique_id import LusidUniqueId
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

type: StrictStr = "example_type"
value: StrictStr = "example_value"
lusid_unique_id_instance = LusidUniqueId(type=type, value=value)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

