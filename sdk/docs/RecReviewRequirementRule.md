# RecReviewRequirementRule

What the results of one structural category need by way of review: the requirement they carry by default,  and an optional condition that flips it for the results it selects.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**review_requirement** | **str** | Whether this category&#39;s results need reviewing. One of: Required, NotRequired. Available values: Required, NotRequired. | 
**override_condition** | **str** | A boolean expression over a rec result, e.g. \&quot;resultType eq &#39;Cross&#39;\&quot;. Where it holds for a result, that result is treated as the opposite of the category&#39;s reviewRequirement. Null means the requirement applies to every result in the category. | [optional] 
## Example

```python
from lusid.models.rec_review_requirement_rule import RecReviewRequirementRule
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

review_requirement: StrictStr = "example_review_requirement"
override_condition: Optional[StrictStr] = "example_override_condition"
rec_review_requirement_rule_instance = RecReviewRequirementRule(review_requirement=review_requirement, override_condition=override_condition)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

