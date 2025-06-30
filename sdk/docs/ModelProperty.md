# ModelProperty

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** | The key of the property. This takes the format {domain}/{scope}/{code} e.g. &#39;Instrument/system/Name&#39; or &#39;Transaction/strategy/quantsignal&#39;. | 
**value** | [**PropertyValue**](PropertyValue.md) |  | [optional] 
**effective_from** | **datetime** | The effective datetime from which the property is valid. | [optional] 
**effective_until** | **datetime** | The effective datetime until which the property is valid. If not supplied this will be valid indefinitely, or until the next &#39;effectiveFrom&#39; datetime of the property. | [optional] 
**reference_data** | [**Dict[str, PropertyReferenceDataValue]**](PropertyReferenceDataValue.md) | The ReferenceData linked to the value of the property. The ReferenceData is taken from the DataType on the PropertyDefinition that defines the property. | [optional] [readonly] 
## Example

```python
from lusid.models.model_property import ModelProperty
from typing import Any, Dict, Optional
from pydantic.v1 import BaseModel, Field, StrictStr
from datetime import datetime
key: StrictStr = "example_key"
value: Optional[PropertyValue] = None
effective_from: Optional[datetime] = # Replace with your value
effective_until: Optional[datetime] = # Replace with your value
reference_data: Optional[Dict[str, PropertyReferenceDataValue]] = # Replace with your value
model_property_instance = ModelProperty(key=key, value=value, effective_from=effective_from, effective_until=effective_until, reference_data=reference_data)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

