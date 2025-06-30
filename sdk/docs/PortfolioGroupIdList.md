# PortfolioGroupIdList

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**values** | [**List[ResourceId]**](ResourceId.md) |  | 
**reference_list_type** | **str** | The reference list values. The available values are: PortfolioGroupIdList, PortfolioIdList, AddressKeyList, StringList, InstrumentList, DecimalList, PropertyList, FundIdList | 
## Example

```python
from lusid.models.portfolio_group_id_list import PortfolioGroupIdList
from typing import Any, Dict, List
from pydantic.v1 import Field, StrictStr, conlist, validator

values: conlist(ResourceId, max_items=10000) = Field(...)
reference_list_type: StrictStr = "example_reference_list_type"
portfolio_group_id_list_instance = PortfolioGroupIdList(values=values, reference_list_type=reference_list_type)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

