# FundConfigurationProperties


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**href** | **str** | The specific Uniform Resource Identifier (URI) for this resource at the requested effective and asAt datetime. | [optional] 
**properties** | [**Dict[str, ModelProperty]**](ModelProperty.md) | The Fund Configuration properties. These will be from the &#39;FundConfiguration&#39; domain. | [optional] 
**version** | [**Version**](Version.md) |  | [optional] 
**links** | [**List[Link]**](Link.md) |  | [optional] 

## Example

```python
from lusid.models.fund_configuration_properties import FundConfigurationProperties

# TODO update the JSON string below
json = "{}"
# create an instance of FundConfigurationProperties from a JSON string
fund_configuration_properties_instance = FundConfigurationProperties.from_json(json)
# print the JSON string representation of the object
print FundConfigurationProperties.to_json()

# convert the object into a dict
fund_configuration_properties_dict = fund_configuration_properties_instance.to_dict()
# create an instance of FundConfigurationProperties from a dict
fund_configuration_properties_form_dict = fund_configuration_properties.from_dict(fund_configuration_properties_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


