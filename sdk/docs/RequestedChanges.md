# RequestedChanges


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attribute_count** | **int** | Number of attributes staged change applies to | [optional] 
**attribute_names** | **List[str]** | Names of the attributes the staged change applies to. | [optional] 

## Example

```python
from lusid.models.requested_changes import RequestedChanges

# TODO update the JSON string below
json = "{}"
# create an instance of RequestedChanges from a JSON string
requested_changes_instance = RequestedChanges.from_json(json)
# print the JSON string representation of the object
print RequestedChanges.to_json()

# convert the object into a dict
requested_changes_dict = requested_changes_instance.to_dict()
# create an instance of RequestedChanges from a dict
requested_changes_form_dict = requested_changes.from_dict(requested_changes_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


