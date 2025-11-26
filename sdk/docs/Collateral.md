# Collateral

Representation of the collateral of a repurchase agreement, along with related details of the agreement.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**buyer_receives_cashflows** | **bool** | Does the buyer of the FlexibleRepo receive the cashflows from any collateral instruments, or do they get paid to the seller. | 
**buyer_receives_corporate_action_payments** | **bool** | Does the buyer of the FlexibleRepo receive any dividend or cash payments as the result of a corporate action  on any of the collateral instruments, or are these amounts paid to the seller.  Referred to as \&quot;manufactured payments\&quot; in the UK, and valid only under a repo with GMRA in Europe | 
**collateral_instruments** | [**List[CollateralInstrument]**](CollateralInstrument.md) | List of any collateral instruments. | [optional] 
**collateral_value** | **float** | Total value of the collateral before any margin or haircut applied.  Can be provided instead of PurchasePrice, so that PurchasePrice can be inferred from the CollateralValue and one of  Haircut or Margin. | [optional] 
**defer_manufactured_payments** | **bool** | Indicates whether manufactured collateral payments are capitalised (i.e. deferred). Capitalised payments will  be deferred to the maturity date of the repo and if applicable interest will be accrued at the repo rate.  Defaults to false. | [optional] 
## Example

```python
from lusid.models.collateral import Collateral
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

buyer_receives_cashflows: StrictBool = # Replace with your value
buyer_receives_cashflows:StrictBool = True
buyer_receives_corporate_action_payments: StrictBool = # Replace with your value
buyer_receives_corporate_action_payments:StrictBool = True
collateral_instruments: Optional[List[CollateralInstrument]] = # Replace with your value
collateral_value: Optional[Union[StrictFloat, StrictInt]] = # Replace with your value
defer_manufactured_payments: Optional[StrictBool] = # Replace with your value
defer_manufactured_payments:Optional[StrictBool] = None
collateral_instance = Collateral(buyer_receives_cashflows=buyer_receives_cashflows, buyer_receives_corporate_action_payments=buyer_receives_corporate_action_payments, collateral_instruments=collateral_instruments, collateral_value=collateral_value, defer_manufactured_payments=defer_manufactured_payments)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

