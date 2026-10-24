# RecDefinitionDetails

Base class for the part of a rec definition whose shape depends on what it reconciles. Polymorphic by  definitionType; each supported type has a corresponding inherited class.
## Example

```python
from lusid.models.rec_definition_details import RecDefinitionDetails
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

# Example with RecDefinitionDetails 

external_rec_definition_details_instance = lusid.models.external_rec_definition_details.ExternalRecDefinitionDetails(
                        matching_ruleset_id = lusid.models.resource_id.ResourceId(
                            scope = '', 
                            code = '', ), 
                        left_filter = '', 
                        right_filter = '', 
                        definition_type = '', )

rec_definition_details_instance = RecDefinitionDetails(external_rec_definition_details_instance)

```
See all compatible oneOf types with RecDefinitionDetails


 * [LusidEntityRecDefinitionDetails](./LusidEntityRecDefinitionDetails.md)

 * [PortfolioContentsRecDefinitionDetails](./PortfolioContentsRecDefinitionDetails.md)

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

