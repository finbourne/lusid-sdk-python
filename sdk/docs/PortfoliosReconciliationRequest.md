# PortfoliosReconciliationRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**left** | [**PortfolioReconciliationRequest**](PortfolioReconciliationRequest.md) |  | 
**right** | [**PortfolioReconciliationRequest**](PortfolioReconciliationRequest.md) |  | 
**instrument_property_keys** | **List[str]** | Instrument properties to be included with any identified breaks. These properties will be in the effective and AsAt dates of the left portfolio | 
## Example

```python
from lusid.models.portfolios_reconciliation_request import PortfoliosReconciliationRequest
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

left: PortfolioReconciliationRequest
right: PortfolioReconciliationRequest
instrument_property_keys: List[StrictStr] = # Replace with your value
portfolios_reconciliation_request_instance = PortfoliosReconciliationRequest(left=left, right=right, instrument_property_keys=instrument_property_keys)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

