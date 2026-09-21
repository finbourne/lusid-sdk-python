# QueryableKeysForMetricsResponse

The queryable key definition of each requested metric. Every requested metric appears in exactly one of  the two maps.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**metrics** | [**Dict[str, QueryableKey]**](QueryableKey.md) | The definition of each metric that resolved, describing what a valuation returns for it and how to  present it. Keyed by the metric as it was requested, for example &#39;Valuation/PV&#39; or  &#39;ProfitAndLoss/Realised/Market(Window&#x3D;YTD)&#39;. Identical requested keys appear once; different  spellings of the same underlying key, such as a property&#39;s raw and wrapper forms, each appear. | 
**failed** | **Dict[str, Optional[str]]** | Why each metric that did not resolve cannot be requested, keyed as for Metrics. Empty when every  metric resolved. | 
## Example

```python
from lusid.models.queryable_keys_for_metrics_response import QueryableKeysForMetricsResponse
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

metrics: Dict[str, QueryableKey] = # Replace with your value
failed: Dict[str, Optional[StrictStr]] = # Replace with your value
queryable_keys_for_metrics_response_instance = QueryableKeysForMetricsResponse(metrics=metrics, failed=failed)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

