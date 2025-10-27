# ReconciliationLine

In evaluating a left and right hand side holding or valuation set, two data records result. These are then compared based on a set of  rules. This results in either a match or failure to match. If there is a match both left and right will be present, otherwise one will not.  A difference will be present if a match was calculated.  The options used in comparison may result in elision of results where an exact or tolerable match is made.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**left** | **Dict[str, Optional[object]]** | Left hand side of the comparison | [optional] 
**right** | **Dict[str, Optional[object]]** | Right hand side of the comparison | [optional] 
**difference** | **Dict[str, Optional[object]]** | Difference between LHS and RHS of comparison | [optional] 
**result_comparison** | **Dict[str, Optional[object]]** | The logical or semantic description of the difference, e.g. \&quot;Matches\&quot; or \&quot;MatchesWithTolerance\&quot; or \&quot;Failed\&quot;. | [optional] 
## Example

```python
from lusid.models.reconciliation_line import ReconciliationLine
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

left: Optional[Dict[str, Any]] = # Replace with your value
right: Optional[Dict[str, Any]] = # Replace with your value
difference: Optional[Dict[str, Any]] = # Replace with your value
result_comparison: Optional[Dict[str, Any]] = # Replace with your value
reconciliation_line_instance = ReconciliationLine(left=left, right=right, difference=difference, result_comparison=result_comparison)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

