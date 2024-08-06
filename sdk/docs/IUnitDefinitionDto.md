# IUnitDefinitionDto


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_schema** | **str** | The available values are: NoUnits, Basic, Iso4217Currency | [optional] 
**code** | **str** |  | [optional] [readonly] 
**display_name** | **str** |  | [optional] [readonly] 
**description** | **str** |  | [optional] [readonly] 

## Example

```python
from lusid.models.i_unit_definition_dto import IUnitDefinitionDto

# TODO update the JSON string below
json = "{}"
# create an instance of IUnitDefinitionDto from a JSON string
i_unit_definition_dto_instance = IUnitDefinitionDto.from_json(json)
# print the JSON string representation of the object
print IUnitDefinitionDto.to_json()

# convert the object into a dict
i_unit_definition_dto_dict = i_unit_definition_dto_instance.to_dict()
# create an instance of IUnitDefinitionDto from a dict
i_unit_definition_dto_form_dict = i_unit_definition_dto.from_dict(i_unit_definition_dto_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


