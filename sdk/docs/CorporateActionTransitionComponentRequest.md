# CorporateActionTransitionComponentRequest

A single transition component request, when grouped with other transition component requests a corporate action transition request is formed.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**instrument_identifiers** | **Dict[str, str]** | Unique instrument identifiers | 
**units_factor** | **float** | The factor to scale units by | 
**cost_factor** | **float** | The factor to scale cost by | 
## Example

```python
from lusid.models.corporate_action_transition_component_request import CorporateActionTransitionComponentRequest
from typing import Any, Dict, Union
from pydantic.v1 import BaseModel, Field, StrictFloat, StrictInt, StrictStr

instrument_identifiers: Dict[str, StrictStr] = # Replace with your value
units_factor: Union[StrictFloat, StrictInt] = # Replace with your value
cost_factor: Union[StrictFloat, StrictInt] = # Replace with your value
corporate_action_transition_component_request_instance = CorporateActionTransitionComponentRequest(instrument_identifiers=instrument_identifiers, units_factor=units_factor, cost_factor=cost_factor)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

