# CustodianAccountRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**scope** | **str** | The Scope assigned to the Custodian Account, where left blank the parent Portfolio Scope will be used | [optional] 
**code** | **str** | Unique Code representing the Custodian Account | 
**status** | **str** | The Account status. Can be Active, Inactive or Deleted. | [optional] 
**account_number** | **str** | The Custodian Account Number | 
**account_name** | **str** | The identifiable name given to the Custodian Account | 
**accounting_method** | **str** | The Accounting method to be used | 
**currency** | **str** | The Currency for the Account | 
**properties** | [**Dict[str, ModelProperty]**](ModelProperty.md) | Set of unique Custodian Account properties and associated values to store with the Custodian Account. Each property must be from the &#39;CustodianAccount&#39; domain. | [optional] 
**custodian_identifier** | [**TypedResourceId**](TypedResourceId.md) |  | 
**account_type** | **str** | The Type of the Custodian Account. Can be Margin, Cash or Swap. Defaults to Margin. | [optional] 
## Example

```python
from lusid.models.custodian_account_request import CustodianAccountRequest
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

scope: Optional[StrictStr] = "example_scope"
code: StrictStr = "example_code"
status: Optional[StrictStr] = "example_status"
account_number: StrictStr = "example_account_number"
account_name: StrictStr = "example_account_name"
accounting_method: StrictStr = "example_accounting_method"
currency: StrictStr = "example_currency"
properties: Optional[Dict[str, ModelProperty]] = # Replace with your value
custodian_identifier: TypedResourceId = # Replace with your value
account_type: Optional[StrictStr] = "example_account_type"
custodian_account_request_instance = CustodianAccountRequest(scope=scope, code=code, status=status, account_number=account_number, account_name=account_name, accounting_method=accounting_method, currency=currency, properties=properties, custodian_identifier=custodian_identifier, account_type=account_type)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

