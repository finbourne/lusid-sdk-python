# ElectionSpecification

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**election_type** | **str** |  | 
**cardinality** | **Dict[str, str]** |  | 
**referenced_as** | **List[str]** |  | 
## Example

```python
from lusid.models.election_specification import ElectionSpecification
from typing import Any, Dict, List
from pydantic.v1 import BaseModel, Field, StrictStr, conlist, constr

election_type: StrictStr = "example_election_type"
cardinality: Dict[str, StrictStr] = # Replace with your value
referenced_as: conlist(StrictStr) = # Replace with your value
election_specification_instance = ElectionSpecification(election_type=election_type, cardinality=cardinality, referenced_as=referenced_as)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

