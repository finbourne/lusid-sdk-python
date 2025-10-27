# PortfolioIdList

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**values** | [**List[ResourceId]**](ResourceId.md) |  | 
**reference_list_type** | **str** | The reference list values. The available values are: PortfolioGroupIdList, PortfolioIdList, AddressKeyList, StringList, InstrumentList, DecimalList, PropertyList, FundIdList | 
## Example

```python
from lusid.models.portfolio_id_list import PortfolioIdList
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

values: List[ResourceId]
reference_list_type: StrictStr = "example_reference_list_type"
portfolio_id_list_instance = PortfolioIdList(values=values, reference_list_type=reference_list_type)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

