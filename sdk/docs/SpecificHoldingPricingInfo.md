# SpecificHoldingPricingInfo

Allows a user to specify fallbacks/overrides using Holding fields for sources that match a particular DependencySourceFilter.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dependency_source_filter** | [**DependencySourceFilter**](DependencySourceFilter.md) |  | 
**field** | **str** | The Holding field which the fallback/override should use to create a price quote. | 
## Example

```python
from lusid.models.specific_holding_pricing_info import SpecificHoldingPricingInfo
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

dependency_source_filter: DependencySourceFilter = # Replace with your value
field: StrictStr = "example_field"
specific_holding_pricing_info_instance = SpecificHoldingPricingInfo(dependency_source_filter=dependency_source_filter, field=field)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

