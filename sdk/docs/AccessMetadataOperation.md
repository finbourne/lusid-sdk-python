# AccessMetadataOperation


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[AccessMetadataValue]**](AccessMetadataValue.md) |  | 
**path** | **str** |  | 
**op** | **str** | The available values are: add, remove | 
**var_from** | **str** |  | [optional] 

## Example

```python
from lusid.models.access_metadata_operation import AccessMetadataOperation

# TODO update the JSON string below
json = "{}"
# create an instance of AccessMetadataOperation from a JSON string
access_metadata_operation_instance = AccessMetadataOperation.from_json(json)
# print the JSON string representation of the object
print AccessMetadataOperation.to_json()

# convert the object into a dict
access_metadata_operation_dict = access_metadata_operation_instance.to_dict()
# create an instance of AccessMetadataOperation from a dict
access_metadata_operation_form_dict = access_metadata_operation.from_dict(access_metadata_operation_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


