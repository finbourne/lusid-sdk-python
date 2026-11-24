# HoldingEntitlementRequest

The request to create or update a holding entitlement.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**holding_entitlement_id** | **str** | The unique identifier of the entitlement within the portfolio | 
**holding_id** | **int** | The id of the holding the entitlement is for, as the holdings endpoints report it | 
**instrument_scope** | **str** | The scope of the holding&#39;s instrument | 
**instrument_id** | **str** | The LUSID instrument identifier of the holding&#39;s instrument | 
**ex_date** | **datetime** | The date the entitlement is booked at. Must be in UTC | 
**payment_date** | **datetime** | The date the entitlement&#39;s transactions settle. Must be in UTC and not before the ex date | 
**announcement_date** | **datetime** | The date the corporate action was announced. Optional; must be in UTC and not after the ex date | [optional] 
**record_date** | **datetime** | The date on which holders are recorded as entitled. Optional; must be in UTC and not after the payment date | [optional] 
**description** | **str** | A description of the entitlement | [optional] 
**parent_units_retained** | **float** | The units of the parent holding that the holder keeps. The remainder of the holding leaves the parent. Cannot be given with ParentUnitsDelivered | [optional] 
**parent_units_delivered** | **float** | The units of the parent holding that leave it. The alternative to ParentUnitsRetained. Where neither is given, no units leave the parent | [optional] 
**parent_cost_adjustment** | **float** | A signed adjustment to the parent holding&#39;s cost, apportioned across its tax lots. Used where cost moves with no child position and no cash | [optional] 
**parent_lot_selection** | **str** | How the parent&#39;s units leave its tax lots when they are realised. ProRata takes units from every lot in proportion to its units. PortfolioSalesRule takes them by the portfolio&#39;s accounting method. A departure at book value is always pro rata. The default is ProRata. Available values: ProRata, PortfolioSalesRule. | [optional] 
**child_lot_treatment** | **str** | The tax lots of a position that carries the parent&#39;s cost, from a CarryCost or ReceiveAndSell leg. RetainLots gives one lot for each parent lot, with that lot&#39;s purchase date. NewLot gives one lot with the ex date as its purchase date. The default is RetainLots. A ParentLotSelection of PortfolioSalesRule requires NewLot. Available values: RetainLots, NewLot. | [optional] 
**capital_adjustment_spread** | **str** | How a return of capital and income reclassified as capital are spread across the parent&#39;s tax lots. ByCost spreads by each lot&#39;s cost, and ByUnits by each lot&#39;s units. The default is ByCost. Available values: ByCost, ByUnits. | [optional] 
**transaction_properties** | [**Dict[str, PerpetualProperty]**](PerpetualProperty.md) | The transaction properties to set on every transaction the entitlement books, at most 100. Each must be in the Transaction domain. A value given here replaces the value the transaction template gives for the same property, and a leg&#39;s value replaces it on the transactions of that leg. A property that is a sub-holding key of the portfolio cannot be given | [optional] 
**legs** | [**List[EntitlementLegRequest]**](EntitlementLegRequest.md) | The child positions and cash movements the corporate action produces for this holding, at most 100. May be empty where the entitlement only adjusts the parent&#39;s cost | [optional] 
## Example

```python
from lusid.models.holding_entitlement_request import HoldingEntitlementRequest
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

holding_entitlement_id: StrictStr = "example_holding_entitlement_id"
holding_id: StrictInt = # Replace with your value
instrument_scope: StrictStr = "example_instrument_scope"
instrument_id: StrictStr = "example_instrument_id"
ex_date: datetime = # Replace with your value
payment_date: datetime = # Replace with your value
announcement_date: Optional[datetime] = # Replace with your value
record_date: Optional[datetime] = # Replace with your value
description: Optional[StrictStr] = "example_description"
parent_units_retained: Optional[Union[StrictFloat, StrictInt]] = # Replace with your value
parent_units_delivered: Optional[Union[StrictFloat, StrictInt]] = # Replace with your value
parent_cost_adjustment: Optional[Union[StrictFloat, StrictInt]] = # Replace with your value
parent_lot_selection: Optional[StrictStr] = "example_parent_lot_selection"
child_lot_treatment: Optional[StrictStr] = "example_child_lot_treatment"
capital_adjustment_spread: Optional[StrictStr] = "example_capital_adjustment_spread"
transaction_properties: Optional[Dict[str, PerpetualProperty]] = # Replace with your value
legs: Optional[List[EntitlementLegRequest]] = # Replace with your value
holding_entitlement_request_instance = HoldingEntitlementRequest(holding_entitlement_id=holding_entitlement_id, holding_id=holding_id, instrument_scope=instrument_scope, instrument_id=instrument_id, ex_date=ex_date, payment_date=payment_date, announcement_date=announcement_date, record_date=record_date, description=description, parent_units_retained=parent_units_retained, parent_units_delivered=parent_units_delivered, parent_cost_adjustment=parent_cost_adjustment, parent_lot_selection=parent_lot_selection, child_lot_treatment=child_lot_treatment, capital_adjustment_spread=capital_adjustment_spread, transaction_properties=transaction_properties, legs=legs)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

