# PreviousShareClassBreakdown

The data for a Share Class at the previous valuation point.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**nav** | [**PreviousNAV**](PreviousNAV.md) |  | 
**unitisation** | [**UnitisationData**](UnitisationData.md) |  | [optional] 
**share_class_to_fund_fx_rate** | **float** | The fx rate from the Share Class currency to the fund currency at this valuation point. | 
## Example

```python
from lusid.models.previous_share_class_breakdown import PreviousShareClassBreakdown
from typing import Any, Dict, Optional, Union
from pydantic.v1 import BaseModel, Field, StrictFloat, StrictInt

nav: PreviousNAV = # Replace with your value
unitisation: Optional[UnitisationData] = None
share_class_to_fund_fx_rate: Union[StrictFloat, StrictInt] = # Replace with your value
previous_share_class_breakdown_instance = PreviousShareClassBreakdown(nav=nav, unitisation=unitisation, share_class_to_fund_fx_rate=share_class_to_fund_fx_rate)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

