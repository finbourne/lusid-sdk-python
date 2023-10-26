# ErrorDetail


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The id of the failed item that this error relates to. | [optional] 
**type** | **str** | The type of failure that occurred. | [optional] 
**detail** | **str** | Description of the failure that occurred. | [optional] 
**error_details** | **List[Dict[str, str]]** | Information about the particular instance of the failure (supplied information depends on the type of failure). | [optional] 

## Example

```python
from lusid.models.error_detail import ErrorDetail

# TODO update the JSON string below
json = "{}"
# create an instance of ErrorDetail from a JSON string
error_detail_instance = ErrorDetail.from_json(json)
# print the JSON string representation of the object
print ErrorDetail.to_json()

# convert the object into a dict
error_detail_dict = error_detail_instance.to_dict()
# create an instance of ErrorDetail from a dict
error_detail_form_dict = error_detail.from_dict(error_detail_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


