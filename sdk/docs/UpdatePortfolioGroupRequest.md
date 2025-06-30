# UpdatePortfolioGroupRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**display_name** | **str** | The name of the portfolio group. | 
**description** | **str** | A long form description of the portfolio group. | [optional] 
## Example

```python
from lusid.models.update_portfolio_group_request import UpdatePortfolioGroupRequest
from typing import Any, Dict, Optional
from pydantic.v1 import BaseModel, Field, StrictStr, constr

display_name: StrictStr = "example_display_name"
description: Optional[StrictStr] = "example_description"
update_portfolio_group_request_instance = UpdatePortfolioGroupRequest(display_name=display_name, description=description)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

