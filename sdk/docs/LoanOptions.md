# LoanOptions

Options for loan facilities and their contracts.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enhanced_rounding** | **bool** | If true, loan facility figures are kept at full precision. A principal repayment that pays a contract down to  within its currency&#39;s smallest unit (for example, under a cent) repays it in full: the leftover below that  precision, the contract&#39;s remaining limit and the undrawn commitment are written off, so the position closes  rather than staying open with a fraction of a cent, and a term facility repaid to that precision has its  remaining units and limit booked out. A facility trade&#39;s share of each contract is also computed without  rounding dust. If false, these figures are calculated as before. Defaults to false. | [optional] 
## Example

```python
from lusid.models.loan_options import LoanOptions
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

enhanced_rounding: Optional[StrictBool] = # Replace with your value
enhanced_rounding:Optional[StrictBool] = None
loan_options_instance = LoanOptions(enhanced_rounding=enhanced_rounding)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

