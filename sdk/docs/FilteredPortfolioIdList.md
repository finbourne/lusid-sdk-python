# FilteredPortfolioIdList

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**filter** | **str** | The filter that selects the portfolios in the list. It is stored as given and resolved against the portfolios the caller is entitled to see each time the list is read. Supports portfolio fields (e.g. id.scope, displayName, type) and portfolio properties (e.g. properties[Portfolio/MyScope/Strategy] eq &#39;Equity&#39;). Relationship filters are not supported. Time-variant properties are evaluated at the asAt of the request; there is no effectiveAt. On upsert the filter must resolve successfully. | 
**values** | [**List[ResourceId]**](ResourceId.md) | The ids of the portfolios the filter resolved to when the list was read. Read only; must not be supplied on upsert. | [optional] [readonly] 
**reference_list_type** | **str** | The reference list values. Available values: PortfolioGroupIdList, PortfolioIdList, AddressKeyList, StringList, InstrumentList, DecimalList, PropertyList, FundIdList, FilteredFundIdList, FilteredPortfolioIdList. | 
## Example

```python
from lusid.models.filtered_portfolio_id_list import FilteredPortfolioIdList
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

filter: StrictStr = "example_filter"
values: Optional[List[ResourceId]] = # Replace with your value
reference_list_type: StrictStr = "example_reference_list_type"
filtered_portfolio_id_list_instance = FilteredPortfolioIdList(filter=filter, values=values, reference_list_type=reference_list_type)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

