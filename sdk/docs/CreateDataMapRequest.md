# CreateDataMapRequest

Request to create a new data map

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | [**DataMapKey**](DataMapKey.md) |  | 
**data** | [**DataMapping**](DataMapping.md) |  | [optional] 

## Example

```python
from lusid.models.create_data_map_request import CreateDataMapRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateDataMapRequest from a JSON string
create_data_map_request_instance = CreateDataMapRequest.from_json(json)
# print the JSON string representation of the object
print CreateDataMapRequest.to_json()

# convert the object into a dict
create_data_map_request_dict = create_data_map_request_instance.to_dict()
# create an instance of CreateDataMapRequest from a dict
create_data_map_request_form_dict = create_data_map_request.from_dict(create_data_map_request_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


