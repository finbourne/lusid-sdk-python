# InflationConvexityOptions

Parameters of the Jarrow-Yildirim convexity correction applied to projected inflation index  values. Unlike most option blocks there is no defaulting here: nothing in the pricing chain  infers an index volatility, a nominal volatility or a correlation from market data, so an armed  correction is entirely the caller's stated view and every member must be supplied.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**nominal_index_correlation** | **float** | Correlation between the inflation index and the nominal short rate, in [-1, 1]. A positive  correlation makes the factor greater than one for a projection funded later than the curve&#39;s  own observation basis. | [optional] 
**index_volatility** | **float** | Lognormal volatility of the inflation index, as a decimal (0.0095 is 0.95%). Must be  strictly positive - a zero volatility disarms the correction arithmetically, which is what  omitting the whole block already expresses. | [optional] 
**nominal_volatility** | **float** | Volatility of the nominal short rate in the Hull-White dynamics the correction assumes, as a  decimal (0.008 is 80bp). Must be strictly positive. | [optional] 
**nominal_mean_reversion** | **float** | Mean reversion speed of the nominal short rate, per year. Must be strictly positive: the  closed form divides by it. | [optional] 
## Example

```python
from lusid.models.inflation_convexity_options import InflationConvexityOptions
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

nominal_index_correlation: Optional[Union[StrictFloat, StrictInt]] = # Replace with your value
index_volatility: Optional[Union[StrictFloat, StrictInt]] = # Replace with your value
nominal_volatility: Optional[Union[StrictFloat, StrictInt]] = # Replace with your value
nominal_mean_reversion: Optional[Union[StrictFloat, StrictInt]] = # Replace with your value
inflation_convexity_options_instance = InflationConvexityOptions(nominal_index_correlation=nominal_index_correlation, index_volatility=index_volatility, nominal_volatility=nominal_volatility, nominal_mean_reversion=nominal_mean_reversion)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

