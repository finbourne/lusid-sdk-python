# PresentationConfiguration

How partner capital is presented on statements and the valuation point.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**contributions_receivable_netted** | **bool** |  | [optional] 
**separate_notice_due_receipt_dates** | **bool** |  | [optional] 
## Example

```python
from lusid.models.presentation_configuration import PresentationConfiguration
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

contributions_receivable_netted: Optional[StrictBool] = # Replace with your value
contributions_receivable_netted:Optional[StrictBool] = None
separate_notice_due_receipt_dates: Optional[StrictBool] = # Replace with your value
separate_notice_due_receipt_dates:Optional[StrictBool] = None
presentation_configuration_instance = PresentationConfiguration(contributions_receivable_netted=contributions_receivable_netted, separate_notice_due_receipt_dates=separate_notice_due_receipt_dates)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

