# UpdatePortfolioRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**display_name** | **str** | The name of the transaction portfolio. | 
**description** | **str** | The description of the transaction portfolio. | [optional] 
## Example

```python
from lusid.models.update_portfolio_request import UpdatePortfolioRequest
from typing import Any, Dict, Optional
from pydantic.v1 import BaseModel, Field, StrictStr, constr

display_name: StrictStr = "example_display_name"
description: Optional[StrictStr] = "example_description"
update_portfolio_request_instance = UpdatePortfolioRequest(display_name=display_name, description=description)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

