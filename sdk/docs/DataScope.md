# DataScope


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**client** | [**Client**](Client.md) |  | [optional] 
**scope** | **str** |  | [optional] 

## Example

```python
from lusid.models.data_scope import DataScope

# TODO update the JSON string below
json = "{}"
# create an instance of DataScope from a JSON string
data_scope_instance = DataScope.from_json(json)
# print the JSON string representation of the object
print DataScope.to_json()

# convert the object into a dict
data_scope_dict = data_scope_instance.to_dict()
# create an instance of DataScope from a dict
data_scope_form_dict = data_scope.from_dict(data_scope_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


