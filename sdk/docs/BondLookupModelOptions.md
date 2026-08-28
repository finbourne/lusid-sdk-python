# BondLookupModelOptions

Model options for the quote-anchored bond lookup pricer.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**spread_anchored_risk** | **bool** | Price the bond by discounting its own cashflows over its discounting curve at a constant  spread, instead of marking it to its quoted price. Marking to a quote declares no curve  dependency, so a lookup-priced bond reports no curve delta at all. In this mode the pricer  declares both the discounting curve and a ZSpread quote for the instrument and prices off  them, so holding the spread fixed while the curve is perturbed produces the curve&#39;s delta.  Off by default, as the mode changes both the declared dependencies and where the price  comes from. | 
**model_options_type** | **str** | Available values: Invalid, OpaqueModelOptions, EmptyModelOptions, IndexModelOptions, FxForwardModelOptions, FundingLegModelOptions, EquityModelOptions, CdsModelOptions, FlexibleLoanPricerOptions, HullWhiteModelOptions, BondLookupModelOptions. | 
## Example

```python
from lusid.models.bond_lookup_model_options import BondLookupModelOptions
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

spread_anchored_risk: StrictBool = # Replace with your value
spread_anchored_risk:StrictBool = True
model_options_type: StrictStr = "example_model_options_type"
bond_lookup_model_options_instance = BondLookupModelOptions(spread_anchored_risk=spread_anchored_risk, model_options_type=model_options_type)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

