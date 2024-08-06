# UpdateUnitRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** |  | [optional] 
**display_name** | **str** |  | [optional] 
**description** | **str** |  | [optional] 

## Example

```python
from lusid.models.update_unit_request import UpdateUnitRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateUnitRequest from a JSON string
update_unit_request_instance = UpdateUnitRequest.from_json(json)
# print the JSON string representation of the object
print UpdateUnitRequest.to_json()

# convert the object into a dict
update_unit_request_dict = update_unit_request_instance.to_dict()
# create an instance of UpdateUnitRequest from a dict
update_unit_request_form_dict = update_unit_request.from_dict(update_unit_request_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


