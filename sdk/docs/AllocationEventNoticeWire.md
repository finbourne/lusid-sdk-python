# AllocationEventNoticeWire

Wire instructions for the payment a notice asks for or announces, from the investor record's payment  instructions. Absent when the investor record holds none.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bank_name** | **str** | The name of the bank. | [optional] 
**account_name** | **str** | The name on the account. | [optional] 
**account_number** | **str** | The account number or IBAN. | [optional] 
**bic** | **str** | The bank identifier code. | [optional] 
**reference** | **str** | The payment reference. | [optional] 
## Example

```python
from lusid.models.allocation_event_notice_wire import AllocationEventNoticeWire
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

bank_name: Optional[StrictStr] = "example_bank_name"
account_name: Optional[StrictStr] = "example_account_name"
account_number: Optional[StrictStr] = "example_account_number"
bic: Optional[StrictStr] = "example_bic"
reference: Optional[StrictStr] = "example_reference"
allocation_event_notice_wire_instance = AllocationEventNoticeWire(bank_name=bank_name, account_name=account_name, account_number=account_number, bic=bic, reference=reference)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

