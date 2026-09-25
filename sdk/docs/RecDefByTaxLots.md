# RecDefByTaxLots

Per-side tax-lot granularity for a Holding entry of a rec definition's rulesets.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**left** | **bool** | Whether the left side splits holdings by tax lot. Must be omitted when the left side is relational, and reads as null there. | [optional] 
**right** | **bool** | Whether the right side splits holdings by tax lot. Must be omitted when the right side is relational, and reads as null there. | [optional] 
## Example

```python
from lusid.models.rec_def_by_tax_lots import RecDefByTaxLots
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

left: Optional[StrictBool] = # Replace with your value
left:Optional[StrictBool] = None
right: Optional[StrictBool] = # Replace with your value
right:Optional[StrictBool] = None
rec_def_by_tax_lots_instance = RecDefByTaxLots(left=left, right=right)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

