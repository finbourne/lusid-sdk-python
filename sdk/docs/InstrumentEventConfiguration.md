# InstrumentEventConfiguration

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**transaction_template_scopes** | **List[str]** |  | [optional] 
**recipe_id** | [**ResourceId**](ResourceId.md) |  | [optional] 
## Example

```python
from lusid.models.instrument_event_configuration import InstrumentEventConfiguration
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

transaction_template_scopes: Optional[List[StrictStr]] = # Replace with your value
recipe_id: Optional[ResourceId] = # Replace with your value
instrument_event_configuration_instance = InstrumentEventConfiguration(transaction_template_scopes=transaction_template_scopes, recipe_id=recipe_id)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

