# SideConfigurationDataRequest

Configuration needed to define a side. Sides are referenced by Label. Beyond that, other properties  can be used to reference either transaction fields, or transaction properties.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**side** | **str** | The side&#39;s label. | 
**security** | **str** | The security, or instrument. | 
**currency** | **str** | The currency. | 
**rate** | **str** | The rate. | 
**units** | **str** | The units. | 
**amount** | **str** | The amount. | 
## Example

```python
from lusid.models.side_configuration_data_request import SideConfigurationDataRequest
from typing import Any, Dict
from pydantic.v1 import BaseModel, Field, constr

side: StrictStr = "example_side"
security: StrictStr = "example_security"
currency: StrictStr = "example_currency"
rate: StrictStr = "example_rate"
units: StrictStr = "example_units"
amount: StrictStr = "example_amount"
side_configuration_data_request_instance = SideConfigurationDataRequest(side=side, security=security, currency=currency, rate=rate, units=units, amount=amount)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

