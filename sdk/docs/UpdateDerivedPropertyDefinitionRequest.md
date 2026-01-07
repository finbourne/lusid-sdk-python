# UpdateDerivedPropertyDefinitionRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**display_name** | **str** | The display name of the property. | 
**data_type_id** | [**ResourceId**](ResourceId.md) |  | 
**property_description** | **str** | Describes the property | [optional] 
**derivation_formula** | **str** | The rule that defines how data is composed for a derived property. | 
**is_filterable** | **bool** | Bool indicating whether the values of this property are fitlerable, this is true for all non-derived property defintions.  For a derived definition this must be set true to enable filtering. | 
**value_format** | **str** | The format in which values for this property definition should be represented. | [optional] 
**custom_entity_type** | **str** | The custom entity type that this derived property definition can be applied to. | [optional] 
## Example

```python
from lusid.models.update_derived_property_definition_request import UpdateDerivedPropertyDefinitionRequest
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

display_name: StrictStr = "example_display_name"
data_type_id: ResourceId = # Replace with your value
property_description: Optional[StrictStr] = "example_property_description"
derivation_formula: StrictStr = "example_derivation_formula"
is_filterable: StrictBool = # Replace with your value
is_filterable:StrictBool = True
value_format: Optional[StrictStr] = "example_value_format"
custom_entity_type: Optional[StrictStr] = "example_custom_entity_type"
update_derived_property_definition_request_instance = UpdateDerivedPropertyDefinitionRequest(display_name=display_name, data_type_id=data_type_id, property_description=property_description, derivation_formula=derivation_formula, is_filterable=is_filterable, value_format=value_format, custom_entity_type=custom_entity_type)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

