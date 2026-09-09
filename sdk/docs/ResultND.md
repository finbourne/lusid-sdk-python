# ResultND

A single result-value shape whose structure is derived from `dimension`, replacing one  hand-maintained type per rank (Result0D/Result1D/Result2D). Additive and opt-in: existing  consumers of those types see no change to their response bytes.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**result_value_type** | **str** | The discriminator for this result shape. Always \&quot;ResultND\&quot;. | [optional] [readonly] 
**dimension** | **int** | The rank of the result, 0..N. Determines which of &#x60;value&#x60; / &#x60;values&#x60; is populated  and how deeply &#x60;values&#x60; is nested. | [optional] 
**labels** | **List[List[str]]** | One ordered array of labels per axis, index to label, in the same axis order as  &#x60;AddressDefinition.Axes&#x60;. Length equals &#x60;dimension&#x60;; empty for a scalar. | [optional] 
**value** | **float** | The scalar value. Present if and only if &#x60;dimension&#x60; is 0. | [optional] 
**values** | **List[float]** | The values, flattened row-major with axis 0 outermost and dense - a coordinate the legacy  format would have elided is materialised as 0. The shape is read off &#x60;labels&#x60;: position  (i0, i1, ..., ik) is at offset i0 * len(labels[1]) * ... * len(labels[k]) + i1 * ... + ik.  Present if and only if &#x60;dimension&#x60; is at least 1. | [optional] 
**has_annotation** | **bool** | Unchanged from Result0D/1D/2D. | [optional] 
**units** | [**List[UnitDimension]**](UnitDimension.md) | A flat list of dimensional-analysis units, replacing the doubled  &#x60;{ units: { units: [] } }&#x60; wrapper on the legacy types. The count reflects the order of  the derivative (e.g. two entries for a ratio such as a rates delta), not the result&#39;s axes. | [optional] 
## Example

```python
from lusid.models.result_nd import ResultND
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

result_value_type: Optional[StrictStr] = "example_result_value_type"
dimension: Optional[StrictInt] = # Replace with your value
dimension: Optional[StrictInt] = None
labels: Optional[List[List[StrictStr]]] = # Replace with your value
value: Optional[Union[StrictFloat, StrictInt]] = # Replace with your value
values: Optional[List[Union[StrictFloat, StrictInt]]] = # Replace with your value
has_annotation: Optional[StrictBool] = # Replace with your value
has_annotation:Optional[StrictBool] = None
units: Optional[List[UnitDimension]] = # Replace with your value
result_nd_instance = ResultND(result_value_type=result_value_type, dimension=dimension, labels=labels, value=value, values=values, has_annotation=has_annotation, units=units)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

