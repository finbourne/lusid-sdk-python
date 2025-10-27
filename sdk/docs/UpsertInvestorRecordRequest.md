# UpsertInvestorRecordRequest

Request to create or update an investor record
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**scope** | **str** | The scope in which the Investor Record lies. | 
**identifiers** | [**Dict[str, ModelProperty]**](ModelProperty.md) | Unique client-defined identifiers of the Investor Record. | 
**properties** | [**Dict[str, ModelProperty]**](ModelProperty.md) | A set of properties associated to the Investor Record. | [optional] 
**display_name** | **str** | The display name of the Investor Record | 
**description** | **str** | The description of the Investor Record | [optional] 
**investor** | [**InvestorIdentifier**](InvestorIdentifier.md) |  | 
## Example

```python
from lusid.models.upsert_investor_record_request import UpsertInvestorRecordRequest
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

scope: StrictStr = "example_scope"
identifiers: Dict[str, ModelProperty] = # Replace with your value
properties: Optional[Dict[str, ModelProperty]] = # Replace with your value
display_name: StrictStr = "example_display_name"
description: Optional[StrictStr] = "example_description"
investor: InvestorIdentifier
upsert_investor_record_request_instance = UpsertInvestorRecordRequest(scope=scope, identifiers=identifiers, properties=properties, display_name=display_name, description=description, investor=investor)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

