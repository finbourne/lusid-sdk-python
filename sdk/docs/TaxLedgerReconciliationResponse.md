# TaxLedgerReconciliationResponse

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fund_id** | [**ResourceId**](ResourceId.md) |  | [optional] 
**period** | [**TaxAccountingPeriod**](TaxAccountingPeriod.md) |  | [optional] 
**ledger_capital_gain_loss** | **float** | The realised and unrealised capital gain or loss recorded in the ledger for the period. | [optional] 
**comparable_tax_figure** | **float** | The tax figure on the same basis as the ledger, before the return adjustments. | [optional] 
**differences** | [**List[TaxReconciliationDifferenceRow]**](TaxReconciliationDifferenceRow.md) | The explained differences between the two sides, by holding. | [optional] 
**unexplained** | **float** | The part of the difference not explained by any category. Nil when the reconciliation is complete. | [optional] 
**bridge** | [**List[TaxReconciliationBridgeRow]**](TaxReconciliationBridgeRow.md) | The bridge from the ledger figure to the return total. | [optional] 
**return_total** | **float** | The total of lines A, D and LR. | [optional] 
**bridge_unexplained** | **float** | The part of the bridge not explained. Nil when the bridge is complete. | [optional] 
## Example

```python
from lusid.models.tax_ledger_reconciliation_response import TaxLedgerReconciliationResponse
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

fund_id: Optional[ResourceId] = # Replace with your value
period: Optional[TaxAccountingPeriod] = None
ledger_capital_gain_loss: Optional[Union[StrictFloat, StrictInt]] = # Replace with your value
comparable_tax_figure: Optional[Union[StrictFloat, StrictInt]] = # Replace with your value
differences: Optional[List[TaxReconciliationDifferenceRow]] = # Replace with your value
unexplained: Optional[Union[StrictFloat, StrictInt]] = # Replace with your value
bridge: Optional[List[TaxReconciliationBridgeRow]] = # Replace with your value
return_total: Optional[Union[StrictFloat, StrictInt]] = # Replace with your value
bridge_unexplained: Optional[Union[StrictFloat, StrictInt]] = # Replace with your value
tax_ledger_reconciliation_response_instance = TaxLedgerReconciliationResponse(fund_id=fund_id, period=period, ledger_capital_gain_loss=ledger_capital_gain_loss, comparable_tax_figure=comparable_tax_figure, differences=differences, unexplained=unexplained, bridge=bridge, return_total=return_total, bridge_unexplained=bridge_unexplained)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

