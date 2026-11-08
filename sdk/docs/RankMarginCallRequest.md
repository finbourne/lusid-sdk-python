# RankMarginCallRequest

Ranks a margin call's collateral again against the holdings as they stand now, keeping the assets the user chose.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**overrides** | [**List[CollateralAllocationOverride]**](CollateralAllocationOverride.md) | The assets and units the user chose, each validated against the agreement&#39;s constraints and kept with its reason when it fails one. Optional. | [optional] 
**fill_remainder** | **bool** | Whether to fill what the overrides leave uncovered from the ranking, cheapest first. Defaults to true. | [optional] 
## Example

```python
from lusid.models.rank_margin_call_request import RankMarginCallRequest
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

overrides: Optional[List[CollateralAllocationOverride]] = # Replace with your value
fill_remainder: Optional[StrictBool] = # Replace with your value
fill_remainder:Optional[StrictBool] = None
rank_margin_call_request_instance = RankMarginCallRequest(overrides=overrides, fill_remainder=fill_remainder)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

