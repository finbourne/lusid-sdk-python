# SeriesConfiguration

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**share_class_short_code** | **str** |  | 
**series_launch_price** | **float** |  | [optional] 
**distribution_series_selection** | **str** | Available values: ProRataByNav, FIFO, SpecifiedSeries. | [optional] 
**deal_linked_series** | **bool** |  | [optional] 
## Example

```python
from lusid.models.series_configuration import SeriesConfiguration
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

share_class_short_code: StrictStr = "example_share_class_short_code"
series_launch_price: Optional[Union[StrictFloat, StrictInt]] = # Replace with your value
distribution_series_selection: Optional[StrictStr] = "example_distribution_series_selection"
deal_linked_series: Optional[StrictBool] = # Replace with your value
deal_linked_series:Optional[StrictBool] = None
series_configuration_instance = SeriesConfiguration(share_class_short_code=share_class_short_code, series_launch_price=series_launch_price, distribution_series_selection=distribution_series_selection, deal_linked_series=deal_linked_series)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

