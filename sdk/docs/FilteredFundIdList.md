# FilteredFundIdList

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**filter** | **str** |  | 
**values** | [**List[ResourceId]**](ResourceId.md) |  | [optional] [readonly] 
**reference_list_type** | **str** | The reference list values. The available values are: PortfolioGroupIdList, PortfolioIdList, AddressKeyList, StringList, InstrumentList, DecimalList, PropertyList, FundIdList, FilteredFundIdList | 
## Example

```python
from lusid.models.filtered_fund_id_list import FilteredFundIdList
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

filter: StrictStr = "example_filter"
values: Optional[List[ResourceId]] = None
reference_list_type: StrictStr = "example_reference_list_type"
filtered_fund_id_list_instance = FilteredFundIdList(filter=filter, values=values, reference_list_type=reference_list_type)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

