# ChartOfAccountsRequest

The request used to create a chart of account.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** | The code given for the Chart of Accounts. | 
**display_name** | **str** | The name of the Chart of Account. | [optional] 
**description** | **str** | A description of the Chart of Accounts. | [optional] 
**properties** | [**Dict[str, ModelProperty]**](ModelProperty.md) | A set of properties for the Chart of Accounts. | [optional] 
## Example

```python
from lusid.models.chart_of_accounts_request import ChartOfAccountsRequest
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

code: StrictStr = "example_code"
display_name: Optional[StrictStr] = "example_display_name"
description: Optional[StrictStr] = "example_description"
properties: Optional[Dict[str, ModelProperty]] = # Replace with your value
chart_of_accounts_request_instance = ChartOfAccountsRequest(code=code, display_name=display_name, description=description, properties=properties)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

