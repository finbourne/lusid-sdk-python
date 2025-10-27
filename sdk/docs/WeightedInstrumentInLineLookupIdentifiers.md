# WeightedInstrumentInLineLookupIdentifiers

External market codes and identifiers for the equity, e.g. IBM.  Required for valuation via SimpleStatic (look-up pricing).  Valuation will not succeed without a matching quote.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**lusid_instrument_id** | **str** |  | [optional] 
**isin** | **str** |  | [optional] 
**sedol** | **str** |  | [optional] 
**cusip** | **str** |  | [optional] 
**client_internal** | **str** |  | [optional] 
**figi** | **str** |  | [optional] 
**ric** | **str** |  | [optional] 
**quote_perm_id** | **str** |  | [optional] 
**red_code** | **str** |  | [optional] 
**bbgid** | **str** |  | [optional] 
**ice_code** | **str** |  | [optional] 
## Example

```python
from lusid.models.weighted_instrument_in_line_lookup_identifiers import WeightedInstrumentInLineLookupIdentifiers
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

lusid_instrument_id: Optional[StrictStr] = "example_lusid_instrument_id"
isin: Optional[StrictStr] = "example_isin"
sedol: Optional[StrictStr] = "example_sedol"
cusip: Optional[StrictStr] = "example_cusip"
client_internal: Optional[StrictStr] = "example_client_internal"
figi: Optional[StrictStr] = "example_figi"
ric: Optional[StrictStr] = "example_ric"
quote_perm_id: Optional[StrictStr] = "example_quote_perm_id"
red_code: Optional[StrictStr] = "example_red_code"
bbgid: Optional[StrictStr] = "example_bbgid"
ice_code: Optional[StrictStr] = "example_ice_code"
weighted_instrument_in_line_lookup_identifiers_instance = WeightedInstrumentInLineLookupIdentifiers(lusid_instrument_id=lusid_instrument_id, isin=isin, sedol=sedol, cusip=cusip, client_internal=client_internal, figi=figi, ric=ric, quote_perm_id=quote_perm_id, red_code=red_code, bbgid=bbgid, ice_code=ice_code)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

