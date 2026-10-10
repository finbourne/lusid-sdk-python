# ReportingPrice

A share class price a fund publishes at each valuation point under a label of its own, alongside the dealing price.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**source** | **str** | The share class price published: Mid, the unit price, or Bid, Offer, BidIncNdc or OfferIncNdc, as the valuation recipe of each active NAV type publishes it. Available values: Mid, Bid, Offer, BidIncNdc, OfferIncNdc, Creation, Cancellation. | 
**label** | **str** | The name the price is published under in the share class&#39;s reporting prices. Unique within the fund. | 
## Example

```python
from lusid.models.reporting_price import ReportingPrice
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

source: StrictStr = "example_source"
label: StrictStr = "example_label"
reporting_price_instance = ReportingPrice(source=source, label=label)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

