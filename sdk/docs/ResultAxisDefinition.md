# ResultAxisDefinition

Describes one labelled axis of a matrix-shaped result (Result1D/Result2D), so consumers can  tell what the labels on that axis mean without opening each value.  A Result1D has a single Y axis; a Result2D has a Y (row) and an X (column) axis.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**axis** | **str** | Which axis of the result this describes: \&quot;Y\&quot; labels the rows (the only axis of a Result1D,  serialized as labelsY on the value); \&quot;X\&quot; labels the columns of a Result2D (labelsX). | [optional] 
**name** | **str** | The display name of the axis, e.g. \&quot;Bucket\&quot; or \&quot;Expiry\&quot;. | [optional] 
**label_type** | **str** | What kind of value the axis labels are drawn from, e.g. \&quot;Tenor\&quot;, \&quot;Date\&quot; or \&quot;Strike\&quot;.  Consumers can switch rendering on well-known values and fall back to showing labels verbatim. | [optional] 
**description** | **str** | What the axis means for this result. | [optional] 
## Example

```python
from lusid.models.result_axis_definition import ResultAxisDefinition
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

axis: Optional[StrictStr] = "example_axis"
name: Optional[StrictStr] = "example_name"
label_type: Optional[StrictStr] = "example_label_type"
description: Optional[StrictStr] = "example_description"
result_axis_definition_instance = ResultAxisDefinition(axis=axis, name=name, label_type=label_type, description=description)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

