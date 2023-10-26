# InstrumentIdTypeDescriptor

The description of an allowable instrument identifier.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**identifier_type** | **str** | The name of the identifier type. | 
**property_key** | **str** | The property key that corresponds to the identifier type. | 
**is_unique_identifier_type** | **bool** | Whether or not the identifier type is enforced to be unique. | 

## Example

```python
from lusid.models.instrument_id_type_descriptor import InstrumentIdTypeDescriptor

# TODO update the JSON string below
json = "{}"
# create an instance of InstrumentIdTypeDescriptor from a JSON string
instrument_id_type_descriptor_instance = InstrumentIdTypeDescriptor.from_json(json)
# print the JSON string representation of the object
print InstrumentIdTypeDescriptor.to_json()

# convert the object into a dict
instrument_id_type_descriptor_dict = instrument_id_type_descriptor_instance.to_dict()
# create an instance of InstrumentIdTypeDescriptor from a dict
instrument_id_type_descriptor_form_dict = instrument_id_type_descriptor.from_dict(instrument_id_type_descriptor_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


