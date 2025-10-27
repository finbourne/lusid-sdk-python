# ReferencePortfolioConstituent

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**instrument_identifiers** | **Dict[str, Optional[str]]** | Unique instrument identifiers | [optional] 
**instrument_uid** | **str** | LUSID&#39;s internal unique instrument identifier, resolved from the instrument identifiers | 
**currency** | **str** |  | 
**properties** | [**Dict[str, PerpetualProperty]**](PerpetualProperty.md) | Properties associated with the constituent | [optional] 
**weight** | **float** |  | 
**floating_weight** | **float** |  | [optional] 
**instrument_scope** | **str** |  | [optional] 
## Example

```python
from lusid.models.reference_portfolio_constituent import ReferencePortfolioConstituent
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

instrument_identifiers: Optional[Dict[str, Optional[StrictStr]]] = # Replace with your value
instrument_uid: StrictStr = "example_instrument_uid"
currency: StrictStr = "example_currency"
properties: Optional[Dict[str, PerpetualProperty]] = # Replace with your value
weight: Union[StrictFloat, StrictInt]
floating_weight: Optional[Union[StrictFloat, StrictInt]] = # Replace with your value
instrument_scope: Optional[StrictStr] = "example_instrument_scope"
reference_portfolio_constituent_instance = ReferencePortfolioConstituent(instrument_identifiers=instrument_identifiers, instrument_uid=instrument_uid, currency=currency, properties=properties, weight=weight, floating_weight=floating_weight, instrument_scope=instrument_scope)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

