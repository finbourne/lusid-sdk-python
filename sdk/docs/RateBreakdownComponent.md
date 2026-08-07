# RateBreakdownComponent

A tax-characterised payout line within a CashElection on a CashDividendEvent.  Each line carries a rate-type classifier and a per-unit amount in the parent election's currency.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**rate_type** | **str** | Free-string distribution rate-type code (e.g. UNFR, FLFR, PID). | 
**dividend_rate** | **float** | Per-unit amount for this line, in the parent election&#39;s dividend currency. | 
## Example

```python
from lusid.models.rate_breakdown_component import RateBreakdownComponent
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

rate_type: StrictStr = "example_rate_type"
dividend_rate: Union[StrictFloat, StrictInt] = # Replace with your value
rate_breakdown_component_instance = RateBreakdownComponent(rate_type=rate_type, dividend_rate=dividend_rate)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

