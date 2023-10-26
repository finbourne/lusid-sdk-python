# PropertySchema


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**href** | **str** |  | [optional] 
**values** | [**Dict[str, FieldSchema]**](FieldSchema.md) |  | [optional] 
**links** | [**List[Link]**](Link.md) |  | [optional] 

## Example

```python
from lusid.models.property_schema import PropertySchema

# TODO update the JSON string below
json = "{}"
# create an instance of PropertySchema from a JSON string
property_schema_instance = PropertySchema.from_json(json)
# print the JSON string representation of the object
print PropertySchema.to_json()

# convert the object into a dict
property_schema_dict = property_schema_instance.to_dict()
# create an instance of PropertySchema from a dict
property_schema_form_dict = property_schema.from_dict(property_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


