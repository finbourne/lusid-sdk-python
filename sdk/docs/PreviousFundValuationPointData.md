# PreviousFundValuationPointData

The data for a Fund at the previous valuation point.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**nav** | [**FundPreviousNAV**](FundPreviousNAV.md) |  | 
## Example

```python
from lusid.models.previous_fund_valuation_point_data import PreviousFundValuationPointData
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

nav: FundPreviousNAV
previous_fund_valuation_point_data_instance = PreviousFundValuationPointData(nav=nav)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

