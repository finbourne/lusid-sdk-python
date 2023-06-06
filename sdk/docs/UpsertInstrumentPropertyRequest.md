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

# TODO update the JSON string below
json = "{}"
# create an instance of UpsertInstrumentPropertyRequest from a JSON string
upsert_instrument_property_request_instance = UpsertInstrumentPropertyRequest.from_json(json)
# print the JSON string representation of the object
print UpsertInstrumentPropertyRequest.to_json()

# convert the object into a dict
upsert_instrument_property_request_dict = upsert_instrument_property_request_instance.to_dict()
# create an instance of UpsertInstrumentPropertyRequest from a dict
upsert_instrument_property_request_form_dict = upsert_instrument_property_request.from_dict(upsert_instrument_property_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


