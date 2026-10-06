# UpdatePropertyDefinitionRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**display_name** | **str** | The display name of the property. | 
**property_description** | **str** | Describes the property | [optional] 
**custom_entity_types** | **List[str]** | The custom entity types that properties relating to this property definition can be applied to. | [optional] 
**value_format** | **str** | The format in which values for this property definition should be represented. Available values: Text, Html. | [optional] 
**qualifier_definitions** | [**List[QualifierDefinitionRequest]**](QualifierDefinitionRequest.md) | The qualifiers declared against this property definition. Omit this field, or supply it as null, to leave the declared qualifiers unchanged. Otherwise the supplied array replaces the stored array in full, so a qualifier omitted from it is no longer declared and can no longer be set, and an empty array clears every declaration. Stored qualifier values are retained in every case and become readable again if the same keys are re-declared with the same data types. | [optional] 
## Example

```python
from lusid.models.update_property_definition_request import UpdatePropertyDefinitionRequest
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

display_name: StrictStr = "example_display_name"
property_description: Optional[StrictStr] = "example_property_description"
custom_entity_types: Optional[List[StrictStr]] = # Replace with your value
value_format: Optional[StrictStr] = "example_value_format"
qualifier_definitions: Optional[List[QualifierDefinitionRequest]] = # Replace with your value
update_property_definition_request_instance = UpdatePropertyDefinitionRequest(display_name=display_name, property_description=property_description, custom_entity_types=custom_entity_types, value_format=value_format, qualifier_definitions=qualifier_definitions)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

