# PropertyReferenceDataValue

The ReferenceData relevant to the property. The ReferenceData is taken from the DataType on the PropertyDefinition that defines the Property.  Only ReferenceData where the ReferenceData value matches the Property value is included.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**string_value** | **str** |  | [optional] 
**numeric_value** | **float** |  | [optional] 
## Example

```python
from lusid.models.property_reference_data_value import PropertyReferenceDataValue
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

string_value: Optional[StrictStr] = "example_string_value"
numeric_value: Optional[Union[StrictFloat, StrictInt]] = # Replace with your value
property_reference_data_value_instance = PropertyReferenceDataValue(string_value=string_value, numeric_value=numeric_value)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

