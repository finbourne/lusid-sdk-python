# FundConfiguration


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**href** | **str** | The specific Uniform Resource Identifier (URI) for this resource at the requested effective and asAt datetime. | [optional] 
**id** | [**ResourceId**](ResourceId.md) |  | 
**display_name** | **str** | The name of the FundConfiguration. | [optional] 
**description** | **str** | A description for the FundConfiguration. | [optional] 
**component_rules** | [**List[ComponentRule]**](ComponentRule.md) | The first matching rule decides the set of filters used. | [optional] 
**properties** | [**Dict[str, ModelProperty]**](ModelProperty.md) | A set of properties for the Fund Configuration. | [optional] 
**version** | [**Version**](Version.md) |  | [optional] 
**links** | [**List[Link]**](Link.md) |  | [optional] 

## Example

```python
from lusid.models.fund_configuration import FundConfiguration

# TODO update the JSON string below
json = "{}"
# create an instance of FundConfiguration from a JSON string
fund_configuration_instance = FundConfiguration.from_json(json)
# print the JSON string representation of the object
print FundConfiguration.to_json()

# convert the object into a dict
fund_configuration_dict = fund_configuration_instance.to_dict()
# create an instance of FundConfiguration from a dict
fund_configuration_form_dict = fund_configuration.from_dict(fund_configuration_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


