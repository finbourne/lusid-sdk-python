# WithholdingTaxRateSplit

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**stop_at_source_rate** | **float** | The rate withheld at source. | 
**irrecoverable_rate** | **float** | The part of the country rate that cannot be recovered. | 
**relief_at_source_rate** | **float** | The part of the country rate relieved at source. | 
**reclaimable_rate** | **float** | The part of the rate withheld at source that can be reclaimed. | 
## Example

```python
from lusid.models.withholding_tax_rate_split import WithholdingTaxRateSplit
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

stop_at_source_rate: Union[StrictFloat, StrictInt] = # Replace with your value
irrecoverable_rate: Union[StrictFloat, StrictInt] = # Replace with your value
relief_at_source_rate: Union[StrictFloat, StrictInt] = # Replace with your value
reclaimable_rate: Union[StrictFloat, StrictInt] = # Replace with your value
withholding_tax_rate_split_instance = WithholdingTaxRateSplit(stop_at_source_rate=stop_at_source_rate, irrecoverable_rate=irrecoverable_rate, relief_at_source_rate=relief_at_source_rate, reclaimable_rate=reclaimable_rate)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

