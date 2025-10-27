# FundValuationPointData

The Valuation Point Data for a Fund on a specified date.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**back_out** | [**Dict[str, FundAmount]**](FundAmount.md) | Bucket of detail for the Valuation Point where data points have been &#39;backed out&#39;. | 
**dealing** | [**Dict[str, FundAmount]**](FundAmount.md) | Bucket of detail for any &#39;Dealing&#39; that has occured inside the queried period. | 
**pn_l** | [**FundPnlBreakdown**](FundPnlBreakdown.md) |  | 
**gav** | **float** | The Gross Asset Value of the Fund or Share Class at the Valuation Point. This is effectively a summation of all Trial balance entries linked to accounts of types &#39;Asset&#39; and &#39;Liabilities&#39;. | 
**fees** | [**Dict[str, FeeAccrual]**](FeeAccrual.md) | Bucket of detail for any &#39;Fees&#39; that have been charged in the selected period. | 
**nav** | **float** | The Net Asset Value of the Fund or Share Class at the Valuation Point. This represents the GAV with any fees applied in the period. | 
**miscellaneous** | [**Dict[str, FundAmount]**](FundAmount.md) | Not used directly by the LUSID engines but serves as a holding area for any custom derived data points that may be useful in, for example, fee calculations). | [optional] 
**previous_valuation_point_data** | [**PreviousFundValuationPointData**](PreviousFundValuationPointData.md) |  | [optional] 
## Example

```python
from lusid.models.fund_valuation_point_data import FundValuationPointData
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

back_out: Dict[str, FundAmount] = # Replace with your value
dealing: Dict[str, FundAmount] = # Replace with your value
pn_l: FundPnlBreakdown = # Replace with your value
gav: Union[StrictFloat, StrictInt] = # Replace with your value
fees: Dict[str, FeeAccrual] = # Replace with your value
nav: Union[StrictFloat, StrictInt] = # Replace with your value
miscellaneous: Optional[Dict[str, FundAmount]] = # Replace with your value
previous_valuation_point_data: Optional[PreviousFundValuationPointData] = # Replace with your value
fund_valuation_point_data_instance = FundValuationPointData(back_out=back_out, dealing=dealing, pn_l=pn_l, gav=gav, fees=fees, nav=nav, miscellaneous=miscellaneous, previous_valuation_point_data=previous_valuation_point_data)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

