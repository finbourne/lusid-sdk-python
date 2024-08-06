# VersionedResourceListOfHoldingContributor


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**version** | [**Version**](Version.md) |  | 
**values** | [**List[HoldingContributor]**](HoldingContributor.md) |  | 
**href** | **str** |  | [optional] 
**next_page** | **str** |  | [optional] 
**previous_page** | **str** |  | [optional] 
**links** | [**List[Link]**](Link.md) |  | [optional] 

## Example

```python
from lusid.models.versioned_resource_list_of_holding_contributor import VersionedResourceListOfHoldingContributor

# TODO update the JSON string below
json = "{}"
# create an instance of VersionedResourceListOfHoldingContributor from a JSON string
versioned_resource_list_of_holding_contributor_instance = VersionedResourceListOfHoldingContributor.from_json(json)
# print the JSON string representation of the object
print VersionedResourceListOfHoldingContributor.to_json()

# convert the object into a dict
versioned_resource_list_of_holding_contributor_dict = versioned_resource_list_of_holding_contributor_instance.to_dict()
# create an instance of VersionedResourceListOfHoldingContributor from a dict
versioned_resource_list_of_holding_contributor_form_dict = versioned_resource_list_of_holding_contributor.from_dict(versioned_resource_list_of_holding_contributor_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


