# ExternalRecDefinitionDetails

A definition reconciling relational data on both sides, driven by a single External matching ruleset.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**matching_ruleset_id** | [**ResourceId**](ResourceId.md) |  | 
**left_filter** | **str** | Optional filter over the left dataset&#39;s rows, in the dataset&#39;s own grammar, e.g. \&quot;Values[custodian] eq &#39;something&#39;\&quot;. | [optional] 
**right_filter** | **str** | Optional filter over the right dataset&#39;s rows, in the dataset&#39;s own grammar. | [optional] 
**definition_type** | **str** | What this definition reconciles, and so which shape of details it carries. Available values: PortfolioContents, LusidEntity, External. | 
## Example

```python
from lusid.models.external_rec_definition_details import ExternalRecDefinitionDetails
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

matching_ruleset_id: ResourceId = # Replace with your value
left_filter: Optional[StrictStr] = "example_left_filter"
right_filter: Optional[StrictStr] = "example_right_filter"
definition_type: StrictStr = "example_definition_type"
external_rec_definition_details_instance = ExternalRecDefinitionDetails(matching_ruleset_id=matching_ruleset_id, left_filter=left_filter, right_filter=right_filter, definition_type=definition_type)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

