# QualifierDefinition

A qualifier as returned on read: the request shape plus the value type resolved from its data type.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** | The key by which the qualifier is addressed, for example &#39;direction&#39;. Addressed in filters, sort orders and derivation formulae as Properties[{propertyKey}].Qualifiers[{qualifierKey}]. Validated under the same rules as a property code. | [optional] 
**display_name** | **str** | The display name of the qualifier. | [optional] 
**description** | **str** | Describes the qualifier. Optional; null where not supplied. | [optional] 
**data_type_id** | [**ResourceId**](ResourceId.md) |  | [optional] 
**value_type** | **str** | The type of value this qualifier carries, resolved from its data type. Available values: String, Int, Decimal, DateTime, Boolean, Map, List, PropertyArray, Percentage, Code, Id, Uri, CurrencyAndAmount, TradePrice, Currency, MetricValue, ResourceId, ResultValue, CutLocalTime, DateOrCutLabel, UnindexedText. | [optional] 
**is_required** | **bool** | Whether a value for this qualifier must be supplied when a value of the property is written. Defaults to false, and is returned as a boolean rather than as null. Validated on write only, so setting it true does not retroactively invalidate values stored before the change. | [optional] 
## Example

```python
from lusid.models.qualifier_definition import QualifierDefinition
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

key: Optional[StrictStr] = "example_key"
display_name: Optional[StrictStr] = "example_display_name"
description: Optional[StrictStr] = "example_description"
data_type_id: Optional[ResourceId] = # Replace with your value
value_type: Optional[StrictStr] = "example_value_type"
is_required: Optional[StrictBool] = # Replace with your value
is_required:Optional[StrictBool] = None
qualifier_definition_instance = QualifierDefinition(key=key, display_name=display_name, description=description, data_type_id=data_type_id, value_type=value_type, is_required=is_required)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

