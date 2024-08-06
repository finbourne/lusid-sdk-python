# InstrumentMatch

A collection of instrument search results

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**mastered_instruments** | [**List[InstrumentDefinition]**](InstrumentDefinition.md) | The collection of instruments found by the search which have been mastered within LUSID. | [optional] 
**external_instruments** | [**List[InstrumentDefinition]**](InstrumentDefinition.md) | The collection of instruments found by the search which have not been mastered within LUSID and instead found via OpenFIGI. | [optional] 

## Example

```python
from lusid.models.instrument_match import InstrumentMatch

# TODO update the JSON string below
json = "{}"
# create an instance of InstrumentMatch from a JSON string
instrument_match_instance = InstrumentMatch.from_json(json)
# print the JSON string representation of the object
print InstrumentMatch.to_json()

# convert the object into a dict
instrument_match_dict = instrument_match_instance.to_dict()
# create an instance of InstrumentMatch from a dict
instrument_match_form_dict = instrument_match.from_dict(instrument_match_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


