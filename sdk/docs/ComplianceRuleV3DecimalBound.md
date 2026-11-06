# ComplianceRuleV3DecimalBound

A check bound value paired with whether a value landing exactly on it satisfies the check.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | **float** |  | 
**inclusive** | **bool** |  | 
## Example

```python
from lusid.models.compliance_rule_v3_decimal_bound import ComplianceRuleV3DecimalBound
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

value: Union[StrictFloat, StrictInt]
inclusive: StrictBool
inclusive:StrictBool = True
compliance_rule_v3_decimal_bound_instance = ComplianceRuleV3DecimalBound(value=value, inclusive=inclusive)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

