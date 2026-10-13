# FundTerms

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**versions** | [**List[FundTermsVersion]**](FundTermsVersion.md) |  | 
## Example

```python
from lusid.models.fund_terms import FundTerms
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

versions: List[FundTermsVersion]
fund_terms_instance = FundTerms(versions=versions)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

