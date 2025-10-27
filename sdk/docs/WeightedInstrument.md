# WeightedInstrument

Specification for a holding or quantity of (weight for) an instrument on a given date.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**quantity** | **float** | The quantity of the instrument that is owned. | [optional] 
**holding_identifier** | **str** | Identifier for the instrument.  For a single, unique trade or transaction this can be thought of as equivalent to the transaction identifier, or  a composite of the sub-holding keys for a regular sub-holding. When there are multiple transactions sharing the same underlying instrument  such as purchase of shares on multiple dates where tax implications are different this would not be the case.    In an inlined aggregation request if this is wanted to identify a line item, it can be specified in the set of aggregation keys given on the aggregation  request that accompanies the set of weighted instruments. | [optional] 
**instrument** | [**LusidInstrument**](LusidInstrument.md) |  | [optional] 
**in_line_lookup_identifiers** | [**WeightedInstrumentInLineLookupIdentifiers**](WeightedInstrumentInLineLookupIdentifiers.md) |  | [optional] 
**instrument_scope** | **str** | The scope in which to resolve the instrument, if no inlined definition is provided.  If left empty, the default scope will be used. | [optional] 
## Example

```python
from lusid.models.weighted_instrument import WeightedInstrument
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

quantity: Optional[Union[StrictFloat, StrictInt]] = # Replace with your value
holding_identifier: Optional[StrictStr] = "example_holding_identifier"
instrument: Optional[LusidInstrument] = None
in_line_lookup_identifiers: Optional[WeightedInstrumentInLineLookupIdentifiers] = # Replace with your value
instrument_scope: Optional[StrictStr] = "example_instrument_scope"
weighted_instrument_instance = WeightedInstrument(quantity=quantity, holding_identifier=holding_identifier, instrument=instrument, in_line_lookup_identifiers=in_line_lookup_identifiers, instrument_scope=instrument_scope)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

