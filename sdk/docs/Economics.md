# Economics

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**instrument_scope** | **str** | The scope in which the instrument lies. | [optional] 
**lusid_instrument_id** | **str** | The unique Lusid Instrument Id (LUID) of the instrument that economics are for. | 
**sub_holding_keys** | [**Dict[str, PerpetualProperty]**](PerpetualProperty.md) | The sub-holding properties which identify the Economic. Each property will be from the &#39;Transaction&#39; domain. These are configured on a transaction portfolio. | [optional] 
**buckets** | [**List[Bucket]**](Bucket.md) | Set of economic data related with each of the side impact of the transaction. | [optional] 
## Example

```python
from lusid.models.economics import Economics
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

instrument_scope: Optional[StrictStr] = "example_instrument_scope"
lusid_instrument_id: StrictStr = "example_lusid_instrument_id"
sub_holding_keys: Optional[Dict[str, PerpetualProperty]] = # Replace with your value
buckets: Optional[List[Bucket]] = # Replace with your value
economics_instance = Economics(instrument_scope=instrument_scope, lusid_instrument_id=lusid_instrument_id, sub_holding_keys=sub_holding_keys, buckets=buckets)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

