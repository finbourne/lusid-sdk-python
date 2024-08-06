# ResourceListOfIUnitDefinitionDto


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**values** | [**List[IUnitDefinitionDto]**](IUnitDefinitionDto.md) |  | 
**href** | **str** |  | [optional] 
**links** | [**List[Link]**](Link.md) |  | [optional] 
**next_page** | **str** |  | [optional] 
**previous_page** | **str** |  | [optional] 

## Example

```python
from lusid.models.resource_list_of_i_unit_definition_dto import ResourceListOfIUnitDefinitionDto

# TODO update the JSON string below
json = "{}"
# create an instance of ResourceListOfIUnitDefinitionDto from a JSON string
resource_list_of_i_unit_definition_dto_instance = ResourceListOfIUnitDefinitionDto.from_json(json)
# print the JSON string representation of the object
print ResourceListOfIUnitDefinitionDto.to_json()

# convert the object into a dict
resource_list_of_i_unit_definition_dto_dict = resource_list_of_i_unit_definition_dto_instance.to_dict()
# create an instance of ResourceListOfIUnitDefinitionDto from a dict
resource_list_of_i_unit_definition_dto_form_dict = resource_list_of_i_unit_definition_dto.from_dict(resource_list_of_i_unit_definition_dto_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


