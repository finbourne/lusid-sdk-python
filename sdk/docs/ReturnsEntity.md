# ReturnsEntity

Returns entity, used for configuring the calculation of aggregated returns.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | [**ResourceId**](ResourceId.md) |  | 
**recipe_id** | [**ResourceId**](ResourceId.md) |  | [optional] 
**recipe_entity** | **str** | Entity a recipe is retrieved from for use in the aggregated returns calculation. Either RecipeId or RecipeEntity must be specified. | [optional] 
**fee_handling** | **str** | Configures how fees are handled in the aggregated returns calculation. | [optional] 
**flow_handling** | **str** | Configures how flows are handled in the aggregated returns calculation. | [optional] 
**business_calendar** | **str** | Calendar used in the aggregated returns calculation. | [optional] 
**handle_flow_discrepancy** | **str** | Configures handling for the case where net flows do not match the sum of tagged flows. | [optional] 
## Example

```python
from lusid.models.returns_entity import ReturnsEntity
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

id: ResourceId
recipe_id: Optional[ResourceId] = # Replace with your value
recipe_entity: Optional[StrictStr] = "example_recipe_entity"
fee_handling: Optional[StrictStr] = "example_fee_handling"
flow_handling: Optional[StrictStr] = "example_flow_handling"
business_calendar: Optional[StrictStr] = "example_business_calendar"
handle_flow_discrepancy: Optional[StrictStr] = "example_handle_flow_discrepancy"
returns_entity_instance = ReturnsEntity(id=id, recipe_id=recipe_id, recipe_entity=recipe_entity, fee_handling=fee_handling, flow_handling=flow_handling, business_calendar=business_calendar, handle_flow_discrepancy=handle_flow_discrepancy)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

