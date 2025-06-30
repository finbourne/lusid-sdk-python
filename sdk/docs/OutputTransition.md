# OutputTransition

A 'transition' within a corporate action, representing an output transition.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**instrument_identifiers** | **Dict[str, str]** | Unique instrument identifiers | 
**units_factor** | **float** | The factor to scale units by | 
**cost_factor** | **float** | The factor to scale cost by | 
**lusid_instrument_id** | **str** | LUSID&#39;s internal unique instrument identifier, resolved from the instrument identifiers | [optional] [readonly] 
**instrument_scope** | **str** | The scope in which the instrument lies. | [optional] [readonly] 
**rounding** | [**RoundingConfiguration**](RoundingConfiguration.md) |  | [optional] 
## Example

```python
from lusid.models.output_transition import OutputTransition
from typing import Any, Dict, Optional, Union
from pydantic.v1 import BaseModel, Field, StrictFloat, StrictInt, StrictStr

instrument_identifiers: Dict[str, StrictStr] = # Replace with your value
units_factor: Union[StrictFloat, StrictInt] = # Replace with your value
cost_factor: Union[StrictFloat, StrictInt] = # Replace with your value
lusid_instrument_id: Optional[StrictStr] = "example_lusid_instrument_id"
instrument_scope: Optional[StrictStr] = "example_instrument_scope"
rounding: Optional[RoundingConfiguration] = None
output_transition_instance = OutputTransition(instrument_identifiers=instrument_identifiers, units_factor=units_factor, cost_factor=cost_factor, lusid_instrument_id=lusid_instrument_id, instrument_scope=instrument_scope, rounding=rounding)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

