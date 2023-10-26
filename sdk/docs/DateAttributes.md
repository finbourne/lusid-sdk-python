# DateAttributes


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**irregular** | **bool** |  | 
**irregular_session** | **bool** |  | 
**new_hours** | **bool** |  | 
**activity** | **str** |  | [optional] 
**first_open** | **str** |  | [optional] 
**last_open** | **str** |  | [optional] 
**first_close** | **str** |  | [optional] 
**last_close** | **str** |  | [optional] 

## Example

```python
from lusid.models.date_attributes import DateAttributes

# TODO update the JSON string below
json = "{}"
# create an instance of DateAttributes from a JSON string
date_attributes_instance = DateAttributes.from_json(json)
# print the JSON string representation of the object
print DateAttributes.to_json()

# convert the object into a dict
date_attributes_dict = date_attributes_instance.to_dict()
# create an instance of DateAttributes from a dict
date_attributes_form_dict = date_attributes.from_dict(date_attributes_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


