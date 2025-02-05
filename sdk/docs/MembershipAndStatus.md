# MembershipAndStatus


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** | Describes whether the entity is still a valid member of the data model. | 
**scope** | **str** | The scope of the unique identifier associated with the Custom Data Model. | 
**code** | **str** | The code of the unique identifier associated with the Custom Data Model. | 
**display_name** | **str** | The name of the Custom Data Model. | 

## Example

```python
from lusid.models.membership_and_status import MembershipAndStatus

# TODO update the JSON string below
json = "{}"
# create an instance of MembershipAndStatus from a JSON string
membership_and_status_instance = MembershipAndStatus.from_json(json)
# print the JSON string representation of the object
print MembershipAndStatus.to_json()

# convert the object into a dict
membership_and_status_dict = membership_and_status_instance.to_dict()
# create an instance of MembershipAndStatus from a dict
membership_and_status_form_dict = membership_and_status.from_dict(membership_and_status_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


