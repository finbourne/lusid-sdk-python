# ShareClassDetails

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**lusid_instrument_id** | **str** | LUSID&#39;s internal unique instrument identifier, resolved from the share class&#39; instrument identifiers | [optional] 
**instrument_scope** | **str** | The scope in which the share class instrument lies. | [optional] 
**short_code** | **str** | The unique code within the fund for the share class instrument. | [optional] 
**dom_currency** | **str** | The domestic currency of the share class instrument | [optional] 
**instrument_active** | **bool** | If the instrument of the share class is active. | [optional] 
## Example

```python
from lusid.models.share_class_details import ShareClassDetails
from typing import Any, Dict, Optional
from pydantic.v1 import BaseModel, Field, StrictBool, StrictStr, constr, validator

lusid_instrument_id: Optional[StrictStr] = "example_lusid_instrument_id"
instrument_scope: Optional[StrictStr] = "example_instrument_scope"
short_code: Optional[StrictStr] = "example_short_code"
dom_currency: Optional[StrictStr] = "example_dom_currency"
instrument_active: Optional[StrictBool] = # Replace with your value
instrument_active:Optional[StrictBool] = None
share_class_details_instance = ShareClassDetails(lusid_instrument_id=lusid_instrument_id, instrument_scope=instrument_scope, short_code=short_code, dom_currency=dom_currency, instrument_active=instrument_active)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

