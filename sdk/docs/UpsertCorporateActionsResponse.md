# UpsertCorporateActionsResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**href** | **str** | The specific Uniform Resource Identifier (URI) for this resource at the requested effective and asAt datetime. | [optional] 
**values** | [**Dict[str, CorporateAction]**](CorporateAction.md) | The corporate actions which have been successfully updated or inserted. | [optional] 
**failed** | [**Dict[str, ErrorDetail]**](ErrorDetail.md) | The corporate actions that could not be updated or inserted along with a reason for their failure. | [optional] 
**links** | [**List[Link]**](Link.md) |  | [optional] 

## Example

```python
from lusid.models.upsert_corporate_actions_response import UpsertCorporateActionsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of UpsertCorporateActionsResponse from a JSON string
upsert_corporate_actions_response_instance = UpsertCorporateActionsResponse.from_json(json)
# print the JSON string representation of the object
print UpsertCorporateActionsResponse.to_json()

# convert the object into a dict
upsert_corporate_actions_response_dict = upsert_corporate_actions_response_instance.to_dict()
# create an instance of UpsertCorporateActionsResponse from a dict
upsert_corporate_actions_response_form_dict = upsert_corporate_actions_response.from_dict(upsert_corporate_actions_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


