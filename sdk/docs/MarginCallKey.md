# MarginCallKey

The parts that identify a margin call: its run and the call's business key.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**run_id** | **str** | The run the call belongs to. | 
**agreement_scope** | **str** | The scope of the call&#39;s collateral agreement. | 
**agreement_code** | **str** | The code of the call&#39;s collateral agreement. | 
**item** | **str** | The margin item of the call. | 
**margin_type** | **str** | The margin type of the call. Currently VariationMargin. | 
**direction** | **str** | Who posts under the call: WePost, TheyPost or None. | 
## Example

```python
from lusid.models.margin_call_key import MarginCallKey
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

run_id: StrictStr = "example_run_id"
agreement_scope: StrictStr = "example_agreement_scope"
agreement_code: StrictStr = "example_agreement_code"
item: StrictStr = "example_item"
margin_type: StrictStr = "example_margin_type"
direction: StrictStr = "example_direction"
margin_call_key_instance = MarginCallKey(run_id=run_id, agreement_scope=agreement_scope, agreement_code=agreement_code, item=item, margin_type=margin_type, direction=direction)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

