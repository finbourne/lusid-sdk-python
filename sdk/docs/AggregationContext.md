# AggregationContext

Aggregation context node. Whilst the market and pricing nodes concern themselves with which models are used and where the market data comes from, the aggregation  context determines how data is aggregated together. This controls the behaviour of the grouping and sql-like engine at the back of the valuation. For instance,  it controls conversion of currencies and whether the sql-like engine behaves more like ANSI or MySql SQL.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**options** | [**AggregationOptions**](AggregationOptions.md) |  | [optional] 
## Example

```python
from lusid.models.aggregation_context import AggregationContext
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

options: Optional[AggregationOptions] = None
aggregation_context_instance = AggregationContext(options=options)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

