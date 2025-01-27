# UpsertCustomDataModelRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**display_name** | **str** | The name of the Custom Data Model. | 
**description** | **str** | A description for the Custom Data Model. | 
**parent_data_model** | [**ResourceId**](ResourceId.md) |  | [optional] 
**conditions** | **str** | The conditions that the bound entity must meet to be valid. | [optional] 
**properties** | [**List[CustomDataModelPropertySpecification]**](CustomDataModelPropertySpecification.md) | The properties that are required or allowed on the bound entity. | [optional] 
**identifier_types** | [**List[CustomDataModelIdentifierTypeSpecification]**](CustomDataModelIdentifierTypeSpecification.md) | The identifier types that are required or allowed on the bound entity. | [optional] 
**attribute_aliases** | [**List[Alias]**](Alias.md) | The aliases for property keys, identifier types, and fields on the bound entity. | [optional] 
**recommended_sort_by** | [**List[RecommendedSortBy]**](RecommendedSortBy.md) | The preferred default sorting instructions. | [optional] 

## Example

```python
from lusid.models.upsert_custom_data_model_request import UpsertCustomDataModelRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpsertCustomDataModelRequest from a JSON string
upsert_custom_data_model_request_instance = UpsertCustomDataModelRequest.from_json(json)
# print the JSON string representation of the object
print UpsertCustomDataModelRequest.to_json()

# convert the object into a dict
upsert_custom_data_model_request_dict = upsert_custom_data_model_request_instance.to_dict()
# create an instance of UpsertCustomDataModelRequest from a dict
upsert_custom_data_model_request_form_dict = upsert_custom_data_model_request.from_dict(upsert_custom_data_model_request_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


