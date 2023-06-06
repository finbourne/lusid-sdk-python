# UpdateDataTypeRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**display_name** | **str** | The display name of the data type. | [optional] 
**description** | **str** | The description of the data type. | [optional] 
**acceptable_values** | **List[str]** | The acceptable set of values for this data type. Only applies to &#39;open&#39; value type range. | [optional] 
**acceptable_units** | [**List[UpdateUnitRequest]**](UpdateUnitRequest.md) | The definitions of the acceptable units. | [optional] 

## Example

```python
from lusid.models.update_data_type_request import UpdateDataTypeRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateDataTypeRequest from a JSON string
update_data_type_request_instance = UpdateDataTypeRequest.from_json(json)
# print the JSON string representation of the object
print UpdateDataTypeRequest.to_json()

# convert the object into a dict
update_data_type_request_dict = update_data_type_request_instance.to_dict()
# create an instance of UpdateDataTypeRequest from a dict
update_data_type_request_form_dict = update_data_type_request.from_dict(update_data_type_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


