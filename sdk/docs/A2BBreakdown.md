# A2BBreakdown

A2B Breakdown - Shows the total, and each sub-element within an A2B Category
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total** | **float** | The total value of all the components within this category. | [optional] 
**currency** | **str** | The currency. Applies to the Total, as well as all the componenents. | [optional] 
**components** | **Dict[str, float]** | The individual components that make up the category. For example, the Start category may have Cost, Unrealised gains and accrued interest components. | [optional] 
## Example

```python
from lusid.models.a2_b_breakdown import A2BBreakdown
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

total: Optional[Union[StrictFloat, StrictInt]] = # Replace with your value
currency: Optional[StrictStr] = "example_currency"
components: Optional[Dict[str, Union[StrictFloat, StrictInt]]] = # Replace with your value
a2_b_breakdown_instance = A2BBreakdown(total=total, currency=currency, components=components)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

