# FilteredFundIdList

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**filter** | **str** |  | 
**values** | [**List[ResourceId]**](ResourceId.md) |  | [optional] [readonly] 
**nav_type_codes_hint** | **List[str]** |  | [optional] 
**nav_type_selection** | **str** | Available values: First, All. | [optional] 
**resolved_fund_nav_type_codes** | [**List[FundNavTypeCodes]**](FundNavTypeCodes.md) |  | [optional] [readonly] 
**reference_list_type** | **str** | The reference list values. Available values: PortfolioGroupIdList, PortfolioIdList, AddressKeyList, StringList, InstrumentList, DecimalList, PropertyList, FundIdList, FilteredFundIdList. | 
## Example

```python
from lusid.models.filtered_fund_id_list import FilteredFundIdList
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

filter: StrictStr = "example_filter"
values: Optional[List[ResourceId]] = None
nav_type_codes_hint: Optional[List[StrictStr]] = # Replace with your value
nav_type_selection: Optional[StrictStr] = "example_nav_type_selection"
resolved_fund_nav_type_codes: Optional[List[FundNavTypeCodes]] = # Replace with your value
reference_list_type: StrictStr = "example_reference_list_type"
filtered_fund_id_list_instance = FilteredFundIdList(filter=filter, values=values, nav_type_codes_hint=nav_type_codes_hint, nav_type_selection=nav_type_selection, resolved_fund_nav_type_codes=resolved_fund_nav_type_codes, reference_list_type=reference_list_type)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

