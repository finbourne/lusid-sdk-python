# NavActivityAdjustment

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**nav_activity_adjustment_type** | **str** | . The available values are: PortfolioTransaction | 
## Example

```python
from lusid.models.nav_activity_adjustment import NavActivityAdjustment
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

nav_activity_adjustment_type: StrictStr = "example_nav_activity_adjustment_type"
nav_activity_adjustment_instance = NavActivityAdjustment(nav_activity_adjustment_type=nav_activity_adjustment_type)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

