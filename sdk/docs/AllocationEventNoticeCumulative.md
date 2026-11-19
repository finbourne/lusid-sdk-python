# AllocationEventNoticeCumulative

Cumulative balances to date for a partner on a notice.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**contributions** | **float** | Cumulative contributions after the event. | 
**distributions** | **float** | Cumulative distributions after the event, tax withheld on the partner&#39;s behalf included, as the capital account&#39;s distributions row counts them. | 
**recallable** | **float** | Cumulative recallable distributions after the event. | 
**tax_withheld** | **float** | Tax withheld from the partner&#39;s distributions to date and paid to the tax authority on its behalf: counted in the cumulative distributions, so the cash the partner actually received is distributions less this. | 
## Example

```python
from lusid.models.allocation_event_notice_cumulative import AllocationEventNoticeCumulative
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

contributions: Union[StrictFloat, StrictInt] = # Replace with your value
distributions: Union[StrictFloat, StrictInt] = # Replace with your value
recallable: Union[StrictFloat, StrictInt] = # Replace with your value
tax_withheld: Union[StrictFloat, StrictInt] = # Replace with your value
allocation_event_notice_cumulative_instance = AllocationEventNoticeCumulative(contributions=contributions, distributions=distributions, recallable=recallable, tax_withheld=tax_withheld)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

