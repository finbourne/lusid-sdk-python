# HullWhiteModelOptions

Model options for the Hull-White one-factor lattice pricer.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**mean_reversion** | **float** | The mean reversion speed of the short rate. Must be strictly positive. Defaults to 0.03. | [optional] 
**volatility** | **float** | The normal (absolute) volatility of the short rate, e.g. 0.008 for 80bp per year. Defaults to 0.008. | [optional] 
**lattice_steps** | **int** | The number of uniform time steps in the lattice. More steps give a finer discretisation  of the short-rate process at greater computational cost. Defaults to 200. | [optional] 
**effective_rate_bump_size** | **float** | The parallel curve shift, as an absolute rate, used for the central-difference effective  duration and convexity, e.g. 0.0001 for a 1bp bump. Must be strictly positive.  Defaults to 0.0025 (25bp, the market convention for option-adjusted risk) when not supplied. | [optional] 
**mean_reversion_by_currency** | **Dict[str, float]** | Per-currency mean-reversion overrides, keyed by ISO currency code.  A currency absent from this map uses MeanReversion. | [optional] 
**volatility_by_currency** | **Dict[str, float]** | Per-currency short-rate volatility overrides, keyed by ISO currency code.  A currency absent from this map uses Volatility. Short-rate volatility is a per-currency  quantity in practice, so a book spanning several currencies can calibrate each currency  separately instead of sharing a single global figure. | [optional] 
**model_options_type** | **str** | Available values: Invalid, OpaqueModelOptions, EmptyModelOptions, IndexModelOptions, FxForwardModelOptions, FundingLegModelOptions, EquityModelOptions, CdsModelOptions, FlexibleLoanPricerOptions, HullWhiteModelOptions, BondLookupModelOptions. | 
## Example

```python
from lusid.models.hull_white_model_options import HullWhiteModelOptions
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

mean_reversion: Optional[Union[StrictFloat, StrictInt]] = # Replace with your value
volatility: Optional[Union[StrictFloat, StrictInt]] = # Replace with your value
lattice_steps: Optional[StrictInt] = # Replace with your value
lattice_steps: Optional[StrictInt] = None
effective_rate_bump_size: Optional[Union[StrictFloat, StrictInt]] = # Replace with your value
mean_reversion_by_currency: Optional[Dict[str, Union[StrictFloat, StrictInt]]] = # Replace with your value
volatility_by_currency: Optional[Dict[str, Union[StrictFloat, StrictInt]]] = # Replace with your value
model_options_type: StrictStr = "example_model_options_type"
hull_white_model_options_instance = HullWhiteModelOptions(mean_reversion=mean_reversion, volatility=volatility, lattice_steps=lattice_steps, effective_rate_bump_size=effective_rate_bump_size, mean_reversion_by_currency=mean_reversion_by_currency, volatility_by_currency=volatility_by_currency, model_options_type=model_options_type)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

