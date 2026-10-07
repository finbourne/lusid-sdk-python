# ValuationPointDiagnostic

Something found while striking a valuation point that did not stop it but should be looked at.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | What kind of finding this is. &#39;OwnershipDrift&#39;: a fund structure holder&#39;s declared sharing percentage in a held member differs from the share its contributions make of that member&#39;s capital by enough to misallocate more of the period&#39;s P&amp;L than the holder&#39;s drift materiality warning amount allows. | 
**message** | **str** | What was found and what to do about it. | 
**details** | **Dict[str, Optional[str]]** | The values the finding was made on, by name. For &#39;OwnershipDrift&#39;: holder, member, declaredShare, actualShare, delta (actual less declared) and impact (the P&amp;L the drift would misallocate this period). | [optional] 
## Example

```python
from lusid.models.valuation_point_diagnostic import ValuationPointDiagnostic
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

type: StrictStr = "example_type"
message: StrictStr = "example_message"
details: Optional[Dict[str, Optional[StrictStr]]] = # Replace with your value
valuation_point_diagnostic_instance = ValuationPointDiagnostic(type=type, message=message, details=details)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

