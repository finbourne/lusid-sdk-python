# RecDatasetSchema

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | The kind of dataset this side draws on. One of: PortfolioContents, LusidEntity, RelationalData. At most one side may be RelationalData. Available values: PortfolioContents, LusidEntity, RelationalData. | 
**entity_type** | **str** | The entity within the dataset. Required when type is PortfolioContents, in which case it is one of: Holding, Valuation, Transaction, OutputTransaction, SettlementActivity. Must be omitted when type is RelationalData. Available values: Holding, Valuation, Transaction, OutputTransaction, SettlementActivity. | [optional] 
**relational_dataset_definition_id** | [**ResourceId**](ResourceId.md) |  | [optional] 
## Example

```python
from lusid.models.rec_dataset_schema import RecDatasetSchema
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

type: StrictStr = "example_type"
entity_type: Optional[StrictStr] = "example_entity_type"
relational_dataset_definition_id: Optional[ResourceId] = # Replace with your value
rec_dataset_schema_instance = RecDatasetSchema(type=type, entity_type=entity_type, relational_dataset_definition_id=relational_dataset_definition_id)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

