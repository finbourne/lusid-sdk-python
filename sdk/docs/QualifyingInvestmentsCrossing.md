# QualifyingInvestmentsCrossing

A flip of the qualifying-investments result between two consecutive observed days.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_from** | **datetime** | The date of the observation before the flip. | 
**to** | **datetime** | The date of the observation after the flip. | 
**was_bond_fund_before** | **bool** | Whether the scheme was a bond fund on the From date. | 
**is_bond_fund_after** | **bool** | Whether the scheme was a bond fund on the To date. | 
## Example

```python
from lusid.models.qualifying_investments_crossing import QualifyingInvestmentsCrossing
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

var_from: datetime = # Replace with your value
to: datetime = # Replace with your value
was_bond_fund_before: StrictBool = # Replace with your value
was_bond_fund_before:StrictBool = True
is_bond_fund_after: StrictBool = # Replace with your value
is_bond_fund_after:StrictBool = True
qualifying_investments_crossing_instance = QualifyingInvestmentsCrossing(var_from=var_from, to=to, was_bond_fund_before=was_bond_fund_before, is_bond_fund_after=is_bond_fund_after)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

