# ResourceListOfInstrumentIdTypeDescriptor


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**values** | [**List[InstrumentIdTypeDescriptor]**](InstrumentIdTypeDescriptor.md) |  | 
**href** | **str** |  | [optional] 
**links** | [**List[Link]**](Link.md) |  | [optional] 
**next_page** | **str** |  | [optional] 
**previous_page** | **str** |  | [optional] 

## Example

```python
from lusid.models.resource_list_of_instrument_id_type_descriptor import ResourceListOfInstrumentIdTypeDescriptor

# TODO update the JSON string below
json = "{}"
# create an instance of ResourceListOfInstrumentIdTypeDescriptor from a JSON string
resource_list_of_instrument_id_type_descriptor_instance = ResourceListOfInstrumentIdTypeDescriptor.from_json(json)
# print the JSON string representation of the object
print ResourceListOfInstrumentIdTypeDescriptor.to_json()

# convert the object into a dict
resource_list_of_instrument_id_type_descriptor_dict = resource_list_of_instrument_id_type_descriptor_instance.to_dict()
# create an instance of ResourceListOfInstrumentIdTypeDescriptor from a dict
resource_list_of_instrument_id_type_descriptor_form_dict = resource_list_of_instrument_id_type_descriptor.from_dict(resource_list_of_instrument_id_type_descriptor_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


