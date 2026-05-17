# ValuationPointInstrument

An Instrument held at a Valuation Point, including its origin
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**instrument** | [**Instrument**](Instrument.md) |  | [optional] 
**valuation_point_origin** | **str** | Designates if the instrument was originally part of the Valuation Point or if it was added as part of a Complex Close action. Available values: None, Original, Added. | [optional] 
**added_origin_valuation_point_code** | **str** | The Valuation Point, only for an Instrument added as part of a Complex Close action. | [optional] 
**added_origin_valuation_point_variant_code** | **str** | The Valuation Point variant, only for Instruments added as part of a Complex Close action. | [optional] 
**properties** | [**Dict[str, ModelProperty]**](ModelProperty.md) | The requested instrument properties. These will be from the &#39;Instrument&#39; domain. | [optional] 
## Example

```python
from lusid.models.valuation_point_instrument import ValuationPointInstrument
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

instrument: Optional[Instrument] = None
valuation_point_origin: Optional[StrictStr] = "example_valuation_point_origin"
added_origin_valuation_point_code: Optional[StrictStr] = "example_added_origin_valuation_point_code"
added_origin_valuation_point_variant_code: Optional[StrictStr] = "example_added_origin_valuation_point_variant_code"
properties: Optional[Dict[str, ModelProperty]] = # Replace with your value
valuation_point_instrument_instance = ValuationPointInstrument(instrument=instrument, valuation_point_origin=valuation_point_origin, added_origin_valuation_point_code=added_origin_valuation_point_code, added_origin_valuation_point_variant_code=added_origin_valuation_point_variant_code, properties=properties)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

