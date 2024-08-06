# BatchUpsertPropertyDefinitionPropertiesResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**values** | [**Dict[str, ModelProperty]**](ModelProperty.md) | The properties that have been successfully upserted | 
**failed** | [**Dict[str, ErrorDetail]**](ErrorDetail.md) | The properties that could not be upserted along with a reason for their failure. | 
**as_at_date** | **datetime** | The as-at datetime at which properties were created or updated. | 
**links** | [**List[Link]**](Link.md) |  | [optional] 

## Example

```python
from lusid.models.batch_upsert_property_definition_properties_response import BatchUpsertPropertyDefinitionPropertiesResponse

# TODO update the JSON string below
json = "{}"
# create an instance of BatchUpsertPropertyDefinitionPropertiesResponse from a JSON string
batch_upsert_property_definition_properties_response_instance = BatchUpsertPropertyDefinitionPropertiesResponse.from_json(json)
# print the JSON string representation of the object
print BatchUpsertPropertyDefinitionPropertiesResponse.to_json()

# convert the object into a dict
batch_upsert_property_definition_properties_response_dict = batch_upsert_property_definition_properties_response_instance.to_dict()
# create an instance of BatchUpsertPropertyDefinitionPropertiesResponse from a dict
batch_upsert_property_definition_properties_response_form_dict = batch_upsert_property_definition_properties_response.from_dict(batch_upsert_property_definition_properties_response_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


