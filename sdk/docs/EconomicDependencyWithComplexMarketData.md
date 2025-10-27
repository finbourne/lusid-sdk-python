# EconomicDependencyWithComplexMarketData

Container class pairing economic dependency and complex market data (i.e. discounting curves, etc.)
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**economic_dependency** | [**EconomicDependency**](EconomicDependency.md) |  | 
**complex_market_data** | [**ComplexMarketData**](ComplexMarketData.md) |  | 
## Example

```python
from lusid.models.economic_dependency_with_complex_market_data import EconomicDependencyWithComplexMarketData
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

economic_dependency: EconomicDependency = # Replace with your value
complex_market_data: ComplexMarketData = # Replace with your value
economic_dependency_with_complex_market_data_instance = EconomicDependencyWithComplexMarketData(economic_dependency=economic_dependency, complex_market_data=complex_market_data)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

