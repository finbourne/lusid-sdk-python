# ShareClassBreakdown

The Valuation Point Data for a Share Class on a specified date.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**back_out** | [**Dict[str, ShareClassAmount]**](ShareClassAmount.md) | Bucket of detail for the Valuation Point where data points have been &#39;backed out&#39;. | 
**dealing** | [**ShareClassDealingBreakdown**](ShareClassDealingBreakdown.md) |  | 
**pn_l** | [**ShareClassPnlBreakdown**](ShareClassPnlBreakdown.md) |  | 
**gav** | [**ShareClassAmount**](ShareClassAmount.md) |  | 
**fees** | [**Dict[str, FeeAccrual]**](FeeAccrual.md) | Bucket of detail for any &#39;Fees&#39; that have been charged in the selected period. | 
**nav** | [**ShareClassAmount**](ShareClassAmount.md) |  | 
**unitisation** | [**UnitisationData**](UnitisationData.md) |  | [optional] 
**miscellaneous** | [**Dict[str, ShareClassAmount]**](ShareClassAmount.md) | Not used directly by the LUSID engines but serves as a holding area for any custom derived data points that may be useful in, for example, fee calculations). | [optional] 
**share_class_to_fund_fx_rate** | **float** | The fx rate from the Share Class currency to the fund currency at this valuation point. | 
**capital_ratio** | **float** | The proportion of the fund&#39;s adjusted beginning equity (ie: the sum of the previous NAV and the net dealing) that is invested in the share class. | 
**previous_share_class_breakdown** | [**PreviousShareClassBreakdown**](PreviousShareClassBreakdown.md) |  | 
## Example

```python
from lusid.models.share_class_breakdown import ShareClassBreakdown
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

back_out: Dict[str, ShareClassAmount] = # Replace with your value
dealing: ShareClassDealingBreakdown
pn_l: ShareClassPnlBreakdown = # Replace with your value
gav: ShareClassAmount
fees: Dict[str, FeeAccrual] = # Replace with your value
nav: ShareClassAmount
unitisation: Optional[UnitisationData] = None
miscellaneous: Optional[Dict[str, ShareClassAmount]] = # Replace with your value
share_class_to_fund_fx_rate: Union[StrictFloat, StrictInt] = # Replace with your value
capital_ratio: Union[StrictFloat, StrictInt] = # Replace with your value
previous_share_class_breakdown: PreviousShareClassBreakdown = # Replace with your value
share_class_breakdown_instance = ShareClassBreakdown(back_out=back_out, dealing=dealing, pn_l=pn_l, gav=gav, fees=fees, nav=nav, unitisation=unitisation, miscellaneous=miscellaneous, share_class_to_fund_fx_rate=share_class_to_fund_fx_rate, capital_ratio=capital_ratio, previous_share_class_breakdown=previous_share_class_breakdown)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

