# TaxReturnResponse

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fund_id** | [**ResourceId**](ResourceId.md) |  | [optional] 
**period** | [**TaxAccountingPeriod**](TaxAccountingPeriod.md) |  | [optional] 
**status** | **str** | The workflow status of the return. Available values: Draft, Prepared, Reviewed, SignedOff, Final. Available values: Draft, Prepared, Reviewed, SignedOff, Final. | [optional] 
**steps** | [**List[TaxReturnWorkflowStep]**](TaxReturnWorkflowStep.md) | The workflow history of the return in the order the steps were taken. | [optional] 
**line_a** | [**List[TaxReturnDisposalRow]**](TaxReturnDisposalRow.md) | Chargeable gains and allowable losses on actual disposals in the period. | [optional] 
**line_a_total** | **float** | The total of line A, in whole pounds. | [optional] 
**vintages** | [**List[TaxReturnVintage]**](TaxReturnVintage.md) | The deemed-disposal vintages, one per period, that feed line D. | [optional] 
**instalments** | [**List[TaxReturnSpreadInstalment]**](TaxReturnSpreadInstalment.md) | The instalments of earlier vintages that fall into the period. | [optional] 
**line_d_total** | **float** | The total of line D, in whole pounds. | [optional] 
**loan_relationships** | [**List[TaxReturnLoanRelationshipRow]**](TaxReturnLoanRelationshipRow.md) | The loan relationship and derivative holdings that make up line LR. Empty for a fund. | [optional] 
**line_lr_total** | **float** | The total of line LR, in whole pounds. Zero for a fund. | [optional] 
**outside** | [**List[TaxReturnExcludedRow]**](TaxReturnExcludedRow.md) | The holdings excluded from the return, with the reason. | [optional] 
**summary** | [**List[TaxReturnMemoRow]**](TaxReturnMemoRow.md) | Memo rows such as the tax at the applicable rate and the minimum-profits trade profit. | [optional] 
**sync_break_open** | **bool** | True when the tax records are out of sync with the ledger and the return cannot advance past Reviewed. | [optional] 
## Example

```python
from lusid.models.tax_return_response import TaxReturnResponse
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

fund_id: Optional[ResourceId] = # Replace with your value
period: Optional[TaxAccountingPeriod] = None
status: Optional[StrictStr] = "example_status"
steps: Optional[List[TaxReturnWorkflowStep]] = # Replace with your value
line_a: Optional[List[TaxReturnDisposalRow]] = # Replace with your value
line_a_total: Optional[Union[StrictFloat, StrictInt]] = # Replace with your value
vintages: Optional[List[TaxReturnVintage]] = # Replace with your value
instalments: Optional[List[TaxReturnSpreadInstalment]] = # Replace with your value
line_d_total: Optional[Union[StrictFloat, StrictInt]] = # Replace with your value
loan_relationships: Optional[List[TaxReturnLoanRelationshipRow]] = # Replace with your value
line_lr_total: Optional[Union[StrictFloat, StrictInt]] = # Replace with your value
outside: Optional[List[TaxReturnExcludedRow]] = # Replace with your value
summary: Optional[List[TaxReturnMemoRow]] = # Replace with your value
sync_break_open: Optional[StrictBool] = # Replace with your value
sync_break_open:Optional[StrictBool] = None
tax_return_response_instance = TaxReturnResponse(fund_id=fund_id, period=period, status=status, steps=steps, line_a=line_a, line_a_total=line_a_total, vintages=vintages, instalments=instalments, line_d_total=line_d_total, loan_relationships=loan_relationships, line_lr_total=line_lr_total, outside=outside, summary=summary, sync_break_open=sync_break_open)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

