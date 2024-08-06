# VersionedResourceListOfTrialBalance


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**version** | [**Version**](Version.md) |  | 
**values** | [**List[TrialBalance]**](TrialBalance.md) |  | 
**href** | **str** |  | [optional] 
**next_page** | **str** |  | [optional] 
**previous_page** | **str** |  | [optional] 
**links** | [**List[Link]**](Link.md) |  | [optional] 

## Example

```python
from lusid.models.versioned_resource_list_of_trial_balance import VersionedResourceListOfTrialBalance

# TODO update the JSON string below
json = "{}"
# create an instance of VersionedResourceListOfTrialBalance from a JSON string
versioned_resource_list_of_trial_balance_instance = VersionedResourceListOfTrialBalance.from_json(json)
# print the JSON string representation of the object
print VersionedResourceListOfTrialBalance.to_json()

# convert the object into a dict
versioned_resource_list_of_trial_balance_dict = versioned_resource_list_of_trial_balance_instance.to_dict()
# create an instance of VersionedResourceListOfTrialBalance from a dict
versioned_resource_list_of_trial_balance_form_dict = versioned_resource_list_of_trial_balance.from_dict(versioned_resource_list_of_trial_balance_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


