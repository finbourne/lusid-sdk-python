# FundStructureDriftMateriality

How much ownership drift a Fund Structure member tolerates on the members it holds through an instrument.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**warn_amount** | **float** | The misallocated P&amp;L, in base currency, above which the valuation point carries a warning naming the holder, the held member and both shares. Optional; unset means never warn. | [optional] 
**refuse_amount** | **float** | The misallocated P&amp;L, in base currency, above which the P&amp;L flow is refused until the sharing percentage is corrected. Must not be less than the warning amount. Optional; unset means never refuse. A share bought from another investor at a premium or a discount shows as drift however correct the sharing percentage. | [optional] 
## Example

```python
from lusid.models.fund_structure_drift_materiality import FundStructureDriftMateriality
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

warn_amount: Optional[Union[StrictFloat, StrictInt]] = # Replace with your value
refuse_amount: Optional[Union[StrictFloat, StrictInt]] = # Replace with your value
fund_structure_drift_materiality_instance = FundStructureDriftMateriality(warn_amount=warn_amount, refuse_amount=refuse_amount)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

