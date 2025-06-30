# SideConfigurationData

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
**links** | [**List[Link]**](Link.md) |  | [optional] 
## Example

```python
from lusid.models.side_configuration_data import SideConfigurationData
from typing import Any, Dict, List, Optional
from pydantic.v1 import BaseModel, Field, conlist, constr

side: StrictStr = "example_side"
security: StrictStr = "example_security"
currency: StrictStr = "example_currency"
rate: StrictStr = "example_rate"
units: StrictStr = "example_units"
amount: StrictStr = "example_amount"
links: Optional[conlist(Link)] = None
side_configuration_data_instance = SideConfigurationData(side=side, security=security, currency=currency, rate=rate, units=units, amount=amount, links=links)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

