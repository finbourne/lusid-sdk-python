# PriceShiftDefinition

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**instrument** | **str** | A single instrument identifier this shift applies to. Exactly one of Instrument and Filter  must be supplied. | [optional] 
**filter** | **str** | A LUSID filter expression over the instrument entity - fields and properties - selecting which  instruments&#39; quotes the shift applies to, e.g.  \&quot;assetClass eq &#39;Bond&#39; and properties[Instrument/Issuer/Name] eq &#39;X&#39;\&quot;.  Exactly one of Instrument and Filter must be supplied. | [optional] 
**amount** | **float** |  | [optional] 
**shift_type** | **str** | Available values: Absolute, Relative, Percentage. | 
**quote_type** | **str** | Available values: Price, Spread, Rate, LogNormalVol, NormalVol, ParSpread, IsdaSpread, Upfront, Index, Ratio, Delta, PoolFactor, InflationAssumption, DirtyPrice, PrincipalWriteOff, InterestDeferred, InterestShortfall, ConstituentWeightFactor. | [optional] 
**scenario_shift_type** | **str** | Available values: RateCurveShiftDefinition, FxShiftDefinition, PriceShiftDefinition, VolSurfaceShiftDefinition, MdkrGroupShiftDefinition, InflationCurveShiftDefinition, CreditSpreadShiftDefinition, ModelOptionShiftDefinition. | 
## Example

```python
from lusid.models.price_shift_definition import PriceShiftDefinition
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

instrument: Optional[StrictStr] = "example_instrument"
filter: Optional[StrictStr] = "example_filter"
amount: Optional[Union[StrictFloat, StrictInt]] = None
shift_type: StrictStr = "example_shift_type"
quote_type: Optional[StrictStr] = "example_quote_type"
scenario_shift_type: StrictStr = "example_scenario_shift_type"
price_shift_definition_instance = PriceShiftDefinition(instrument=instrument, filter=filter, amount=amount, shift_type=shift_type, quote_type=quote_type, scenario_shift_type=scenario_shift_type)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

