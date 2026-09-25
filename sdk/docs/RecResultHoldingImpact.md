# RecResultHoldingImpact

One holding, and where known the tax lot within it, that a transaction or settlement activity item impacted.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**holding_id** | **str** | The impacted holding, at holding level: the id a holding item over it carries. | 
**tax_lot_id** | **str** | The impacted tax lot within the holding, where the source states one; null when the impact is known at holding level only. Opaque: compare it whole, do not parse it. | [optional] 
## Example

```python
from lusid.models.rec_result_holding_impact import RecResultHoldingImpact
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

holding_id: StrictStr = "example_holding_id"
tax_lot_id: Optional[StrictStr] = "example_tax_lot_id"
rec_result_holding_impact_instance = RecResultHoldingImpact(holding_id=holding_id, tax_lot_id=tax_lot_id)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

