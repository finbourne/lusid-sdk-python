# InstrumentProperties


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**href** | **str** | The specific Uniform Resource Identifier (URI) for this resource at the requested effective and asAt datetime. | [optional] 
**properties** | [**Dict[str, ModelProperty]**](ModelProperty.md) | The instrument properties. These will be from the &#39;Instrument&#39; domain. | [optional] 
**version** | [**Version**](Version.md) |  | [optional] 
**links** | [**List[Link]**](Link.md) |  | [optional] 

## Example

```python
from lusid.models.instrument_properties import InstrumentProperties

# TODO update the JSON string below
json = "{}"
# create an instance of InstrumentProperties from a JSON string
instrument_properties_instance = InstrumentProperties.from_json(json)
# print the JSON string representation of the object
print InstrumentProperties.to_json()

# convert the object into a dict
instrument_properties_dict = instrument_properties_instance.to_dict()
# create an instance of InstrumentProperties from a dict
instrument_properties_form_dict = instrument_properties.from_dict(instrument_properties_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


