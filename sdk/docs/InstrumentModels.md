# InstrumentModels

Supported pricing models for an instrument.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**instrument_id** | **str** | The unique LUSID Instrument Identifier (LUID) of the instrument. | [optional] 
**supported_models** | **List[str]** | The pricing models supported by the instrument e.g. &#39;Discounting&#39;. | [optional] 
**links** | [**List[Link]**](Link.md) |  | [optional] 

## Example

```python
from lusid.models.instrument_models import InstrumentModels

# TODO update the JSON string below
json = "{}"
# create an instance of InstrumentModels from a JSON string
instrument_models_instance = InstrumentModels.from_json(json)
# print the JSON string representation of the object
print InstrumentModels.to_json()

# convert the object into a dict
instrument_models_dict = instrument_models_instance.to_dict()
# create an instance of InstrumentModels from a dict
instrument_models_form_dict = instrument_models.from_dict(instrument_models_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


