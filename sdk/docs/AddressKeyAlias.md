# AddressKeyAlias

An address key alias that maps a short alias key to a real key with options.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**scope** | **str** | The scope of the alias | 
**code** | **str** | The code of the alias | 
**alias_key** | **str** | The alias address key, must start with \&quot;Alias/\&quot; prefix (e.g., \&quot;Alias/DailyNZPnL\&quot;) | 
**real_key** | **str** | The real address key this alias resolves to (e.g., \&quot;ProfitAndLoss/Total\&quot;). Must NOT start with \&quot;Alias/\&quot;. | 
**options** | **Dict[str, Optional[str]]** | Options to apply when resolving the alias (e.g., {\&quot;Window\&quot;:\&quot;Daily\&quot;,\&quot;TimeZone\&quot;:\&quot;NZ\&quot;}) | [optional] 
**display_name** | **str** | Human-readable display name | [optional] 
**description** | **str** | Description of the alias | [optional] 
## Example

```python
from lusid.models.address_key_alias import AddressKeyAlias
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

scope: StrictStr = "example_scope"
code: StrictStr = "example_code"
alias_key: StrictStr = "example_alias_key"
real_key: StrictStr = "example_real_key"
options: Optional[Dict[str, Optional[StrictStr]]] = # Replace with your value
display_name: Optional[StrictStr] = "example_display_name"
description: Optional[StrictStr] = "example_description"
address_key_alias_instance = AddressKeyAlias(scope=scope, code=code, alias_key=alias_key, real_key=real_key, options=options, display_name=display_name, description=description)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

