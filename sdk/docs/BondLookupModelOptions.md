# BondLookupModelOptions

Model options for the quote-anchored bond lookup pricer.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**spread_anchored_risk** | **bool** | Price the bond by discounting its own cashflows over its discounting curve at a constant  spread, instead of marking it to its quoted price. Marking to a quote declares no curve  dependency, so a lookup-priced bond reports no curve delta at all. In this mode the pricer  declares both the discounting curve and a ZSpread quote for the instrument and prices off  them, so holding the spread fixed while the curve is perturbed produces the curve&#39;s delta.  The anchor may also be served as a per-instrument CreditSpreadCurve complex market data  document (rule key Credit.CreditSpreadCurve[.IdentifierType], market asset  CreditSpreadCurve/&lt;identifier&gt;), which takes precedence over the quote when present.  Only the spread at the bond&#39;s maturity is read off it; the document&#39;s recoveryRate is not  used by this pricer.  Off by default, as the mode changes both the declared dependencies and where the price  comes from. | 
**cs01_bump_width** | **float** | The TOTAL width of the central-difference stencil behind the CS01/Central measure: the  instrument&#39;s own z-spread is repriced at spread ± width/2, so a width of 0.0001 means  ±0.5bp reprice points. The width is the whole distance between the two reprice points,  NOT the half-shift. The reported measure is always per one basis point of widening  whatever width is configured. Must be strictly positive.  Defaults to 0.0001 (1bp, repriced at ±0.5bp) when not supplied. | [optional] 
**spread_anchor_source** | **str** | Where the spread anchor comes from when no CreditSpreadCurve is served for the instrument. Only  read when SpreadAnchoredRisk is true.                Supported string (enumeration) values are: [MarketData, SolvedFromPrice].  Defaults to MarketData - the original behaviour, where a ZSpread quote must be served from the  quote store or as a market data override - when not supplied.                SolvedFromPrice: a served CreditSpreadCurve or ZSpread quote still wins. When neither is served,  the bond is valued exactly as the plain lookup values it, and the anchor is the z-spread its  looked-up price implies over the discounting curve (the value Analytic/ZSpread returns). Risk  measures, carry and scenario columns solve that anchor against the unperturbed market and hold it,  so no spread has to be stored or sent. | [optional] 
**spread_term_structure** | **bool** | In spread-anchored mode with a credit-spread curve (a served CreditSpreadCurve, or the curve the  risk engine builds from the ZSpread quote), discount each cash flow at the curve&#39;s level on its own  payment date instead of discounting every flow at the level at maturity. Pointwise and bucketed  Risk/Credit ladders then split CS01 by cash flow, and the curve built from a quote carries one pillar  per remaining payment date. The price is unchanged on a flat curve (and so on any curve built from a  quote) but not on a sloped served curve.  Defaults to false - the level at maturity - when not supplied. | [optional] 
**model_options_type** | **str** | Available values: Invalid, OpaqueModelOptions, EmptyModelOptions, IndexModelOptions, FxForwardModelOptions, FundingLegModelOptions, EquityModelOptions, CdsModelOptions, FlexibleLoanPricerOptions, HullWhiteModelOptions, BondLookupModelOptions, BondForwardModelOptions, SimpleModelOptions. | 
## Example

```python
from lusid.models.bond_lookup_model_options import BondLookupModelOptions
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

spread_anchored_risk: StrictBool = # Replace with your value
spread_anchored_risk:StrictBool = True
cs01_bump_width: Optional[Union[StrictFloat, StrictInt]] = # Replace with your value
spread_anchor_source: Optional[StrictStr] = "example_spread_anchor_source"
spread_term_structure: Optional[StrictBool] = # Replace with your value
spread_term_structure:Optional[StrictBool] = None
model_options_type: StrictStr = "example_model_options_type"
bond_lookup_model_options_instance = BondLookupModelOptions(spread_anchored_risk=spread_anchored_risk, cs01_bump_width=cs01_bump_width, spread_anchor_source=spread_anchor_source, spread_term_structure=spread_term_structure, model_options_type=model_options_type)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

