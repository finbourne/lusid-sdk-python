# RelationalDatasetFieldsToAdd

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**series_identifiers** | [**List[CreateSeriesIdentifierField]**](CreateSeriesIdentifierField.md) | The schema defining the structure and data types of the relational dataset. | [optional] 
**value_and_metadata_fields** | [**List[RelationalDatasetFieldDefinition]**](RelationalDatasetFieldDefinition.md) | The schema defining the structure and data types of the relational dataset. | [optional] 
## Example

```python
from lusid.models.relational_dataset_fields_to_add import RelationalDatasetFieldsToAdd
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

series_identifiers: Optional[List[CreateSeriesIdentifierField]] = # Replace with your value
value_and_metadata_fields: Optional[List[RelationalDatasetFieldDefinition]] = # Replace with your value
relational_dataset_fields_to_add_instance = RelationalDatasetFieldsToAdd(series_identifiers=series_identifiers, value_and_metadata_fields=value_and_metadata_fields)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

