# Series

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**series_identifier** | **str** | The identifier that uniquely identifies this Series within the Share Class. | 
**series_type** | **str** | The type of the Series. Valid values are: Lead, Standard. | 
**launch_date** | **datetime** | The date on which the Series was launched. | 
**launch_price_type** | **str** | The type of launch price for the Series. Valid values are: Manual, Calculated. | 
**dom_ccy** | **str** | The denomination currency of the Series. | 
**properties** | [**Dict[str, ModelProperty]**](ModelProperty.md) | An optional set of properties to associate with the Series. Only applied if createInstrument is set to true on the parent Fund. | [optional] 
## Example

```python
from lusid.models.series import Series
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

series_identifier: StrictStr = "example_series_identifier"
series_type: StrictStr = "example_series_type"
launch_date: datetime = # Replace with your value
launch_price_type: StrictStr = "example_launch_price_type"
dom_ccy: StrictStr = "example_dom_ccy"
properties: Optional[Dict[str, ModelProperty]] = # Replace with your value
series_instance = Series(series_identifier=series_identifier, series_type=series_type, launch_date=launch_date, launch_price_type=launch_price_type, dom_ccy=dom_ccy, properties=properties)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

