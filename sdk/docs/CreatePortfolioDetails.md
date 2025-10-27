# CreatePortfolioDetails

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**corporate_action_source_id** | [**ResourceId**](ResourceId.md) |  | [optional] 
## Example

```python
from lusid.models.create_portfolio_details import CreatePortfolioDetails
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

corporate_action_source_id: Optional[ResourceId] = # Replace with your value
create_portfolio_details_instance = CreatePortfolioDetails(corporate_action_source_id=corporate_action_source_id)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

