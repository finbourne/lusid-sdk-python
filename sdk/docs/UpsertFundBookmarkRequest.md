# UpsertFundBookmarkRequest

A definition for the period you wish to close
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bookmark_code** | **str** | Unique code for the Bookmark. | 
**display_name** | **str** | Identifiable Name assigned to the Bookmark. | 
**description** | **str** | Description assigned to the Bookmark. | [optional] 
**effective_at** | **datetime** | The effective time of the Bookmark. | 
**query_as_at** | **datetime** | The query time of the Bookmark. Defaults to latest. | [optional] 
**properties** | [**Dict[str, ModelProperty]**](ModelProperty.md) | A set of properties for the Bookmark. | [optional] 
**holdings_as_at_override** | **datetime** | The optional AsAt Override to use for building holdings in the Bookmark. Defaults to Latest. | [optional] 
**valuations_as_at_override** | **datetime** | The optional AsAt Override to use for performing valuations in the Bookmark. Defaults to Latest. | [optional] 
## Example

```python
from lusid.models.upsert_fund_bookmark_request import UpsertFundBookmarkRequest
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

bookmark_code: StrictStr = "example_bookmark_code"
display_name: StrictStr = "example_display_name"
description: Optional[StrictStr] = "example_description"
effective_at: datetime = # Replace with your value
query_as_at: Optional[datetime] = # Replace with your value
properties: Optional[Dict[str, ModelProperty]] = # Replace with your value
holdings_as_at_override: Optional[datetime] = # Replace with your value
valuations_as_at_override: Optional[datetime] = # Replace with your value
upsert_fund_bookmark_request_instance = UpsertFundBookmarkRequest(bookmark_code=bookmark_code, display_name=display_name, description=description, effective_at=effective_at, query_as_at=query_as_at, properties=properties, holdings_as_at_override=holdings_as_at_override, valuations_as_at_override=valuations_as_at_override)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

