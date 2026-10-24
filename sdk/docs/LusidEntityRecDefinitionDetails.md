# LusidEntityRecDefinitionDetails

A definition that reconciles one type of LUSID entity. A filter selects the population of each side, and a single  matching ruleset of that entity type drives the definition.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**entity_type** | **str** | The type of LUSID entity to reconcile, which is also the rec type of the results. Supported types: Instrument. Must equal the reconciliationType of the matching ruleset. Available values: Holding, CashHolding, Valuation, InputTransaction, OutputTransaction, SettlementActivity, External, Instrument. | 
**matching_ruleset_id** | [**ResourceId**](ResourceId.md) |  | 
**left_filter** | **str** | Optional filter that selects the population of the left side, e.g. \&quot;scope eq &#39;default&#39;\&quot;. It resolves against the left side entity fields. Null reads the whole population of the side. | [optional] 
**right_filter** | **str** | Optional filter that selects the population of the right side. It resolves against the right side entity fields. Null reads the whole population of the side. | [optional] 
**definition_type** | **str** | What this definition reconciles, and so which shape of details it carries. Available values: PortfolioContents, LusidEntity, External. | 
## Example

```python
from lusid.models.lusid_entity_rec_definition_details import LusidEntityRecDefinitionDetails
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

entity_type: StrictStr = "example_entity_type"
matching_ruleset_id: ResourceId = # Replace with your value
left_filter: Optional[StrictStr] = "example_left_filter"
right_filter: Optional[StrictStr] = "example_right_filter"
definition_type: StrictStr = "example_definition_type"
lusid_entity_rec_definition_details_instance = LusidEntityRecDefinitionDetails(entity_type=entity_type, matching_ruleset_id=matching_ruleset_id, left_filter=left_filter, right_filter=right_filter, definition_type=definition_type)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

