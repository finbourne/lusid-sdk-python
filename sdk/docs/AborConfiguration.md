# AborConfiguration

An AborConfiguration entity.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**href** | **str** | The specific Uniform Resource Identifier (URI) for this resource at the requested effective and asAt datetime. | [optional] 
**id** | [**ResourceId**](ResourceId.md) |  | 
**description** | **str** | The description for the AborConfiguration. | [optional] 
**name** | **str** | The given name for the AborConfiguration. | [optional] 
**recipe_id** | [**ResourceId**](ResourceId.md) |  | [optional] 
**chart_of_accounts_id** | [**ResourceId**](ResourceId.md) |  | [optional] 
**properties** | [**Dict[str, ModelProperty]**](ModelProperty.md) | Properties to add to the AborConfiguration. | [optional] 
**version** | [**Version**](Version.md) |  | [optional] 
**links** | [**List[Link]**](Link.md) |  | [optional] 

## Example

```python
from lusid.models.abor_configuration import AborConfiguration

# TODO update the JSON string below
json = "{}"
# create an instance of AborConfiguration from a JSON string
abor_configuration_instance = AborConfiguration.from_json(json)
# print the JSON string representation of the object
print AborConfiguration.to_json()

# convert the object into a dict
abor_configuration_dict = abor_configuration_instance.to_dict()
# create an instance of AborConfiguration from a dict
abor_configuration_form_dict = abor_configuration.from_dict(abor_configuration_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


