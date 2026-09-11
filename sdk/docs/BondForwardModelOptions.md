# BondForwardModelOptions

Model options for bond forward pricing.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bond_forward_projection_type** | **str** | Determines how the forward price of the deliverable bond is projected to the settlement date.                Supported string (enumeration) values are: [QuotedContractPrice, ForwardProjectedFromFundingCurve,  DeliverableSpreadAnchoredToQuote].  Defaults to QuotedContractPrice - the original quote-driven behaviour - when not supplied, so  options persisted before this property existed keep the behaviour they were saved under.                ForwardProjectedFromFundingCurve carries the deliverable&#39;s quoted dirty spot to settlement on the  discount curve. DeliverableSpreadAnchoredToQuote does the same carry but models that spot as well,  off the spread anchored for the deliverable in the base market, which is what gives the forward  the deliverable&#39;s own curve delta rather than only the carry&#39;s - the larger of the two terms. It  requires the deliverable to be a mastered Bond or ComplexBond settling in the forward&#39;s own  currency, and a credit-spread curve or ZSpread quote to be resolvable for it. | [optional] 
**model_options_type** | **str** | Available values: Invalid, OpaqueModelOptions, EmptyModelOptions, IndexModelOptions, FxForwardModelOptions, FundingLegModelOptions, EquityModelOptions, CdsModelOptions, FlexibleLoanPricerOptions, HullWhiteModelOptions, BondLookupModelOptions, BondForwardModelOptions. | 
## Example

```python
from lusid.models.bond_forward_model_options import BondForwardModelOptions
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

bond_forward_projection_type: Optional[StrictStr] = "example_bond_forward_projection_type"
model_options_type: StrictStr = "example_model_options_type"
bond_forward_model_options_instance = BondForwardModelOptions(bond_forward_projection_type=bond_forward_projection_type, model_options_type=model_options_type)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

