# UpsertReferencePortfolioConstituentPropertiesRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**identifiers** | **Dict[str, Optional[str]]** | A set of instrument identifiers that can resolve the constituent to a unique instrument. | 
**properties** | [**Dict[str, PerpetualProperty]**](PerpetualProperty.md) | The updated collection of properties of the constituent. | 
## Example

```python
from lusid.models.upsert_reference_portfolio_constituent_properties_request import UpsertReferencePortfolioConstituentPropertiesRequest
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

identifiers: Dict[str, Optional[StrictStr]] = # Replace with your value
properties: Dict[str, PerpetualProperty] = # Replace with your value
upsert_reference_portfolio_constituent_properties_request_instance = UpsertReferencePortfolioConstituentPropertiesRequest(identifiers=identifiers, properties=properties)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

