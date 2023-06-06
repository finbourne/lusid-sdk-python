# InstrumentSearchProperty


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** | The property key of instrument property to search for. This will be from the &#39;Instrument&#39; domain and will take the format {domain}/{scope}/{code} e.g. &#39;Instrument/system/Isin&#39; or &#39;Instrument/MyScope/AssetClass&#39;. | 
**value** | **str** | The value of the property e.g. &#39;US0378331005&#39; or &#39;Equity&#39;. | 

## Example

```python
from lusid.models.instrument_search_property import InstrumentSearchProperty

# TODO update the JSON string below
json = "{}"
# create an instance of InstrumentSearchProperty from a JSON string
instrument_search_property_instance = InstrumentSearchProperty.from_json(json)
# print the JSON string representation of the object
print InstrumentSearchProperty.to_json()

# convert the object into a dict
instrument_search_property_dict = instrument_search_property_instance.to_dict()
# create an instance of InstrumentSearchProperty from a dict
instrument_search_property_form_dict = instrument_search_property.from_dict(instrument_search_property_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


