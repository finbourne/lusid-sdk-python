# TaxFundReconciliationHoldingResponse

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fund_id** | [**ResourceId**](ResourceId.md) |  | [optional] 
**period** | [**TaxAccountingPeriod**](TaxAccountingPeriod.md) |  | [optional] 
**holding_id** | **str** | The identifier of the holding. For a company this is the pooled LUSID instrument identifier, for a fund the portfolio code and instrument identifier. | [optional] 
**instrument_id** | **str** | The LUSID unique identifier of the instrument. | [optional] 
**instrument_name** | **str** | The name of the instrument. | [optional] 
**company_amount** | **float** | The company-level amount for the holding. | [optional] 
**fund_proxies** | [**List[TaxFundReconciliationProxyRow]**](TaxFundReconciliationProxyRow.md) | The member funds&#39; notional figures for the holding. | [optional] 
**difference** | **float** | The difference between the two sides. | [optional] 
**category** | **str** | The reconciliation category of the difference, when there is one. Available values: ExcludedHoldings, TaxCostAdjustments, OutOfSync, Scope, PoolAveraging, Matching, Indexation, KinkTest. | [optional] 
**explanation** | **str** | The explanation of the difference. | [optional] 
## Example

```python
from lusid.models.tax_fund_reconciliation_holding_response import TaxFundReconciliationHoldingResponse
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

fund_id: Optional[ResourceId] = # Replace with your value
period: Optional[TaxAccountingPeriod] = None
holding_id: Optional[StrictStr] = "example_holding_id"
instrument_id: Optional[StrictStr] = "example_instrument_id"
instrument_name: Optional[StrictStr] = "example_instrument_name"
company_amount: Optional[Union[StrictFloat, StrictInt]] = # Replace with your value
fund_proxies: Optional[List[TaxFundReconciliationProxyRow]] = # Replace with your value
difference: Optional[Union[StrictFloat, StrictInt]] = # Replace with your value
category: Optional[StrictStr] = "example_category"
explanation: Optional[StrictStr] = "example_explanation"
tax_fund_reconciliation_holding_response_instance = TaxFundReconciliationHoldingResponse(fund_id=fund_id, period=period, holding_id=holding_id, instrument_id=instrument_id, instrument_name=instrument_name, company_amount=company_amount, fund_proxies=fund_proxies, difference=difference, category=category, explanation=explanation)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

