# MarginItem

One margin arrangement under an agreement, either variation or initial.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** | The stable key that margin calls and custodian accounts refer to this item by. Unique across the agreement&#39;s variation and initial margin. | 
**trade_filter** | **str** | A filter selecting the trades this item covers. Required where the agreement has more than one margin item. | [optional] 
**settlement** | **str** | Whether margin is settled (Settled) or collateralised (Collateral). Optional. Available values: Collateral, Settled. | [optional] 
**legal_mechanism** | **str** | How title to posted collateral is held. One of TitleTransfer or SecurityInterest. Optional. Available values: TitleTransfer, SecurityInterest. | [optional] 
**we_post** | [**PartyTerms**](PartyTerms.md) |  | 
**they_post** | [**PartyTerms**](PartyTerms.md) |  | 
**eligible_collateral** | [**EligibleCollateralReferences**](EligibleCollateralReferences.md) |  | [optional] 
**calculation** | [**MarginCalculation**](MarginCalculation.md) |  | 
**margin_accounts** | [**MarginAccounts**](MarginAccounts.md) |  | [optional] 
## Example

```python
from lusid.models.margin_item import MarginItem
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

code: StrictStr = "example_code"
trade_filter: Optional[StrictStr] = "example_trade_filter"
settlement: Optional[StrictStr] = "example_settlement"
legal_mechanism: Optional[StrictStr] = "example_legal_mechanism"
we_post: PartyTerms = # Replace with your value
they_post: PartyTerms = # Replace with your value
eligible_collateral: Optional[EligibleCollateralReferences] = # Replace with your value
calculation: MarginCalculation
margin_accounts: Optional[MarginAccounts] = # Replace with your value
margin_item_instance = MarginItem(code=code, trade_filter=trade_filter, settlement=settlement, legal_mechanism=legal_mechanism, we_post=we_post, they_post=they_post, eligible_collateral=eligible_collateral, calculation=calculation, margin_accounts=margin_accounts)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

