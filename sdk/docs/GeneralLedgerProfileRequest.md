# GeneralLedgerProfileRequest

A General Ledger Profile Definition.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**general_ledger_profile_code** | **str** | The unique code for the General Ledger Profile | 
**display_name** | **str** | The name of the General Ledger Profile | 
**description** | **str** | A description for the General Ledger Profile | [optional] 
**general_ledger_profile_mappings** | [**List[GeneralLedgerProfileMapping]**](GeneralLedgerProfileMapping.md) | Rules for mapping Account or property values to aggregation pattern definitions | 
## Example

```python
from lusid.models.general_ledger_profile_request import GeneralLedgerProfileRequest
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

general_ledger_profile_code: StrictStr = "example_general_ledger_profile_code"
display_name: StrictStr = "example_display_name"
description: Optional[StrictStr] = "example_description"
general_ledger_profile_mappings: List[GeneralLedgerProfileMapping] = # Replace with your value
general_ledger_profile_request_instance = GeneralLedgerProfileRequest(general_ledger_profile_code=general_ledger_profile_code, display_name=display_name, description=description, general_ledger_profile_mappings=general_ledger_profile_mappings)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

