# FundTermsVersion

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**terms_version_id** | **str** |  | 
**effective_from** | **datetime** |  | 
**fees** | [**List[FeeDefinition]**](FeeDefinition.md) |  | [optional] 
**carry** | [**CarryParameters**](CarryParameters.md) |  | [optional] 
**recycling** | [**RecyclingTerms**](RecyclingTerms.md) |  | [optional] 
**equalisation** | [**EqualisationTerms**](EqualisationTerms.md) |  | [optional] 
**applies_from_closing_id** | **str** |  | [optional] 
## Example

```python
from lusid.models.fund_terms_version import FundTermsVersion
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

terms_version_id: StrictStr = "example_terms_version_id"
effective_from: datetime = # Replace with your value
fees: Optional[List[FeeDefinition]] = None
carry: Optional[CarryParameters] = None
recycling: Optional[RecyclingTerms] = None
equalisation: Optional[EqualisationTerms] = None
applies_from_closing_id: Optional[StrictStr] = "example_applies_from_closing_id"
fund_terms_version_instance = FundTermsVersion(terms_version_id=terms_version_id, effective_from=effective_from, fees=fees, carry=carry, recycling=recycling, equalisation=equalisation, applies_from_closing_id=applies_from_closing_id)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

