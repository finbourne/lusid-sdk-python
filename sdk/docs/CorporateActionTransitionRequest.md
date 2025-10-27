# CorporateActionTransitionRequest

A 'transition' within a corporate action, representing a set of output movements paired to a single input position
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**input_transition** | [**CorporateActionTransitionComponentRequest**](CorporateActionTransitionComponentRequest.md) |  | [optional] 
**output_transitions** | [**List[CorporateActionTransitionComponentRequest]**](CorporateActionTransitionComponentRequest.md) |  | [optional] 
## Example

```python
from lusid.models.corporate_action_transition_request import CorporateActionTransitionRequest
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

input_transition: Optional[CorporateActionTransitionComponentRequest] = # Replace with your value
output_transitions: Optional[List[CorporateActionTransitionComponentRequest]] = # Replace with your value
corporate_action_transition_request_instance = CorporateActionTransitionRequest(input_transition=input_transition, output_transitions=output_transitions)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

