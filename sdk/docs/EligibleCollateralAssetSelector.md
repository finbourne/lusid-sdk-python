# EligibleCollateralAssetSelector

The assets an eligible collateral row applies to, as stored on a schedule.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**kind** | **str** | What the selector matches. One of BaseCurrencyCash, Cash or Instrument. Available values: BaseCurrencyCash, Cash, Instrument. | 
**currency** | **str** | The currency of the cash. Required for a Cash selector and not allowed otherwise. | [optional] 
**instrument_filter** | **str** | A filter selecting the instruments. Required for an Instrument selector and not allowed otherwise. Checked for structure only when the schedule is stored. | [optional] 
## Example

```python
from lusid.models.eligible_collateral_asset_selector import EligibleCollateralAssetSelector
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

kind: StrictStr = "example_kind"
currency: Optional[StrictStr] = "example_currency"
instrument_filter: Optional[StrictStr] = "example_instrument_filter"
eligible_collateral_asset_selector_instance = EligibleCollateralAssetSelector(kind=kind, currency=currency, instrument_filter=instrument_filter)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

