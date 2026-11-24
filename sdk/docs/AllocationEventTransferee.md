# AllocationEventTransferee

A transferee a Transfer's booking gives a line: the line, and the investment account it is opened under.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**investor_record_id** | **str** | The transferee&#39;s investor record, as the leg names it. | [optional] 
**fund_id** | [**ResourceId**](ResourceId.md) |  | [optional] 
**line_id** | **str** | The commitment line opened for the transferee. | [optional] 
**line** | **str** | What happens to the line: Open when a booking would open it, Opened when this booking opened it. | [optional] 
**investment_account_scope** | **str** | The scope of the investment account the line is opened under: the fund&#39;s. | [optional] 
**investment_account_identifier_type** | **str** | The type of the investment account&#39;s identifier, as a property key. An account a transfer opens is identified by InvestmentAccount/system/TransfereeAccountId. | [optional] 
**investment_account_identifier_value** | **str** | The value of the investment account&#39;s identifier. An account a transfer opens has the value &#39;{fundCode}-{investor record LUID}&#39;, so a retry or a concurrent transfer finds the same account. | [optional] 
**investment_account** | **str** | What happens to the investment account: Existing when the transferee already holds it, Create when a booking would open it, Created when this booking opened it. | [optional] 
## Example

```python
from lusid.models.allocation_event_transferee import AllocationEventTransferee
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

investor_record_id: Optional[StrictStr] = "example_investor_record_id"
fund_id: Optional[ResourceId] = # Replace with your value
line_id: Optional[StrictStr] = "example_line_id"
line: Optional[StrictStr] = "example_line"
investment_account_scope: Optional[StrictStr] = "example_investment_account_scope"
investment_account_identifier_type: Optional[StrictStr] = "example_investment_account_identifier_type"
investment_account_identifier_value: Optional[StrictStr] = "example_investment_account_identifier_value"
investment_account: Optional[StrictStr] = "example_investment_account"
allocation_event_transferee_instance = AllocationEventTransferee(investor_record_id=investor_record_id, fund_id=fund_id, line_id=line_id, line=line, investment_account_scope=investment_account_scope, investment_account_identifier_type=investment_account_identifier_type, investment_account_identifier_value=investment_account_identifier_value, investment_account=investment_account)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

