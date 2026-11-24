# FundGroupReportOutput

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**mode** | **str** | Available values: NonConsolidated (each fund&#39;s rows returned as they are, tagged with the fund and valuation point). Consolidated is not yet supported. Defaults to NonConsolidated. Available values: NonConsolidated, Consolidated. | [optional] 
## Example

```python
from lusid.models.fund_group_report_output import FundGroupReportOutput
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

mode: Optional[StrictStr] = "example_mode"
fund_group_report_output_instance = FundGroupReportOutput(mode=mode)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

