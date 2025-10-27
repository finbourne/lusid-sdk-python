# VendorDependency

For indicating a dependency on some opaque market data requested by an outside vendor
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**vendor_name** | **str** | The name of the outside vendor | 
**vendor_path** | **List[str]** | The specific dependency path | 
**var_date** | **datetime** | The effectiveDate of the entity that this is a dependency for. | 
**dependency_type** | **str** | The available values are: OpaqueDependency, CashDependency, DiscountingDependency, EquityCurveDependency, EquityVolDependency, FxDependency, FxForwardsDependency, FxVolDependency, IndexProjectionDependency, IrVolDependency, QuoteDependency, Vendor, CalendarDependency, InflationFixingDependency | 
## Example

```python
from lusid.models.vendor_dependency import VendorDependency
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

vendor_name: StrictStr = "example_vendor_name"
vendor_path: List[StrictStr] = # Replace with your value
var_date: datetime = # Replace with your value
dependency_type: StrictStr = "example_dependency_type"
vendor_dependency_instance = VendorDependency(vendor_name=vendor_name, vendor_path=vendor_path, var_date=var_date, dependency_type=dependency_type)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

