# UpsertInstrumentPropertyRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**identifier_type** | **str** | The unique identifier type to search for the instrument, for example &#39;Figi&#39;. | 
**identifier** | **str** | A value of that type to identify the instrument to upsert properties for, for example &#39;BBG000BLNNV0&#39;. | 
**properties** | [**List[ModelProperty]**](ModelProperty.md) | A set of instrument properties and associated values to store for the instrument. Each property must be from the &#39;Instrument&#39; domain. | [optional] 
## Example

```python
from lusid.models.upsert_instrument_property_request import UpsertInstrumentPropertyRequest
from typing import Any, Dict, List, Optional
from pydantic.v1 import BaseModel, Field, conlist, constr

identifier_type: StrictStr = "example_identifier_type"
identifier: StrictStr = "example_identifier"
properties: Optional[conlist(ModelProperty)] = # Replace with your value
upsert_instrument_property_request_instance = UpsertInstrumentPropertyRequest(identifier_type=identifier_type, identifier=identifier, properties=properties)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

