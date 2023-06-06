# ResourceListOfParticipation


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**values** | [**List[Participation]**](Participation.md) |  | 
**href** | **str** |  | [optional] 
**links** | [**List[Link]**](Link.md) |  | [optional] 
**next_page** | **str** |  | [optional] 
**previous_page** | **str** |  | [optional] 

## Example

```python
from lusid.models.resource_list_of_participation import ResourceListOfParticipation

# TODO update the JSON string below
json = "{}"
# create an instance of ResourceListOfParticipation from a JSON string
resource_list_of_participation_instance = ResourceListOfParticipation.from_json(json)
# print the JSON string representation of the object
print ResourceListOfParticipation.to_json()

# convert the object into a dict
resource_list_of_participation_dict = resource_list_of_participation_instance.to_dict()
# create an instance of ResourceListOfParticipation from a dict
resource_list_of_participation_form_dict = resource_list_of_participation.from_dict(resource_list_of_participation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


