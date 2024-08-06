# CreateDateRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**date_id** | **str** |  | 
**from_utc** | **datetime** |  | 
**to_utc** | **datetime** |  | 
**time_zone** | **str** |  | 
**description** | **str** |  | 
**type** | **str** |  | [optional] 
**attributes** | [**DateAttributes**](DateAttributes.md) |  | [optional] 
**source_data** | **Dict[str, str]** |  | [optional] 

## Example

```python
from lusid.models.create_date_request import CreateDateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateDateRequest from a JSON string
create_date_request_instance = CreateDateRequest.from_json(json)
# print the JSON string representation of the object
print CreateDateRequest.to_json()

# convert the object into a dict
create_date_request_dict = create_date_request_instance.to_dict()
# create an instance of CreateDateRequest from a dict
create_date_request_form_dict = create_date_request.from_dict(create_date_request_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


