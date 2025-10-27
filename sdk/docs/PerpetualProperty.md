# PerpetualProperty

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** | The key of the property. This takes the format {domain}/{scope}/{code} e.g. &#39;Instrument/system/Name&#39; or &#39;Transaction/strategy/quantsignal&#39;. | 
**value** | [**PropertyValue**](PropertyValue.md) |  | [optional] 
**reference_data** | [**Dict[str, PropertyReferenceDataValue]**](PropertyReferenceDataValue.md) | The ReferenceData linked to the value of the property. The ReferenceData is taken from the DataType on the PropertyDefinition that defines the property. | [optional] [readonly] 
## Example

```python
from lusid.models.perpetual_property import PerpetualProperty
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

key: StrictStr = "example_key"
value: Optional[PropertyValue] = None
reference_data: Optional[Dict[str, PropertyReferenceDataValue]] = # Replace with your value
perpetual_property_instance = PerpetualProperty(key=key, value=value, reference_data=reference_data)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

