# ModelOptionShiftDefinition

A shift of a pricing model option for the duration of the scenario. Unlike every other shift  type, the target is not a piece of market data: it is a field of the model options carried by  the recipe's model rule (for example the short-rate volatility of the Hull-White one-factor  lattice), which no market data shift can reach because a model option is configuration, not a  resolved market element. The shift is scoped to a model rule by the model's name, optionally  narrowed to one instrument type, and applies to every instrument that rule prices.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**model_name** | **str** | The pricing model whose options this shift targets, exactly as named on the recipe&#39;s model  rule, e.g. \&quot;HullWhite1F\&quot;. Only models with shiftable options are accepted; an unknown or  unsupported model name is rejected when the scenario is stored. | 
**instrument_type** | **str** | The instrument type narrowing which of the model&#39;s rules the shift applies to, matching the  instrument-type addressing of model rules in the recipe, e.g. \&quot;ComplexBond\&quot;. Omitted, the  shift applies to every instrument the named model prices. | [optional] 
**option_name** | **str** | The model option field the shift moves, e.g. \&quot;Volatility\&quot; or \&quot;MeanReversion\&quot; for  HullWhite1F. Only a whitelisted set of options per model is shiftable; an unknown option  name is rejected when the scenario is stored. | 
**ccy** | **str** | For options carrying per-currency overrides (e.g. HullWhite1F&#39;s VolatilityByCurrency): the  ISO currency code whose effective value the shift moves. The shifted entry starts from the  existing override for that currency, or from the scalar option where no override exists.  Omitted, the shift moves the scalar option and every per-currency override together, so the  effective value moves for every instrument regardless of which level supplies it. | [optional] 
**amount** | **float** | The size of the shift, in the units given by ShiftType: the option&#39;s own units for Absolute  (0.0010 on a volatility of 0.008 is ten basis points of annualised volatility), or a  fraction of the configured value for Relative (0.1 raises it by ten percent). | [optional] 
**shift_type** | **str** | Available values: Absolute, Relative. | 
**scenario_shift_type** | **str** | Available values: RateCurveShiftDefinition, FxShiftDefinition, PriceShiftDefinition, VolSurfaceShiftDefinition, MdkrGroupShiftDefinition, InflationCurveShiftDefinition, CreditSpreadShiftDefinition, ModelOptionShiftDefinition. | 
## Example

```python
from lusid.models.model_option_shift_definition import ModelOptionShiftDefinition
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

model_name: StrictStr = "example_model_name"
instrument_type: Optional[StrictStr] = "example_instrument_type"
option_name: StrictStr = "example_option_name"
ccy: Optional[StrictStr] = "example_ccy"
amount: Optional[Union[StrictFloat, StrictInt]] = # Replace with your value
shift_type: StrictStr = "example_shift_type"
scenario_shift_type: StrictStr = "example_scenario_shift_type"
model_option_shift_definition_instance = ModelOptionShiftDefinition(model_name=model_name, instrument_type=instrument_type, option_name=option_name, ccy=ccy, amount=amount, shift_type=shift_type, scenario_shift_type=scenario_shift_type)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

