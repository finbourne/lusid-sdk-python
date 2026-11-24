# EntitlementLegRequest

One child position or cash movement produced by a holding entitlement.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**leg_id** | **str** | The identifier of this leg, unique within the entitlement and included in the identifiers of the transactions it produces | 
**instrument_scope** | **str** | The scope of the instrument this leg receives. Given together with the instrument identifier | [optional] 
**instrument_id** | **str** | The LUSID instrument identifier of the instrument this leg receives. Required for CarryCost, ReceiveAndSell, ReceiveInterestInKind and ReceiveDividendInKind, optional for RealiseAtAmount where its absence settles the proceeds to cash, and absent for every treatment that produces no position | [optional] 
**units** | **float** | The units this leg receives. Required where the leg names an instrument and absent where it does not | [optional] 
**cost_fraction** | **float** | The share of the parent&#39;s pre-event cost that this leg takes, from 0 to 1. Required for CarryCost and ReceiveAndSell and absent otherwise. The fractions across all legs must not sum to more than 1 | [optional] 
**cash_paid** | **float** | The cash the holder pays to receive this leg. It adds to the leg&#39;s cost and is neither income nor expense. Must not be negative | [optional] 
**price** | **float** | The stated price of this leg. Must not be negative for RealiseAtAmount and ReceiveAndSell | [optional] 
**amount** | **float** | The stated amount of this leg. Required unless the treatment is CarryCost. For RealiseCash it is the signed cash moved; for ReceiveInterestInKind, ReceiveDividendInKind and for every other treatment that produces no position it must be positive. For RealiseAtAmount and ReceiveAndSell it must not be negative | [optional] 
**settlement_currency** | **str** | The currency of this leg&#39;s cash movement. Defaults to the currency of the holding, and must be that currency where given. The RealiseAtAmount legs of an entitlement must all settle in one currency | [optional] 
**treatment** | **str** | How this leg is booked: CarryCost, RealiseAtAmount, ReceiveAndSell, RealiseCash, ExpenseCash, ReturnOfCapital, ReceiveDividendIncome, ReceiveInterestIncome, ReceiveOtherIncome, PayWithholdingTax, PayFee, ReceiveInterestInKind, ReclassifyIncomeAsCapital or ReceiveDividendInKind. Available values: CarryCost, RealiseAtAmount, ReceiveAndSell, RealiseCash, ExpenseCash, ReturnOfCapital, ReceiveDividendIncome, ReceiveInterestIncome, ReceiveOtherIncome, PayWithholdingTax, PayFee, ReceiveInterestInKind, ReclassifyIncomeAsCapital, ReceiveDividendInKind. | 
**transaction_properties** | [**Dict[str, PerpetualProperty]**](PerpetualProperty.md) | The transaction properties to set on every transaction this leg books, at most 100. Each must be in the Transaction domain. A value given here replaces the value the entitlement gives for the same property on this leg&#39;s transactions, and the value the transaction template gives | [optional] 
## Example

```python
from lusid.models.entitlement_leg_request import EntitlementLegRequest
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

leg_id: StrictStr = "example_leg_id"
instrument_scope: Optional[StrictStr] = "example_instrument_scope"
instrument_id: Optional[StrictStr] = "example_instrument_id"
units: Optional[Union[StrictFloat, StrictInt]] = # Replace with your value
cost_fraction: Optional[Union[StrictFloat, StrictInt]] = # Replace with your value
cash_paid: Optional[Union[StrictFloat, StrictInt]] = # Replace with your value
price: Optional[Union[StrictFloat, StrictInt]] = # Replace with your value
amount: Optional[Union[StrictFloat, StrictInt]] = # Replace with your value
settlement_currency: Optional[StrictStr] = "example_settlement_currency"
treatment: StrictStr = "example_treatment"
transaction_properties: Optional[Dict[str, PerpetualProperty]] = # Replace with your value
entitlement_leg_request_instance = EntitlementLegRequest(leg_id=leg_id, instrument_scope=instrument_scope, instrument_id=instrument_id, units=units, cost_fraction=cost_fraction, cash_paid=cash_paid, price=price, amount=amount, settlement_currency=settlement_currency, treatment=treatment, transaction_properties=transaction_properties)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

