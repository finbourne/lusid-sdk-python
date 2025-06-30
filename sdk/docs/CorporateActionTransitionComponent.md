# CorporateActionTransitionComponent

A single transition component, when grouped with other components a corporate action transition is formed.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**instrument_scope** | **str** | The scope in which the instrument lies. | 
**instrument_identifiers** | **Dict[str, str]** | Unique instrument identifiers | 
**instrument_uid** | **str** | LUSID&#39;s internal unique instrument identifier, resolved from the instrument identifiers | 
**units_factor** | **float** | The factor to scale units by | 
**cost_factor** | **float** | The factor to scale cost by | 
## Example

```python
from lusid.models.corporate_action_transition_component import CorporateActionTransitionComponent
from typing import Any, Dict, Union
from pydantic.v1 import BaseModel, Field, StrictFloat, StrictInt, StrictStr, constr

instrument_scope: StrictStr = "example_instrument_scope"
instrument_identifiers: Dict[str, StrictStr] = # Replace with your value
instrument_uid: StrictStr = "example_instrument_uid"
units_factor: Union[StrictFloat, StrictInt] = # Replace with your value
cost_factor: Union[StrictFloat, StrictInt] = # Replace with your value
corporate_action_transition_component_instance = CorporateActionTransitionComponent(instrument_scope=instrument_scope, instrument_identifiers=instrument_identifiers, instrument_uid=instrument_uid, units_factor=units_factor, cost_factor=cost_factor)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

