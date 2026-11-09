# TaxClassificationFieldVersion

One stored value of a classification input or override and the bitemporal window it held for.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**field** | **str** | The name of the classification input or override the version belongs to. | 
**value** | **str** | The value of the field over the version&#39;s effective and asAt window. | [optional] 
**effective_from** | **datetime** | The start of the effective window the value applies from. | 
**effective_until** | **datetime** | The end of the effective window the value applies until. | 
**as_at_from** | **datetime** | The asAt time the value was recorded. | 
**as_at_until** | **datetime** | The asAt time the value was superseded, if it has been. | [optional] 
## Example

```python
from lusid.models.tax_classification_field_version import TaxClassificationFieldVersion
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

field: StrictStr = "example_field"
value: Optional[StrictStr] = "example_value"
effective_from: datetime = # Replace with your value
effective_until: datetime = # Replace with your value
as_at_from: datetime = # Replace with your value
as_at_until: Optional[datetime] = # Replace with your value
tax_classification_field_version_instance = TaxClassificationFieldVersion(field=field, value=value, effective_from=effective_from, effective_until=effective_until, as_at_from=as_at_from, as_at_until=as_at_until)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

