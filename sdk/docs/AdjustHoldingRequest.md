# AdjustHoldingRequest

This request specifies target holdings. i.e. holding data that the  system should match. When processed by the movement  engine, it will create 'true-up' adjustments on the fly.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**instrument_identifiers** | **Dict[str, Optional[str]]** | A set of instrument identifiers that can resolve the holding adjustment to a unique instrument. | 
**sub_holding_keys** | [**Dict[str, PerpetualProperty]**](PerpetualProperty.md) | Set of unique transaction properties and associated values to store with the holding adjustment transaction automatically created by LUSID. Each property must be from the &#39;Transaction&#39; domain. | [optional] 
**properties** | [**Dict[str, PerpetualProperty]**](PerpetualProperty.md) | Set of unique holding properties and associated values to store with the target holding. Each property must be from the &#39;Holding&#39; domain. | [optional] 
**tax_lots** | [**List[TargetTaxLotRequest]**](TargetTaxLotRequest.md) | The tax-lots that together make up the target holding. | 
**currency** | **str** | The Holding currency. This needs to be equal with the one on the TaxLot -&gt; cost if one is specified | [optional] 
**custodian_account_id** | [**ResourceId**](ResourceId.md) |  | [optional] 
## Example

```python
from lusid.models.adjust_holding_request import AdjustHoldingRequest
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

instrument_identifiers: Dict[str, Optional[StrictStr]] = # Replace with your value
sub_holding_keys: Optional[Dict[str, PerpetualProperty]] = # Replace with your value
properties: Optional[Dict[str, PerpetualProperty]] = # Replace with your value
tax_lots: List[TargetTaxLotRequest] = # Replace with your value
currency: Optional[StrictStr] = "example_currency"
custodian_account_id: Optional[ResourceId] = # Replace with your value
adjust_holding_request_instance = AdjustHoldingRequest(instrument_identifiers=instrument_identifiers, sub_holding_keys=sub_holding_keys, properties=properties, tax_lots=tax_lots, currency=currency, custodian_account_id=custodian_account_id)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

