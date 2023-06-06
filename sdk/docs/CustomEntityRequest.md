# CustomEntityRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**display_name** | **str** | A display label for the custom entity. | 
**description** | **str** | A description of the custom entity. | 
**identifiers** | [**List[CustomEntityId]**](CustomEntityId.md) | The identifiers the custom entity will be upserted with. | 
**fields** | [**List[CustomEntityField]**](CustomEntityField.md) | The fields that decorate the custom entity. | [optional] 

## Example

```python
from lusid.models.custom_entity_request import CustomEntityRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CustomEntityRequest from a JSON string
custom_entity_request_instance = CustomEntityRequest.from_json(json)
# print the JSON string representation of the object
print CustomEntityRequest.to_json()

# convert the object into a dict
custom_entity_request_dict = custom_entity_request_instance.to_dict()
# create an instance of CustomEntityRequest from a dict
custom_entity_request_form_dict = custom_entity_request.from_dict(custom_entity_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


