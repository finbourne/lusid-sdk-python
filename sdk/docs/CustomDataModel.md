# CustomDataModel

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data_model_summary** | [**DataModelSummary**](DataModelSummary.md) |  | [optional] 
**inherited** | [**CustomDataModelCriteria**](CustomDataModelCriteria.md) |  | [optional] 
**incremental** | [**CustomDataModelCriteria**](CustomDataModelCriteria.md) |  | [optional] 
**applied** | [**CustomDataModelCriteria**](CustomDataModelCriteria.md) |  | [optional] 
**version** | [**Version**](Version.md) |  | [optional] 
## Example

```python
from lusid.models.custom_data_model import CustomDataModel
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

data_model_summary: Optional[DataModelSummary] = # Replace with your value
inherited: Optional[CustomDataModelCriteria] = None
incremental: Optional[CustomDataModelCriteria] = None
applied: Optional[CustomDataModelCriteria] = None
version: Optional[Version] = None
custom_data_model_instance = CustomDataModel(data_model_summary=data_model_summary, inherited=inherited, incremental=incremental, applied=applied, version=version)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

