# SwingBaseline

The price a Single fund's dealing price starts from before any swing.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**source** | **str** | The price the dealing price starts from: Mid, the share class unit price, or Bid or Offer, the share class price that the valuation recipe of each active NAV type publishes on that side. Available values: Mid, Bid, Offer. | 
**include_ndc** | **bool** | Whether a Bid or Offer baseline reads the price including notional dealing costs, which needs the NAV type to have a notional dealing cost table. Required for a Bid or Offer baseline and must be omitted for a Mid baseline. | [optional] 
## Example

```python
from lusid.models.swing_baseline import SwingBaseline
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

source: StrictStr = "example_source"
include_ndc: Optional[StrictBool] = # Replace with your value
include_ndc:Optional[StrictBool] = None
swing_baseline_instance = SwingBaseline(source=source, include_ndc=include_ndc)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

