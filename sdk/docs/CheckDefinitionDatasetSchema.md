# CheckDefinitionDatasetSchema

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | The type of dataset schema that the Check Definition applies to | [optional] 
**entity_type** | **str** | The type of entity that the dataset schema applies to, e.g. Instrument, Transaction, etc. | [optional] 
## Example

```python
from lusid.models.check_definition_dataset_schema import CheckDefinitionDatasetSchema
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

type: Optional[StrictStr] = "example_type"
entity_type: Optional[StrictStr] = "example_entity_type"
check_definition_dataset_schema_instance = CheckDefinitionDatasetSchema(type=type, entity_type=entity_type)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

