# UpsertValuationAddressKeyTemplateRequest

The content of a Valuation Template. An upsert replaces the display name, description and metrics.  If isDefault is not specified, the template keeps its current default flag.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**display_name** | **str** | The name of the Valuation Template. | 
**description** | **str** | A description of the Valuation Template. | [optional] 
**metrics** | [**List[AggregateSpec]**](AggregateSpec.md) | The metrics to calculate in a valuation that uses this template. Each metric is an address key, an operation and optional key options. Valuation Templates do not support returnAs. | 
**is_default** | **bool** | Set to true to make this template the domain default. The previous default stops being the default. Set to false on the current default to use the system default again. If not specified, the template keeps its current value. | [optional] 
## Example

```python
from lusid.models.upsert_valuation_address_key_template_request import UpsertValuationAddressKeyTemplateRequest
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

display_name: StrictStr = "example_display_name"
description: Optional[StrictStr] = "example_description"
metrics: List[AggregateSpec] = # Replace with your value
is_default: Optional[StrictBool] = # Replace with your value
is_default:Optional[StrictBool] = None
upsert_valuation_address_key_template_request_instance = UpsertValuationAddressKeyTemplateRequest(display_name=display_name, description=description, metrics=metrics, is_default=is_default)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

