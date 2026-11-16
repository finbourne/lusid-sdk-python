# TaxLedgerReconciliationHoldingResponse

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fund_id** | [**ResourceId**](ResourceId.md) |  | [optional] 
**period** | [**TaxAccountingPeriod**](TaxAccountingPeriod.md) |  | [optional] 
**holding_id** | **str** | The identifier of the holding. For a company this is the pooled LUSID instrument identifier, for a fund the portfolio code and instrument identifier. | [optional] 
**instrument_id** | **str** | The LUSID unique identifier of the instrument. | [optional] 
**instrument_name** | **str** | The name of the instrument. | [optional] 
**portfolio_code** | **str** | The code of the portfolio the holding sits in, or the pooled marker for a company. | [optional] 
**ledger_realised** | **float** | The realised gain or loss recorded in the ledger for the holding. | [optional] 
**ledger_unrealised_movement** | **float** | The movement in unrealised gain or loss recorded in the ledger for the holding. | [optional] 
**tax_realised_unindexed** | **float** | The realised gain or loss for tax before indexation. | [optional] 
**tax_unrealised_movement_unindexed** | **float** | The movement in the unrealised gain or loss for tax before indexation. | [optional] 
**deemed_disposal_net** | **float** | The net deemed-disposal amount for the holding. | [optional] 
**loan_relationship_net** | **float** | The net loan relationship credit or debit for the holding. | [optional] 
**category** | **str** | The reconciliation category of the difference, when there is one. Available values: ExcludedHoldings, TaxCostAdjustments, OutOfSync, Scope, PoolAveraging, Matching, Indexation, KinkTest. | [optional] 
**difference** | **float** | The difference between the two sides. | [optional] 
**explanation** | **str** | The explanation of the difference. | [optional] 
## Example

```python
from lusid.models.tax_ledger_reconciliation_holding_response import TaxLedgerReconciliationHoldingResponse
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

fund_id: Optional[ResourceId] = # Replace with your value
period: Optional[TaxAccountingPeriod] = None
holding_id: Optional[StrictStr] = "example_holding_id"
instrument_id: Optional[StrictStr] = "example_instrument_id"
instrument_name: Optional[StrictStr] = "example_instrument_name"
portfolio_code: Optional[StrictStr] = "example_portfolio_code"
ledger_realised: Optional[Union[StrictFloat, StrictInt]] = # Replace with your value
ledger_unrealised_movement: Optional[Union[StrictFloat, StrictInt]] = # Replace with your value
tax_realised_unindexed: Optional[Union[StrictFloat, StrictInt]] = # Replace with your value
tax_unrealised_movement_unindexed: Optional[Union[StrictFloat, StrictInt]] = # Replace with your value
deemed_disposal_net: Optional[Union[StrictFloat, StrictInt]] = # Replace with your value
loan_relationship_net: Optional[Union[StrictFloat, StrictInt]] = # Replace with your value
category: Optional[StrictStr] = "example_category"
difference: Optional[Union[StrictFloat, StrictInt]] = # Replace with your value
explanation: Optional[StrictStr] = "example_explanation"
tax_ledger_reconciliation_holding_response_instance = TaxLedgerReconciliationHoldingResponse(fund_id=fund_id, period=period, holding_id=holding_id, instrument_id=instrument_id, instrument_name=instrument_name, portfolio_code=portfolio_code, ledger_realised=ledger_realised, ledger_unrealised_movement=ledger_unrealised_movement, tax_realised_unindexed=tax_realised_unindexed, tax_unrealised_movement_unindexed=tax_unrealised_movement_unindexed, deemed_disposal_net=deemed_disposal_net, loan_relationship_net=loan_relationship_net, category=category, difference=difference, explanation=explanation)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

