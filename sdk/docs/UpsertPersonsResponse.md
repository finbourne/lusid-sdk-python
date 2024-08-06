# UpsertPersonsResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**values** | [**Dict[str, Person]**](Person.md) | The Person(s) that have been successfully upserted | 
**failed** | [**Dict[str, ErrorDetail]**](ErrorDetail.md) | The Person(s) that could not be upserted along with a reason for their failure. | 
**as_at_date** | **datetime** | The as-at datetime at which Person(s) were created or updated. | 
**links** | [**List[Link]**](Link.md) |  | [optional] 

## Example

```python
from lusid.models.upsert_persons_response import UpsertPersonsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of UpsertPersonsResponse from a JSON string
upsert_persons_response_instance = UpsertPersonsResponse.from_json(json)
# print the JSON string representation of the object
print UpsertPersonsResponse.to_json()

# convert the object into a dict
upsert_persons_response_dict = upsert_persons_response_instance.to_dict()
# create an instance of UpsertPersonsResponse from a dict
upsert_persons_response_form_dict = upsert_persons_response.from_dict(upsert_persons_response_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


