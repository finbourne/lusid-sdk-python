# PropertyValue

The value of the property.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**label_value** | **str** | The text value of a property defined as having the &#39;Label&#39; type. | [optional] 
**metric_value** | [**MetricValue**](MetricValue.md) |  | [optional] 
**label_value_set** | [**LabelValueSet**](LabelValueSet.md) |  | [optional] 
## Example

```python
from lusid.models.property_value import PropertyValue
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

label_value: Optional[StrictStr] = "example_label_value"
metric_value: Optional[MetricValue] = # Replace with your value
label_value_set: Optional[LabelValueSet] = # Replace with your value
property_value_instance = PropertyValue(label_value=label_value, metric_value=metric_value, label_value_set=label_value_set)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

