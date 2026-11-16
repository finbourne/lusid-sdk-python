# TaxReconciliationDifferenceRow

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**holding_id** | **str** | The identifier of the holding. For a company this is the pooled LUSID instrument identifier, for a fund the portfolio code and instrument identifier. | [optional] 
**instrument_id** | **str** | The LUSID unique identifier of the instrument. | [optional] 
**instrument_name** | **str** | The name of the instrument. | [optional] 
**category** | **str** | The reconciliation category. Available values: ExcludedHoldings, TaxCostAdjustments, OutOfSync, Scope, PoolAveraging, Matching, Indexation, KinkTest. Available values: ExcludedHoldings, TaxCostAdjustments, OutOfSync, Scope, PoolAveraging, Matching, Indexation, KinkTest. | [optional] 
**compared_amount** | **float** | The amount on the side being reconciled from. | [optional] 
**tax_amount** | **float** | The amount on the tax side. | [optional] 
**difference** | **float** | The difference between the two sides. | [optional] 
**explanation** | **str** | The explanation of the difference. | [optional] 
## Example

```python
from lusid.models.tax_reconciliation_difference_row import TaxReconciliationDifferenceRow
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

holding_id: Optional[StrictStr] = "example_holding_id"
instrument_id: Optional[StrictStr] = "example_instrument_id"
instrument_name: Optional[StrictStr] = "example_instrument_name"
category: Optional[StrictStr] = "example_category"
compared_amount: Optional[Union[StrictFloat, StrictInt]] = # Replace with your value
tax_amount: Optional[Union[StrictFloat, StrictInt]] = # Replace with your value
difference: Optional[Union[StrictFloat, StrictInt]] = # Replace with your value
explanation: Optional[StrictStr] = "example_explanation"
tax_reconciliation_difference_row_instance = TaxReconciliationDifferenceRow(holding_id=holding_id, instrument_id=instrument_id, instrument_name=instrument_name, category=category, compared_amount=compared_amount, tax_amount=tax_amount, difference=difference, explanation=explanation)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

