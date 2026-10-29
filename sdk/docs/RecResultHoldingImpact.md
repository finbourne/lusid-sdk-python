# RecResultHoldingImpact

One holding, and where known the tax lot within it, that a transaction or settlement activity item impacted.  Also holds the display names of the holding's instrument.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**holding_id** | **str** | The impacted holding, at holding level: the id a holding item over it carries. | 
**tax_lot_id** | **str** | The impacted tax lot within the holding, where the source states one; null when the impact is known at holding level only. Opaque: compare it whole, do not parse it. | [optional] 
**holding_instrument_scope** | **str** | The scope of the impacted holding&#39;s instrument. Null where the source does not state one. | [optional] 
**holding_lusid_instrument_id** | **str** | The LUID of the impacted holding&#39;s instrument. Null where the source does not state it. | [optional] 
**holding_instrument_name** | **str** | The name of the impacted holding&#39;s instrument, as it stood at the asAt the run read its data. Null where the run did not resolve it. | [optional] 
## Example

```python
from lusid.models.rec_result_holding_impact import RecResultHoldingImpact
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

holding_id: StrictStr = "example_holding_id"
tax_lot_id: Optional[StrictStr] = "example_tax_lot_id"
holding_instrument_scope: Optional[StrictStr] = "example_holding_instrument_scope"
holding_lusid_instrument_id: Optional[StrictStr] = "example_holding_lusid_instrument_id"
holding_instrument_name: Optional[StrictStr] = "example_holding_instrument_name"
rec_result_holding_impact_instance = RecResultHoldingImpact(holding_id=holding_id, tax_lot_id=tax_lot_id, holding_instrument_scope=holding_instrument_scope, holding_lusid_instrument_id=holding_lusid_instrument_id, holding_instrument_name=holding_instrument_name)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

