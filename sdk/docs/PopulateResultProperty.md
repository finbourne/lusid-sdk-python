# PopulateResultProperty

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**property_key** | **str** | The property the formula populates. Must be an existing, single-valued property in the RecResult domain, and may appear only once. | 
**formula** | **str** | The formula gives the value of the property. The value must be of the property&#39;s type. A formula cannot populate an Int property, because its numbers are decimal. A null value means that the property has no value. The formula can read resultType, resultCardinality, resultLifecycle, exception.status, exception.closureType, exception.asAtClosed, exception.asAtClosureInvalidated, review.status, review.decision and review.decisionGroup.groupNumber. It reads rules by name as CoreRules[name] and AggregateRules[name]. Each rule has .leftValue, .rightValue and .appliedTolerance.toleranceType. A numeric aggregate rule also has .difference. You can compare CoreRules[name] with no side by eq, in or startswith. The comparison is true if either side matches. With neq, not in or not startswith, it is true if no side matches. Ordering comparisons must name the side. Comparisons ignore case and accents. | 
**overwrite_manual_edits_on_re_run** | **bool** | Whether a run replaces a value that a user has set or removed on the property. After a run replaces it, later runs populate it again, even if this flag is then false. Defaults to false. | [optional] 
## Example

```python
from lusid.models.populate_result_property import PopulateResultProperty
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

property_key: StrictStr = "example_property_key"
formula: StrictStr = "example_formula"
overwrite_manual_edits_on_re_run: Optional[StrictBool] = # Replace with your value
overwrite_manual_edits_on_re_run:Optional[StrictBool] = None
populate_result_property_instance = PopulateResultProperty(property_key=property_key, formula=formula, overwrite_manual_edits_on_re_run=overwrite_manual_edits_on_re_run)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

