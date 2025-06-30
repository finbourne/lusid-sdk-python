# CancelSingleHoldingAdjustmentRequest

This request specifies single target holding. i.e. holding data that the  system should match. And deletes previous adjustment made to that holding
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**instrument_identifiers** | **Dict[str, str]** | A set of instrument identifiers that can resolve the holding adjustment to a unique instrument. | 
**sub_holding_keys** | [**Dict[str, PerpetualProperty]**](PerpetualProperty.md) | The sub-holding properties which identify the holding. Each property must be from the &#39;Transaction&#39; domain. | [optional] 
**currency** | **str** | The Holding currency. | [optional] 
## Example

```python
from lusid.models.cancel_single_holding_adjustment_request import CancelSingleHoldingAdjustmentRequest
from typing import Any, Dict, Optional
from pydantic.v1 import BaseModel, Field, StrictStr

instrument_identifiers: Dict[str, StrictStr] = # Replace with your value
sub_holding_keys: Optional[Dict[str, PerpetualProperty]] = # Replace with your value
currency: Optional[StrictStr] = "example_currency"
cancel_single_holding_adjustment_request_instance = CancelSingleHoldingAdjustmentRequest(instrument_identifiers=instrument_identifiers, sub_holding_keys=sub_holding_keys, currency=currency)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

