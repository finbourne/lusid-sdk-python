# QueryRelationalDatasetRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**query_method** | **str** | The method used to query data points. Can be either &#39;Latest&#39; or &#39;TimeSeries&#39;. | [optional] 
**filter** | **str** | Expression to filter the result set. For more information about filtering LUSID results, see https://support.lusid.com/knowledgebase/article/KA-01914. | [optional] 
**custom_sort_by** | **List[str]** | A list of fields to sort the results by. For example, to sort by a Value field &#39;AValueField&#39; in descending order, specify &#39;AValueField DESC&#39;. | [optional] 
## Example

```python
from lusid.models.query_relational_dataset_request import QueryRelationalDatasetRequest
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

query_method: Optional[StrictStr] = "example_query_method"
filter: Optional[StrictStr] = "example_filter"
custom_sort_by: Optional[List[StrictStr]] = # Replace with your value
query_relational_dataset_request_instance = QueryRelationalDatasetRequest(query_method=query_method, filter=filter, custom_sort_by=custom_sort_by)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

