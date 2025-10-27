# DataMapping

When importing data from an external source there are essentially three levels of interaction with LUSID.  (1) The data is a raw document that LUSID does not understand. You can store and retrieve it but it does not full interact with other documents inside LUSID  (2) The data has a map from fields and paths to 'properties' in LUSID. In essence, LUSID can then treat the data as weakly typed (decimal, string) data that can be returned through queries      and where various aggregation requests will then work.  (3) The data is fully translatable into LUSID and understood, in some sense, natively. This means that it can be used for context sensitive calculations such as pricing or risk calculations.  The data map object is designed to allow data to transition from step 1 to 2 and in some cases as an alternative for step 2 to 3.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data_definitions** | [**List[DataDefinition]**](DataDefinition.md) | A map from LUSID item keys to data definitions that define the names, types and degree of uniqueness of data provided to LUSID in structured data stores. | [optional] 
## Example

```python
from lusid.models.data_mapping import DataMapping
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

data_definitions: Optional[List[DataDefinition]] = # Replace with your value
data_mapping_instance = DataMapping(data_definitions=data_definitions)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

