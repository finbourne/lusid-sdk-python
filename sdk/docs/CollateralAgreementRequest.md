# CollateralAgreementRequest

The request used to create a Collateral Agreement.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** | The code of the Collateral Agreement. | 
**counterparty_id** | [**CounterpartyIdentifier**](CounterpartyIdentifier.md) |  | 
**applicability_filter** | **str** | A filter selecting the portfolios and trades the agreement covers. Checked for structure only when the agreement is stored. | 
**base_currency** | **str** | The currency margin is calculated and called in. Filterable. | 
**cut_label** | **str** | The cut label naming the market data that margin is valued at. | 
**recipe_id** | [**ResourceId**](ResourceId.md) |  | 
**minimum_transfer_amount** | **float** | The smallest margin movement that is called. Optional. | [optional] 
**rounding** | [**MarginRounding**](MarginRounding.md) |  | 
**settlement_lag** | [**MarginSettlementLag**](MarginSettlementLag.md) |  | 
**match_tolerance** | **float** | The tolerance within which our margin figure and the counterparty&#39;s are considered to match. Optional. | [optional] 
**variation_margin** | [**List[MarginItem]**](MarginItem.md) | The variation margin arrangements under the agreement. | [optional] 
**initial_margin** | [**List[MarginItem]**](MarginItem.md) | The initial margin arrangements under the agreement. | [optional] 
**properties** | [**Dict[str, ModelProperty]**](ModelProperty.md) | A set of properties to decorate onto the Collateral Agreement. Filterable. | [optional] 
**effective_at** | **datetime** | The effective datetime from which the Collateral Agreement applies. Defaults to the beginning of time if not specified, so that the agreement is visible at every effective datetime. | [optional] 
## Example

```python
from lusid.models.collateral_agreement_request import CollateralAgreementRequest
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

code: StrictStr = "example_code"
counterparty_id: CounterpartyIdentifier = # Replace with your value
applicability_filter: StrictStr = "example_applicability_filter"
base_currency: StrictStr = "example_base_currency"
cut_label: StrictStr = "example_cut_label"
recipe_id: ResourceId = # Replace with your value
minimum_transfer_amount: Optional[Union[StrictFloat, StrictInt]] = # Replace with your value
rounding: MarginRounding
settlement_lag: MarginSettlementLag = # Replace with your value
match_tolerance: Optional[Union[StrictFloat, StrictInt]] = # Replace with your value
variation_margin: Optional[List[MarginItem]] = # Replace with your value
initial_margin: Optional[List[MarginItem]] = # Replace with your value
properties: Optional[Dict[str, ModelProperty]] = # Replace with your value
effective_at: Optional[datetime] = # Replace with your value
collateral_agreement_request_instance = CollateralAgreementRequest(code=code, counterparty_id=counterparty_id, applicability_filter=applicability_filter, base_currency=base_currency, cut_label=cut_label, recipe_id=recipe_id, minimum_transfer_amount=minimum_transfer_amount, rounding=rounding, settlement_lag=settlement_lag, match_tolerance=match_tolerance, variation_margin=variation_margin, initial_margin=initial_margin, properties=properties, effective_at=effective_at)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

