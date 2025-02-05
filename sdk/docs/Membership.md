# Membership


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**scope** | **str** | The scope of the unique identifier associated with the Custom Data Model. | 
**code** | **str** | The code of the unique identifier associated with the Custom Data Model. | 
**display_name** | **str** | The name of the Custom Data Model. | 

## Example

```python
from lusid.models.membership import Membership

# TODO update the JSON string below
json = "{}"
# create an instance of Membership from a JSON string
membership_instance = Membership.from_json(json)
# print the JSON string representation of the object
print Membership.to_json()

# convert the object into a dict
membership_dict = membership_instance.to_dict()
# create an instance of Membership from a dict
membership_form_dict = membership.from_dict(membership_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


