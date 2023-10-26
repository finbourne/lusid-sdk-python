# UpsertLegalEntitiesResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**href** | **str** | The specific Uniform Resource Identifier (URI) for this resource at the requested effective and asAt datetime. | [optional] 
**values** | [**Dict[str, LegalEntity]**](LegalEntity.md) | The legal entities which have been successfully updated or created. | [optional] 
**failed** | [**Dict[str, ErrorDetail]**](ErrorDetail.md) | The legal entities that could not be updated or created or were left unchanged without error along with a reason for their failure. | [optional] 
**links** | [**List[Link]**](Link.md) |  | [optional] 

## Example

```python
from lusid.models.upsert_legal_entities_response import UpsertLegalEntitiesResponse

# TODO update the JSON string below
json = "{}"
# create an instance of UpsertLegalEntitiesResponse from a JSON string
upsert_legal_entities_response_instance = UpsertLegalEntitiesResponse.from_json(json)
# print the JSON string representation of the object
print UpsertLegalEntitiesResponse.to_json()

# convert the object into a dict
upsert_legal_entities_response_dict = upsert_legal_entities_response_instance.to_dict()
# create an instance of UpsertLegalEntitiesResponse from a dict
upsert_legal_entities_response_form_dict = upsert_legal_entities_response.from_dict(upsert_legal_entities_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


