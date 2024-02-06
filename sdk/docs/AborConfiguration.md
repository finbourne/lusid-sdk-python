# AborConfiguration

An AborConfiguration entity.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**href** | **str** | The specific Uniform Resource Identifier (URI) for this resource at the requested effective and asAt datetime. | [optional] 
**id** | [**ResourceId**](ResourceId.md) |  | 
**display_name** | **str** | The name of the Abor Configuration. | [optional] 
**description** | **str** | A description for the Abor Configuration. | [optional] 
**recipe_id** | [**ResourceId**](ResourceId.md) |  | [optional] 
**chart_of_accounts_id** | [**ResourceId**](ResourceId.md) |  | 
**posting_module_codes** | **List[str]** | The Posting Module Codes from which the rules to be applied are retrieved. | [optional] 
**cleardown_module_codes** | **List[str]** | The Cleardown Module Codes from which the rules to be applied are retrieved. | [optional] 
**properties** | [**Dict[str, ModelProperty]**](ModelProperty.md) | A set of properties for the Abor Configuration. | [optional] 
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


