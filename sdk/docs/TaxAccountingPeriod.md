# TaxAccountingPeriod

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**label** | **str** | The label of the period, for example the four-digit year. | [optional] 
**start** | **datetime** | The first day of the period, inclusive. | [optional] 
**end** | **datetime** | The last day of the period, inclusive. | [optional] 
## Example

```python
from lusid.models.tax_accounting_period import TaxAccountingPeriod
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

label: Optional[StrictStr] = "example_label"
start: Optional[datetime] = # Replace with your value
end: Optional[datetime] = # Replace with your value
tax_accounting_period_instance = TaxAccountingPeriod(label=label, start=start, end=end)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

