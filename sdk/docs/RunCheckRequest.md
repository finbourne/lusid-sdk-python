# RunCheckRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**lusid_entity_dataset** | [**LusidEntityDataset**](LusidEntityDataset.md) |  | [optional] 
**limit_individual_breaches_per_rule** | **int** | The maximum number of individual breaches to return per rule. Defaults to 100 if not specified. | [optional] 
## Example

```python
from lusid.models.run_check_request import RunCheckRequest
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

lusid_entity_dataset: Optional[LusidEntityDataset] = # Replace with your value
limit_individual_breaches_per_rule: Optional[StrictInt] = # Replace with your value
limit_individual_breaches_per_rule: Optional[StrictInt] = None
run_check_request_instance = RunCheckRequest(lusid_entity_dataset=lusid_entity_dataset, limit_individual_breaches_per_rule=limit_individual_breaches_per_rule)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

