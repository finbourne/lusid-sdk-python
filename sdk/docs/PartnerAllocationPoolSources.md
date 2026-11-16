# PartnerAllocationPoolSources

The amount reaching a pool by each route: its bucket's lines, lines tagged with its character and lines allocated  directly to one partner.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bucket** | **float** | The amount reaching the pool from the lines its bucket&#39;s rule placed. | 
**line_tag** | **float** | The amount reaching the pool from lines tagged with its character. | 
**direct** | **float** | The amount reaching the pool from lines allocated directly to one partner. | 
## Example

```python
from lusid.models.partner_allocation_pool_sources import PartnerAllocationPoolSources
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

bucket: Union[StrictFloat, StrictInt] = # Replace with your value
line_tag: Union[StrictFloat, StrictInt] = # Replace with your value
direct: Union[StrictFloat, StrictInt] = # Replace with your value
partner_allocation_pool_sources_instance = PartnerAllocationPoolSources(bucket=bucket, line_tag=line_tag, direct=direct)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

