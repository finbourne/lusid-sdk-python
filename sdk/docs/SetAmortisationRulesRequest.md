# SetAmortisationRulesRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**rules_interval** | [**RulesInterval**](RulesInterval.md) |  | 
## Example

```python
from lusid.models.set_amortisation_rules_request import SetAmortisationRulesRequest
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

rules_interval: RulesInterval = # Replace with your value
set_amortisation_rules_request_instance = SetAmortisationRulesRequest(rules_interval=rules_interval)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

