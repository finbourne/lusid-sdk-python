# DealingFlowSummary

The transfer agency estimates a swing decision was made on: the orders dealt at the valuation point, what they summed, and how many pending orders were left out and what those were worth.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** | How many orders were summed. | 
**gross_inflow** | **float** | The sum of the inflows, in the fund currency. Zero or more. | 
**gross_outflow** | **float** | The sum of the outflows, in the fund currency, as a magnitude. Zero or more. | 
**pending_not_counted** | **int** | How many pending orders at the valuation point were left out of the sums because the fund&#39;s dealing estimates do not count pending orders. Zero when the fund counts them. | 
**pending_gross_inflow** | **float** | The sum of the inflows among the pending orders left out, in the fund currency, with units at the estimate price. Zero or more; zero when the fund counts pending orders. | 
**pending_gross_outflow** | **float** | The sum of the outflows among the pending orders left out, in the fund currency, as a magnitude, with units at the estimate price. Zero or more; zero when the fund counts pending orders. | 
**pending_unvalued_count** | **int** | How many of the pending orders left out could not be valued, such as a unit order with no price yet. They are in pendingNotCounted but absent from pendingGrossInflow and pendingGrossOutflow. | 
## Example

```python
from lusid.models.dealing_flow_summary import DealingFlowSummary
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

count: StrictInt = # Replace with your value
count: StrictInt = 42
gross_inflow: Union[StrictFloat, StrictInt] = # Replace with your value
gross_outflow: Union[StrictFloat, StrictInt] = # Replace with your value
pending_not_counted: StrictInt = # Replace with your value
pending_not_counted: StrictInt = 42
pending_gross_inflow: Union[StrictFloat, StrictInt] = # Replace with your value
pending_gross_outflow: Union[StrictFloat, StrictInt] = # Replace with your value
pending_unvalued_count: StrictInt = # Replace with your value
pending_unvalued_count: StrictInt = 42
dealing_flow_summary_instance = DealingFlowSummary(count=count, gross_inflow=gross_inflow, gross_outflow=gross_outflow, pending_not_counted=pending_not_counted, pending_gross_inflow=pending_gross_inflow, pending_gross_outflow=pending_gross_outflow, pending_unvalued_count=pending_unvalued_count)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

