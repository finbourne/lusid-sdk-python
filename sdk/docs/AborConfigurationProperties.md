# AborConfigurationProperties


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**href** | **str** | The specific Uniform Resource Identifier (URI) for this resource at the requested effective and asAt datetime. | [optional] 
**properties** | [**Dict[str, ModelProperty]**](ModelProperty.md) | The AborConfiguration properties. These will be from the &#39;AborConfiguration&#39; domain. | [optional] 
**version** | [**Version**](Version.md) |  | [optional] 
**links** | [**List[Link]**](Link.md) |  | [optional] 

## Example

```python
from lusid.models.abor_configuration_properties import AborConfigurationProperties

# TODO update the JSON string below
json = "{}"
# create an instance of AborConfigurationProperties from a JSON string
abor_configuration_properties_instance = AborConfigurationProperties.from_json(json)
# print the JSON string representation of the object
print AborConfigurationProperties.to_json()

# convert the object into a dict
abor_configuration_properties_dict = abor_configuration_properties_instance.to_dict()
# create an instance of AborConfigurationProperties from a dict
abor_configuration_properties_form_dict = abor_configuration_properties.from_dict(abor_configuration_properties_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


