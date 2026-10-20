# WithholdingTaxUnresolvedDimension

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**read_from** | **List[str]** | What booking reads the dimension from: Transaction, Portfolio or Fund. | 
## Example

```python
from lusid.models.withholding_tax_unresolved_dimension import WithholdingTaxUnresolvedDimension
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

read_from: List[StrictStr] = # Replace with your value
withholding_tax_unresolved_dimension_instance = WithholdingTaxUnresolvedDimension(read_from=read_from)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

