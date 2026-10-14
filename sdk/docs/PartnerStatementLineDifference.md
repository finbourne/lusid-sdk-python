# PartnerStatementLineDifference

One figure that differs between two partner statements.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** | The key of the figure. | 
**before** | **float** | The figure on the statement compared against. | [optional] 
**after** | **float** | The figure on this statement. | [optional] 
**change** | **float** | After less before. | 
## Example

```python
from lusid.models.partner_statement_line_difference import PartnerStatementLineDifference
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

key: StrictStr = "example_key"
before: Optional[Union[StrictFloat, StrictInt]] = # Replace with your value
after: Optional[Union[StrictFloat, StrictInt]] = # Replace with your value
change: Union[StrictFloat, StrictInt] = # Replace with your value
partner_statement_line_difference_instance = PartnerStatementLineDifference(key=key, before=before, after=after, change=change)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

