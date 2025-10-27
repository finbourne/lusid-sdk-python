# InvestorIdentifier

Identification of an Investor on the LUSID API.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**investor_type** | **str** | The type of the investor of the Investor Record. Can be either a Person or a LegalEntity | 
**identifiers** | **Dict[str, Optional[str]]** | Single identifier that should target the desired person or legal entity | [optional] 
## Example

```python
from lusid.models.investor_identifier import InvestorIdentifier
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

investor_type: StrictStr = "example_investor_type"
identifiers: Optional[Dict[str, Optional[StrictStr]]] = # Replace with your value
investor_identifier_instance = InvestorIdentifier(investor_type=investor_type, identifiers=identifiers)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

