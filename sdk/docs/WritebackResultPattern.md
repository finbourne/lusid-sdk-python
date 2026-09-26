# WritebackResultPattern

One combination of units difference and result cardinality for which writeback is suggested. A combination  that is not configured never produces a suggestion, even where the reconciliation has crossed the items  successfully. The collection is a set, and is returned in a canonical order regardless of the order supplied.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**units_difference** | **str** | How the origin units compare to the target units, on a literal comparison rather than on the result type. One of: Exact, ShortWithinTolerance, ShortBeyondTolerance, LongWithinTolerance. LongBeyondTolerance is reported on results but cannot be configured. Available values: Exact, ShortWithinTolerance, ShortBeyondTolerance, LongWithinTolerance, LongBeyondTolerance. | 
**result_cardinality** | **str** | The item cardinality of the result, read left to right. One of: OneToOne, OneToMany, ManyToOne. ManyToMany is not supported. Available values: OneToOne, OneToMany, ManyToOne, ManyToMany, OneToNone, ManyToNone, NoneToOne, NoneToMany, NoneToNone. | 
**use_target_units** | **bool** | Which side supplies the units where the two sides do not agree exactly. When false, the units come from the origin and any difference is left outstanding on the target; when true, they come from the target, which is written back in full. Defaults to false. Must be true for LongWithinTolerance, and cannot be true for ShortBeyondTolerance. | [optional] 
## Example

```python
from lusid.models.writeback_result_pattern import WritebackResultPattern
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

units_difference: StrictStr = "example_units_difference"
result_cardinality: StrictStr = "example_result_cardinality"
use_target_units: Optional[StrictBool] = # Replace with your value
use_target_units:Optional[StrictBool] = None
writeback_result_pattern_instance = WritebackResultPattern(units_difference=units_difference, result_cardinality=result_cardinality, use_target_units=use_target_units)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

