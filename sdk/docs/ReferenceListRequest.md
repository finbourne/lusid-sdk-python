# ReferenceListRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | [**ResourceId**](ResourceId.md) |  | 
**name** | **str** | The name of the reference list. | 
**description** | **str** | The description of the reference list. | [optional] 
**tags** | **List[str]** | The tags associated with the reference list. | [optional] 
**reference_list** | [**ReferenceList**](ReferenceList.md) |  | 

## Example

```python
from lusid.models.reference_list_request import ReferenceListRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ReferenceListRequest from a JSON string
reference_list_request_instance = ReferenceListRequest.from_json(json)
# print the JSON string representation of the object
print ReferenceListRequest.to_json()

# convert the object into a dict
reference_list_request_dict = reference_list_request_instance.to_dict()
# create an instance of ReferenceListRequest from a dict
reference_list_request_form_dict = reference_list_request.from_dict(reference_list_request_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


