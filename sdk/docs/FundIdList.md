# FundIdList

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**values** | [**List[ResourceId]**](ResourceId.md) |  | 
**nav_type_codes_hint** | **List[str]** | The NAV type codes this list nominates, in priority order; entries may contain &#39;*&#39; wildcards.  For each fund the first matching code the fund defines is picked, falling back to the fund&#39;s  primary (official) NAV type when the list is empty or nothing matches. Optional. | [optional] 
**reference_list_type** | **str** | The reference list values. Available values: PortfolioGroupIdList, PortfolioIdList, AddressKeyList, StringList, InstrumentList, DecimalList, PropertyList, FundIdList, FilteredFundIdList. | 
## Example

```python
from lusid.models.fund_id_list import FundIdList
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

values: List[ResourceId]
nav_type_codes_hint: Optional[List[StrictStr]] = # Replace with your value
reference_list_type: StrictStr = "example_reference_list_type"
fund_id_list_instance = FundIdList(values=values, nav_type_codes_hint=nav_type_codes_hint, reference_list_type=reference_list_type)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

