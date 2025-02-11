# DataModelMembership


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**membership** | [**List[Membership]**](Membership.md) | The collection of data models this entity is a member of. | 
**current_model** | [**MembershipAndStatus**](MembershipAndStatus.md) |  | [optional] 

## Example

```python
from lusid.models.data_model_membership import DataModelMembership

# TODO update the JSON string below
json = "{}"
# create an instance of DataModelMembership from a JSON string
data_model_membership_instance = DataModelMembership.from_json(json)
# print the JSON string representation of the object
print DataModelMembership.to_json()

# convert the object into a dict
data_model_membership_dict = data_model_membership_instance.to_dict()
# create an instance of DataModelMembership from a dict
data_model_membership_form_dict = data_model_membership.from_dict(data_model_membership_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


