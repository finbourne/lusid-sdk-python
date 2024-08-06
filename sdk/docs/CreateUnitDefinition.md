# CreateUnitDefinition


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** |  | 
**display_name** | **str** |  | 
**description** | **str** |  | 
**details** | **Dict[str, str]** |  | [optional] 

## Example

```python
from lusid.models.create_unit_definition import CreateUnitDefinition

# TODO update the JSON string below
json = "{}"
# create an instance of CreateUnitDefinition from a JSON string
create_unit_definition_instance = CreateUnitDefinition.from_json(json)
# print the JSON string representation of the object
print CreateUnitDefinition.to_json()

# convert the object into a dict
create_unit_definition_dict = create_unit_definition_instance.to_dict()
# create an instance of CreateUnitDefinition from a dict
create_unit_definition_form_dict = create_unit_definition.from_dict(create_unit_definition_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


