# WeightedInstruments

Class that models a set of instruments of which each has some quantity and can be identified by a unique label.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**instruments** | [**List[WeightedInstrument]**](WeightedInstrument.md) | The instruments that are held in the set. | 

## Example

```python
from lusid.models.weighted_instruments import WeightedInstruments

# TODO update the JSON string below
json = "{}"
# create an instance of WeightedInstruments from a JSON string
weighted_instruments_instance = WeightedInstruments.from_json(json)
# print the JSON string representation of the object
print WeightedInstruments.to_json()

# convert the object into a dict
weighted_instruments_dict = weighted_instruments_instance.to_dict()
# create an instance of WeightedInstruments from a dict
weighted_instruments_form_dict = weighted_instruments.from_dict(weighted_instruments_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


