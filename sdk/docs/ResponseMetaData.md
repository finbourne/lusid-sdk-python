# ResponseMetaData

Metadata related to an api response

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | The type of meta data information being provided | [optional] 
**description** | **str** | The description of what occured for this specific piece of meta data | [optional] 
**identifier_type** | **str** | The type of the listed identifiers | [optional] 
**identifiers** | **List[str]** | The related identifiers that were impacted by this event | [optional] 

## Example

```python
from lusid.models.response_meta_data import ResponseMetaData

# TODO update the JSON string below
json = "{}"
# create an instance of ResponseMetaData from a JSON string
response_meta_data_instance = ResponseMetaData.from_json(json)
# print the JSON string representation of the object
print ResponseMetaData.to_json()

# convert the object into a dict
response_meta_data_dict = response_meta_data_instance.to_dict()
# create an instance of ResponseMetaData from a dict
response_meta_data_form_dict = response_meta_data.from_dict(response_meta_data_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


