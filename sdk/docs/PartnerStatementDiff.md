# PartnerStatementDiff

The differences between two of a partner's statements.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**statement_id** | **str** | The identifier of the statement. | 
**against_statement_id** | **str** | The identifier of the statement to compare against. | 
**identical** | **bool** | Whether the two statements carry the same figures. | 
**differences** | [**List[PartnerStatementLineDifference]**](PartnerStatementLineDifference.md) | The figures that differ between the two statements. | 
## Example

```python
from lusid.models.partner_statement_diff import PartnerStatementDiff
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

statement_id: StrictStr = "example_statement_id"
against_statement_id: StrictStr = "example_against_statement_id"
identical: StrictBool = # Replace with your value
identical:StrictBool = True
differences: List[PartnerStatementLineDifference] = # Replace with your value
partner_statement_diff_instance = PartnerStatementDiff(statement_id=statement_id, against_statement_id=against_statement_id, identical=identical, differences=differences)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

