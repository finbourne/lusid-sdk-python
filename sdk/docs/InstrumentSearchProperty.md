# InstrumentSearchProperty

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** | The property key of instrument property to search for. This will be from the &#39;Instrument&#39; domain and will take the format {domain}/{scope}/{code} e.g. &#39;Instrument/system/Isin&#39; or &#39;Instrument/MyScope/AssetClass&#39;. | 
**value** | **str** | The value of the property e.g. &#39;US0378331005&#39; or &#39;Equity&#39;. | 
## Example

```python
from lusid.models.instrument_search_property import InstrumentSearchProperty
from typing import Any, Dict
from pydantic.v1 import BaseModel, Field, StrictStr, constr

key: StrictStr = "example_key"
value: StrictStr = "example_value"
instrument_search_property_instance = InstrumentSearchProperty(key=key, value=value)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

