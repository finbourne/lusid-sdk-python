# InstrumentEventConfiguration

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**transaction_template_scopes** | **List[str]** |  | [optional] 
**recipe_id** | [**ResourceId**](ResourceId.md) |  | [optional] 
## Example

```python
from lusid.models.instrument_event_configuration import InstrumentEventConfiguration
from typing import Any, Dict, List, Optional
from pydantic.v1 import BaseModel, Field, StrictStr, conlist

transaction_template_scopes: Optional[conlist(StrictStr, max_items=1)] = Field(None, alias="transactionTemplateScopes")
recipe_id: Optional[ResourceId] = # Replace with your value
instrument_event_configuration_instance = InstrumentEventConfiguration(transaction_template_scopes=transaction_template_scopes, recipe_id=recipe_id)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

