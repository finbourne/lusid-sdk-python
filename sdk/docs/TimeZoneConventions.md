# TimeZoneConventions

Provides information on the primary time zone of an instrument and optional cut labels  for defining times to be used by instrument events.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**primary_time_zone** | **str** | The IANA time zone code for the instrument. | 
**start_of_day** | **str** | A LUSID Cut Label code used for generating instrument events at a time other than local midnight. | [optional] 
**primary_market_open** | **str** | A LUSID Cut Label code used for delaying the transaction time of certain instrument events until market open. | [optional] 
## Example

```python
from lusid.models.time_zone_conventions import TimeZoneConventions
from typing import Any, Dict, Optional
from pydantic.v1 import BaseModel, Field, constr, validator

primary_time_zone: StrictStr = "example_primary_time_zone"
start_of_day: Optional[StrictStr] = "example_start_of_day"
primary_market_open: Optional[StrictStr] = "example_primary_market_open"
time_zone_conventions_instance = TimeZoneConventions(primary_time_zone=primary_time_zone, start_of_day=start_of_day, primary_market_open=primary_market_open)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

