# DecimalList

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**values** | **List[float]** |  | 
**reference_list_type** | **str** | The reference list values. The available values are: PortfolioGroupIdList, PortfolioIdList, AddressKeyList, StringList, InstrumentList, DecimalList, PropertyList, FundIdList | 
## Example

```python
from lusid.models.decimal_list import DecimalList
from typing import Any, Dict, List, Union
from pydantic.v1 import Field, StrictFloat, StrictInt, StrictStr, conlist, validator

values: conlist(Union[StrictFloat, StrictInt], max_items=10000, min_items=0) = Field(...)
reference_list_type: StrictStr = "example_reference_list_type"
decimal_list_instance = DecimalList(values=values, reference_list_type=reference_list_type)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

