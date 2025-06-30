# UpdateDerivedPropertyDefinitionRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**display_name** | **str** | The display name of the property. | 
**data_type_id** | [**ResourceId**](ResourceId.md) |  | 
**property_description** | **str** | Describes the property | [optional] 
**derivation_formula** | **str** | The rule that defines how data is composed for a derived property. | 
**is_filterable** | **bool** | Bool indicating whether the values of this property are fitlerable, this is true for all non-derived property defintions.  For a derived definition this must be set true to enable filtering. | 
## Example

```python
from lusid.models.update_derived_property_definition_request import UpdateDerivedPropertyDefinitionRequest
from typing import Any, Dict, Optional
from pydantic.v1 import BaseModel, Field, StrictBool, constr

display_name: StrictStr = "example_display_name"
data_type_id: ResourceId = # Replace with your value
property_description: Optional[StrictStr] = "example_property_description"
derivation_formula: StrictStr = "example_derivation_formula"
is_filterable: StrictBool = # Replace with your value
is_filterable:StrictBool = True
update_derived_property_definition_request_instance = UpdateDerivedPropertyDefinitionRequest(display_name=display_name, data_type_id=data_type_id, property_description=property_description, derivation_formula=derivation_formula, is_filterable=is_filterable)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

