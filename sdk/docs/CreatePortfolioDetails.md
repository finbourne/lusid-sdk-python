# CreatePortfolioDetails

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**corporate_action_source_id** | [**ResourceId**](ResourceId.md) |  | [optional] 
## Example

```python
from lusid.models.create_portfolio_details import CreatePortfolioDetails
from typing import Any, Dict, Optional
from pydantic.v1 import BaseModel, Field

corporate_action_source_id: Optional[ResourceId] = # Replace with your value
create_portfolio_details_instance = CreatePortfolioDetails(corporate_action_source_id=corporate_action_source_id)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

