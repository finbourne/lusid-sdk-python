# UpsertCurrencyGroupRequest

Request body for creating or updating a currency group.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** | The code of the currency group. This uniquely identifies the currency group within the tenant. | 
**display_name** | **str** | The name of the currency group. | 
**description** | **str** | A description for the currency group. | [optional] 
**major_unit_currency** | **str** | The three-letter, case-sensitive currency code of the group&#39;s major unit, e.g. GBP for the sterling group. | 
**circulation_domain** | **str** | The domain in which the group&#39;s currencies circulate, e.g. an ISO 3166 country code. | [optional] 
**minor_units** | [**List[CurrencyGroupMinorUnit]**](CurrencyGroupMinorUnit.md) | The minor unit currencies belonging to this currency group. | [optional] 
## Example

```python
from lusid.models.upsert_currency_group_request import UpsertCurrencyGroupRequest
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

code: StrictStr = "example_code"
display_name: StrictStr = "example_display_name"
description: Optional[StrictStr] = "example_description"
major_unit_currency: StrictStr = "example_major_unit_currency"
circulation_domain: Optional[StrictStr] = "example_circulation_domain"
minor_units: Optional[List[CurrencyGroupMinorUnit]] = # Replace with your value
upsert_currency_group_request_instance = UpsertCurrencyGroupRequest(code=code, display_name=display_name, description=description, major_unit_currency=major_unit_currency, circulation_domain=circulation_domain, minor_units=minor_units)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

