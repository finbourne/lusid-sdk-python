# EconomicDependencyWithQuote

Container class pairing economic dependencies and quote data
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**economic_dependency** | [**EconomicDependency**](EconomicDependency.md) |  | 
**metric_value** | [**MetricValue**](MetricValue.md) |  | 
**scale_factor** | **float** | Scale factor for the quote - this can be null, in which case we default to 1. | [optional] 
## Example

```python
from lusid.models.economic_dependency_with_quote import EconomicDependencyWithQuote
from typing import Any, Dict, Optional, Union
from pydantic.v1 import BaseModel, Field, StrictFloat, StrictInt

economic_dependency: EconomicDependency = # Replace with your value
metric_value: MetricValue = # Replace with your value
scale_factor: Optional[Union[StrictFloat, StrictInt]] = # Replace with your value
economic_dependency_with_quote_instance = EconomicDependencyWithQuote(economic_dependency=economic_dependency, metric_value=metric_value, scale_factor=scale_factor)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

