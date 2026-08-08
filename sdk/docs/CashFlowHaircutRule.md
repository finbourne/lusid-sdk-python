# CashFlowHaircutRule

A rule describing how projected cashflow inflows are reduced by a haircut representing expected  default loss or cost of downgrade, for matching-adjustment and liquidity (Solvency II) analyses.  Rules are matched in request order against each cashflow's instrument and the first matching rule  wins; a rule with no criteria acts as a catch-all. Only inflows are haircut; outflows always pass  through untouched.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**rule_id** | **str** | Optional identifier reported back against cashflows this rule haircut. Defaults to the rule&#39;s position in the list, e.g. &#39;HaircutRules[0]&#39;. | [optional] 
**property_key** | **str** | The instrument property key the rule matches on, e.g. &#39;Instrument/default/CreditRating&#39;. When omitted the rule does not match on a property. | [optional] 
**property_value** | **str** | The instrument property value the rule matches. Required when PropertyKey is supplied. | [optional] 
**instrument_type** | **str** | Optional instrument type filter, e.g. &#39;Bond&#39;. When supplied the rule only matches cashflows from instruments of that type. | [optional] 
**haircut_type** | **str** | The mathematical form of the haircut. One of &#39;CumulativeAnnualised&#39; (net &#x3D; gross x (1 - rate)^t, where t is the ACT/365.25 year fraction from the valuation date to the payment date) or &#39;Flat&#39; (net &#x3D; gross x (1 - h(t)), where h(t) is the flat rate or the term structure rate at t). Available values: CumulativeAnnualised, Flat. | 
**rate** | **float** | The haircut rate as a fraction in the range [0, 1]. Exactly one of Rate and TermStructure must be supplied. | [optional] 
**term_structure** | [**List[CashFlowHaircutTermPoint]**](CashFlowHaircutTermPoint.md) | The haircut rate term structure, linearly interpolated on time-to-payment with flat extrapolation beyond either end. Exactly one of Rate and TermStructure must be supplied. | [optional] 
## Example

```python
from lusid.models.cash_flow_haircut_rule import CashFlowHaircutRule
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

rule_id: Optional[StrictStr] = "example_rule_id"
property_key: Optional[StrictStr] = "example_property_key"
property_value: Optional[StrictStr] = "example_property_value"
instrument_type: Optional[StrictStr] = "example_instrument_type"
haircut_type: StrictStr = "example_haircut_type"
rate: Optional[Union[StrictFloat, StrictInt]] = # Replace with your value
term_structure: Optional[List[CashFlowHaircutTermPoint]] = # Replace with your value
cash_flow_haircut_rule_instance = CashFlowHaircutRule(rule_id=rule_id, property_key=property_key, property_value=property_value, instrument_type=instrument_type, haircut_type=haircut_type, rate=rate, term_structure=term_structure)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

