# ExternalRecType

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name for this external reconciliation describing source data. | 
**temporality** | **str** | How the reconciliation reads its data: PointInTime (the latest state as at the instance&#39;s effectiveAt, the default) or Activity (everything effective across the instance&#39;s activity window). Available values: PointInTime, Activity. | [optional] 
## Example

```python
from lusid.models.external_rec_type import ExternalRecType
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

name: StrictStr = "example_name"
temporality: Optional[StrictStr] = "example_temporality"
external_rec_type_instance = ExternalRecType(name=name, temporality=temporality)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

