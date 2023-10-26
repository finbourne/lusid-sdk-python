# InstrumentDefinition


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name of the instrument. | 
**identifiers** | [**Dict[str, InstrumentIdValue]**](InstrumentIdValue.md) | A set of identifiers that can be used to identify the instrument. At least one of these must be configured to be a unique identifier. | 
**properties** | [**List[ModelProperty]**](ModelProperty.md) | Set of unique instrument properties and associated values to store with the instrument. Each property must be from the &#39;Instrument&#39; domain. | [optional] 
**look_through_portfolio_id** | [**ResourceId**](ResourceId.md) |  | [optional] 
**definition** | [**LusidInstrument**](LusidInstrument.md) |  | [optional] 

## Example

```python
from lusid.models.instrument_definition import InstrumentDefinition

# TODO update the JSON string below
json = "{}"
# create an instance of InstrumentDefinition from a JSON string
instrument_definition_instance = InstrumentDefinition.from_json(json)
# print the JSON string representation of the object
print InstrumentDefinition.to_json()

# convert the object into a dict
instrument_definition_dict = instrument_definition_instance.to_dict()
# create an instance of InstrumentDefinition from a dict
instrument_definition_form_dict = instrument_definition.from_dict(instrument_definition_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


