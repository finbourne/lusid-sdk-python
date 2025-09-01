# Compounding

The compounding settings used on interest rate.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**averaging_method** | **str** | Defines whether a weighted or unweighted average is used when calculating the average rate.  It applies only when CompoundingMethod &#x3D; ‘Averaging‘.    Supported string (enumeration) values are: [Unweighted, UnweightedIncludingWeekends, Weighted].  Defaults to \&quot;None\&quot; if not set. | [optional] 
**calculation_shift_method** | **str** | Defines which resets and day counts are used for the rate calculation    Supported string (enumeration) values are: [Lookback, NoShift, ObservationPeriodShift, Lockout].  Defaults to \&quot;NoShift\&quot; if not set. | [optional] 
**compounding_method** | **str** | If the interest rate is simple, compounded or using a pre-computed compounded index.    Supported string (enumeration) values are: [Averaging, Compounding, CompoundedIndex, NonCumulativeCompounding]. | 
**reset_frequency** | **str** | The interest payment frequency.    For more information on tenors, see [knowledge base article KA-02097](https://support.lusid.com/knowledgebase/article/KA-02097) | 
**shift** | **int** | Defines the number of days to lockout or shift observation period by - should be a non-negative integer.  Defaults to 0 if not set. | [optional] 
**spread_compounding_method** | **str** | Defines how the computed leg spread is applied to compounded rate.  It applies only when CompoundingMethod &#x3D; ‘Compounding‘ or ‘CompoundedIndex‘.    Available compounding methods:    | Method | Description |  | ------ | ----------- |  | Straight | Compounding rate in each compound period includes the spread. |  | Flat | Compounding rate does not include the spread, and the spread is used for simple interest in each compound period. |  | SpreadExclusive | Compounding rate does not include the spread, and the spread is used for simple interest for whole accrual period. |    The values \&quot;IsdaCompounding\&quot;, \&quot;NoCompounding\&quot;, \&quot;IsdaFlatCompounding\&quot;, and \&quot;None\&quot; are accepted for compatibility  with existing instruments and their use is discouraged.    Supported string (enumeration) values are: [Straight, IsdaCompounding, NoCompounding, SpreadExclusive, IsdaFlatCompounding, Flat, None].  Defaults to \&quot;None\&quot; if not set. | [optional] 
**rounding_precision** | **int** | Defines the number of decimal places the compounded rate (expressed as a decimal) should be rounded to.  This is an optional field, leaving it blank will mean no rounding takes place in Compounding. | [optional] 
## Example

```python
from lusid.models.compounding import Compounding
from typing import Any, Dict, Optional
from pydantic.v1 import BaseModel, Field, StrictInt, StrictStr, constr

averaging_method: Optional[StrictStr] = "example_averaging_method"
calculation_shift_method: Optional[StrictStr] = "example_calculation_shift_method"
compounding_method: StrictStr = "example_compounding_method"
reset_frequency: StrictStr = "example_reset_frequency"
shift: Optional[StrictInt] = # Replace with your value
shift: Optional[StrictInt] = None
spread_compounding_method: Optional[StrictStr] = "example_spread_compounding_method"
rounding_precision: Optional[StrictInt] = # Replace with your value
rounding_precision: Optional[StrictInt] = None
compounding_instance = Compounding(averaging_method=averaging_method, calculation_shift_method=calculation_shift_method, compounding_method=compounding_method, reset_frequency=reset_frequency, shift=shift, spread_compounding_method=spread_compounding_method, rounding_precision=rounding_precision)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

