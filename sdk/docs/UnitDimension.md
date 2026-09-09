# UnitDimension

One factor of a result's unit, modelled as dimensional analysis rather than a label, e.g. a  rates delta is GBP^1 . GBP.LIBOR.3M^-1 - \"GBP per basis point\". A result's `units` is a  flat list of these; the count tracks the order of the derivative (a ratio), not the result's  axes, and must not be indexed by axis.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**unit_domain** | **str** | The domain this factor is drawn from, e.g. \&quot;Ccy\&quot;, \&quot;Rate\&quot;, \&quot;Vol\&quot;, \&quot;Security\&quot;. | [optional] 
**name** | **str** | The name within the domain, e.g. a currency code or a curve identifier. | [optional] 
**power** | **int** | The exponent this factor is raised to. | [optional] 
**scale** | **float** | The scale of one unit of this factor, e.g. 1e-4 for a basis point. | [optional] 
## Example

```python
from lusid.models.unit_dimension import UnitDimension
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

unit_domain: Optional[StrictStr] = "example_unit_domain"
name: Optional[StrictStr] = "example_name"
power: Optional[StrictInt] = # Replace with your value
power: Optional[StrictInt] = None
scale: Optional[Union[StrictFloat, StrictInt]] = # Replace with your value
unit_dimension_instance = UnitDimension(unit_domain=unit_domain, name=name, power=power, scale=scale)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

