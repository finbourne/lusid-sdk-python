# CreateCorporateActionSourceRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**scope** | **str** | The scope of the corporate action source | 
**code** | **str** | The code of the corporate action source | 
**display_name** | **str** | The name of the corporate action source | 
**description** | **str** | The description of the corporate action source | [optional] 
**instrument_scopes** | **List[str]** | The list of instrument scopes used as the scope resolution strategy when resolving instruments of upserted corporate actions. | [optional] 
## Example

```python
from lusid.models.create_corporate_action_source_request import CreateCorporateActionSourceRequest
from typing import Any, Dict, List, Optional
from pydantic.v1 import BaseModel, Field, StrictStr, conlist, constr, validator

scope: StrictStr = "example_scope"
code: StrictStr = "example_code"
display_name: StrictStr = "example_display_name"
description: Optional[StrictStr] = "example_description"
instrument_scopes: Optional[conlist(StrictStr, max_items=1)] = Field(None, alias="instrumentScopes", description="The list of instrument scopes used as the scope resolution strategy when resolving instruments of upserted corporate actions.")
create_corporate_action_source_request_instance = CreateCorporateActionSourceRequest(scope=scope, code=code, display_name=display_name, description=description, instrument_scopes=instrument_scopes)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

