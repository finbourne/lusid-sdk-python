# TaxDeemedDisposalsResponse

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fund_id** | [**ResourceId**](ResourceId.md) |  | [optional] 
**period** | [**TaxAccountingPeriod**](TaxAccountingPeriod.md) |  | [optional] 
**disposals** | [**List[TaxDeemedDisposalResponse]**](TaxDeemedDisposalResponse.md) | The deemed disposals at the end of the period. | [optional] 
**vintages** | [**List[TaxReturnVintage]**](TaxReturnVintage.md) | The deemed-disposal vintages, one per period, that feed line D. | [optional] 
**matrix** | [**List[TaxReturnSpreadInstalment]**](TaxReturnSpreadInstalment.md) | The seven-period spreading matrix for the vintages. | [optional] 
## Example

```python
from lusid.models.tax_deemed_disposals_response import TaxDeemedDisposalsResponse
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

fund_id: Optional[ResourceId] = # Replace with your value
period: Optional[TaxAccountingPeriod] = None
disposals: Optional[List[TaxDeemedDisposalResponse]] = # Replace with your value
vintages: Optional[List[TaxReturnVintage]] = # Replace with your value
matrix: Optional[List[TaxReturnSpreadInstalment]] = # Replace with your value
tax_deemed_disposals_response_instance = TaxDeemedDisposalsResponse(fund_id=fund_id, period=period, disposals=disposals, vintages=vintages, matrix=matrix)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

