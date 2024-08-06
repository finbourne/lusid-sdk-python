# InstrumentIdValue


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | **str** | The value of the identifier. | 
**effective_at** | **datetime** | The effective datetime from which the identifier will be valid. If left unspecified the default value is the beginning of time. | [optional] 

## Example

```python
from lusid.models.instrument_id_value import InstrumentIdValue

# TODO update the JSON string below
json = "{}"
# create an instance of InstrumentIdValue from a JSON string
instrument_id_value_instance = InstrumentIdValue.from_json(json)
# print the JSON string representation of the object
print InstrumentIdValue.to_json()

# convert the object into a dict
instrument_id_value_dict = instrument_id_value_instance.to_dict()
# create an instance of InstrumentIdValue from a dict
instrument_id_value_form_dict = instrument_id_value.from_dict(instrument_id_value_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


