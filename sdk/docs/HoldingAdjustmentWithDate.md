# HoldingAdjustmentWithDate

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**effective_at** | **datetime** | The effective date of the holding adjustment | [optional] 
**instrument_identifiers** | **Dict[str, str]** | A set of instrument identifiers that can resolve the holding adjustment to a unique instrument. | [optional] 
**instrument_scope** | **str** | The scope of the instrument that the holding adjustment is in. | [optional] 
**instrument_uid** | **str** | The unique Lusid Instrument Id (LUID) of the instrument that the holding adjustment is in. | 
**sub_holding_keys** | [**Dict[str, PerpetualProperty]**](PerpetualProperty.md) | The set of unique transaction properties and associated values stored with the holding adjustment transactions automatically created by LUSID. Each property will be from the &#39;Transaction&#39; domain. | [optional] 
**properties** | [**Dict[str, PerpetualProperty]**](PerpetualProperty.md) | The set of unique holding properties and associated values stored with the target holding. Each property will be from the &#39;Holding&#39; domain. | [optional] 
**tax_lots** | [**List[TargetTaxLot]**](TargetTaxLot.md) | The tax-lots that together make up the target holding. | 
**currency** | **str** | The Holding currency. | [optional] 
**custodian_account_id** | [**ResourceId**](ResourceId.md) |  | [optional] 
## Example

```python
from lusid.models.holding_adjustment_with_date import HoldingAdjustmentWithDate
from typing import Any, Dict, List, Optional
from pydantic.v1 import BaseModel, Field, StrictStr, conlist, constr
from datetime import datetime
effective_at: Optional[datetime] = # Replace with your value
instrument_identifiers: Optional[Dict[str, StrictStr]] = # Replace with your value
instrument_scope: Optional[StrictStr] = "example_instrument_scope"
instrument_uid: StrictStr = "example_instrument_uid"
sub_holding_keys: Optional[Dict[str, PerpetualProperty]] = # Replace with your value
properties: Optional[Dict[str, PerpetualProperty]] = # Replace with your value
tax_lots: conlist(TargetTaxLot) = # Replace with your value
currency: Optional[StrictStr] = "example_currency"
custodian_account_id: Optional[ResourceId] = # Replace with your value
holding_adjustment_with_date_instance = HoldingAdjustmentWithDate(effective_at=effective_at, instrument_identifiers=instrument_identifiers, instrument_scope=instrument_scope, instrument_uid=instrument_uid, sub_holding_keys=sub_holding_keys, properties=properties, tax_lots=tax_lots, currency=currency, custodian_account_id=custodian_account_id)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

