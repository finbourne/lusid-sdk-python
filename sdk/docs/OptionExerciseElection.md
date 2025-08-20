# OptionExerciseElection

Option exercise election.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**election_key** | **str** | Unique key associated to this election | 
**is_default** | **bool** | Is this election automatically applied in the absence of an election having been made. May only be true for one election if multiple are provided. | [optional] 
**is_chosen** | **bool** | Is this the election that has been explicitly chosen from multiple options. | [optional] 
## Example

```python
from lusid.models.option_exercise_election import OptionExerciseElection
from typing import Any, Dict, Optional
from pydantic.v1 import BaseModel, Field, StrictBool, constr

election_key: StrictStr = "example_election_key"
is_default: Optional[StrictBool] = # Replace with your value
is_default:Optional[StrictBool] = None
is_chosen: Optional[StrictBool] = # Replace with your value
is_chosen:Optional[StrictBool] = None
option_exercise_election_instance = OptionExerciseElection(election_key=election_key, is_default=is_default, is_chosen=is_chosen)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

