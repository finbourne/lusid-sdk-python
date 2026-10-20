# WithholdingTaxReliefAtSourceFlags

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**treaty_ras** | **bool** | Whether relief at source applies at the treaty rate. | 
**better_ras** | **bool** | Whether relief at source applies at the better rate. | 
**enhanced_ras** | **bool** | Whether relief at source applies at the enhanced rate. | 
## Example

```python
from lusid.models.withholding_tax_relief_at_source_flags import WithholdingTaxReliefAtSourceFlags
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

treaty_ras: StrictBool = # Replace with your value
treaty_ras:StrictBool = True
better_ras: StrictBool = # Replace with your value
better_ras:StrictBool = True
enhanced_ras: StrictBool = # Replace with your value
enhanced_ras:StrictBool = True
withholding_tax_relief_at_source_flags_instance = WithholdingTaxReliefAtSourceFlags(treaty_ras=treaty_ras, better_ras=better_ras, enhanced_ras=enhanced_ras)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

