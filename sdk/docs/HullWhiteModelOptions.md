# HullWhiteModelOptions

Model options for the Hull-White one-factor lattice pricer.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**mean_reversion** | **float** | The mean reversion speed of the short rate. Must be strictly positive. Defaults to 0.03. | [optional] 
**volatility** | **float** | The normal (absolute) volatility of the short rate, e.g. 0.008 for 80bp per year. Must not  be negative; zero is allowed and prices with a deterministic short rate. Defaults to 0.008. | [optional] 
**lattice_steps** | **int** | The number of uniform time steps in the lattice. More steps give a finer discretisation  of the short-rate process at greater computational cost. Defaults to 200. | [optional] 
**effective_rate_bump_size** | **float** | The parallel curve shift, as an absolute rate, used for the central-difference effective  duration and convexity, e.g. 0.0001 for a 1bp bump. Must be strictly positive.  Defaults to 0.0025 (25bp, the market convention for option-adjusted risk) when not supplied. | [optional] 
**mean_reversion_by_currency** | **Dict[str, float]** | Per-currency mean-reversion overrides, keyed by ISO currency code.  A currency absent from this map uses MeanReversion. | [optional] 
**volatility_by_currency** | **Dict[str, float]** | Per-currency short-rate volatility overrides, keyed by ISO currency code.  A currency absent from this map uses Volatility. Short-rate volatility is a per-currency  quantity in practice, so a book spanning several currencies can calibrate each currency  separately instead of sharing a single global figure. | [optional] 
**volatility_multiplier** | **float** | A multiplicative scaling applied to the resolved short-rate volatility - the scalar  Volatility or its per-currency override, whichever applies - at the point of use, e.g. 1.1  prices with the configured volatility raised by ten percent. A single multiplier scales  every per-currency calibration coherently, so a shocked set of options can differ from its  base by this one field rather than a hand-rebuilt volatility (or map of volatilities).  Must not be negative; zero is allowed and prices with a deterministic short rate.  Defaults to 1, which reproduces the configured volatility exactly, when not supplied. | [optional] 
**effective_cs01_bump_width** | **float** | The TOTAL width, as an absolute spread, of the central-difference stencil used for the  option-adjusted Analytic/EffectiveCS01: the two reprice points sit at the solved OAS plus  and minus half of this. The reported figure is normalised to a one-basis-point move  whatever width is configured. Must be strictly positive. Defaults to 0.0001 (1bp, the  market convention for a credit sensitivity) when not supplied. | [optional] 
**effective_key_rate_buckets** | **List[str]** | The maturity buckets of the Analytic/EffectiveKeyRateDuration ladder, as tenor strings  such as \&quot;1Y\&quot; or \&quot;6M\&quot;, in strictly increasing order. Each bucket is repriced under a  tent-shaped curve shift centred on its own tenor, so the ladder sums to the parallel  effective duration to first order. Buckets past an instrument&#39;s maturity report zero, so  one grid can serve a whole book. Defaults to the 1Y, 2Y, 3Y, 5Y, 7Y, 10Y, 20Y, 30Y grid  when not supplied; an empty list is rejected. | [optional] 
**model_options_type** | **str** | Available values: Invalid, OpaqueModelOptions, EmptyModelOptions, IndexModelOptions, FxForwardModelOptions, FundingLegModelOptions, EquityModelOptions, CdsModelOptions, FlexibleLoanPricerOptions, HullWhiteModelOptions, BondLookupModelOptions, BondForwardModelOptions, SimpleModelOptions. | 
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
volatility_multiplier: Optional[Union[StrictFloat, StrictInt]] = # Replace with your value
effective_cs01_bump_width: Optional[Union[StrictFloat, StrictInt]] = # Replace with your value
effective_key_rate_buckets: Optional[List[StrictStr]] = # Replace with your value
model_options_type: StrictStr = "example_model_options_type"
hull_white_model_options_instance = HullWhiteModelOptions(mean_reversion=mean_reversion, volatility=volatility, lattice_steps=lattice_steps, effective_rate_bump_size=effective_rate_bump_size, mean_reversion_by_currency=mean_reversion_by_currency, volatility_by_currency=volatility_by_currency, volatility_multiplier=volatility_multiplier, effective_cs01_bump_width=effective_cs01_bump_width, effective_key_rate_buckets=effective_key_rate_buckets, model_options_type=model_options_type)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

