# CorporateActionSource

A corporate action source

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**href** | **str** | The specific Uniform Resource Identifier (URI) for this resource at the requested effective and asAt datetime. | [optional] 
**id** | [**ResourceId**](ResourceId.md) |  | [optional] 
**version** | [**Version**](Version.md) |  | [optional] 
**display_name** | **str** | The name of the corporate action source | [optional] 
**description** | **str** | The description of the corporate action source | [optional] 
**instrument_scopes** | **List[str]** | The list of instrument scopes used as the scope resolution strategy when resolving instruments of upserted corporate actions. | [optional] 
**links** | [**List[Link]**](Link.md) |  | [optional] 

## Example

```python
from lusid.models.corporate_action_source import CorporateActionSource

# TODO update the JSON string below
json = "{}"
# create an instance of CorporateActionSource from a JSON string
corporate_action_source_instance = CorporateActionSource.from_json(json)
# print the JSON string representation of the object
print CorporateActionSource.to_json()

# convert the object into a dict
corporate_action_source_dict = corporate_action_source_instance.to_dict()
# create an instance of CorporateActionSource from a dict
corporate_action_source_form_dict = corporate_action_source.from_dict(corporate_action_source_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


