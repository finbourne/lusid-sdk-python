# PartnerStatementLine

One figure on a partner statement.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** | The key of the figure. | 
**label** | **str** | The label of the figure. | 
**amount** | **float** | The amount of the figure. | 
## Example

```python
from lusid.models.partner_statement_line import PartnerStatementLine
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

key: StrictStr = "example_key"
label: StrictStr = "example_label"
amount: Union[StrictFloat, StrictInt] = # Replace with your value
partner_statement_line_instance = PartnerStatementLine(key=key, label=label, amount=amount)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

