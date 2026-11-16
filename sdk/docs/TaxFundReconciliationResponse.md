# TaxFundReconciliationResponse

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fund_id** | [**ResourceId**](ResourceId.md) |  | [optional] 
**period** | [**TaxAccountingPeriod**](TaxAccountingPeriod.md) |  | [optional] 
**company_total** | **float** | The company-level total of lines A, D and LR. | [optional] 
**sum_of_fund_proxies** | **float** | The sum of the member funds&#39; notional totals. | [optional] 
**differences** | [**List[TaxReconciliationDifferenceRow]**](TaxReconciliationDifferenceRow.md) | The explained differences between the two sides, by holding. | [optional] 
**unexplained** | **float** | The part of the difference not explained by any category. Nil when the reconciliation is complete. | [optional] 
**company_line_d** | **float** | Line D at company level. | [optional] 
**funds_line_d** | **float** | The sum of line D across the member funds. | [optional] 
**company_line_lr** | **float** | Line LR at company level. | [optional] 
**funds_line_lr** | **float** | The sum of line LR across the member funds. | [optional] 
## Example

```python
from lusid.models.tax_fund_reconciliation_response import TaxFundReconciliationResponse
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

fund_id: Optional[ResourceId] = # Replace with your value
period: Optional[TaxAccountingPeriod] = None
company_total: Optional[Union[StrictFloat, StrictInt]] = # Replace with your value
sum_of_fund_proxies: Optional[Union[StrictFloat, StrictInt]] = # Replace with your value
differences: Optional[List[TaxReconciliationDifferenceRow]] = # Replace with your value
unexplained: Optional[Union[StrictFloat, StrictInt]] = # Replace with your value
company_line_d: Optional[Union[StrictFloat, StrictInt]] = # Replace with your value
funds_line_d: Optional[Union[StrictFloat, StrictInt]] = # Replace with your value
company_line_lr: Optional[Union[StrictFloat, StrictInt]] = # Replace with your value
funds_line_lr: Optional[Union[StrictFloat, StrictInt]] = # Replace with your value
tax_fund_reconciliation_response_instance = TaxFundReconciliationResponse(fund_id=fund_id, period=period, company_total=company_total, sum_of_fund_proxies=sum_of_fund_proxies, differences=differences, unexplained=unexplained, company_line_d=company_line_d, funds_line_d=funds_line_d, company_line_lr=company_line_lr, funds_line_lr=funds_line_lr)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

