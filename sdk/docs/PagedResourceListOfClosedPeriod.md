# PagedResourceListOfClosedPeriod


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**next_page** | **str** |  | [optional] 
**previous_page** | **str** |  | [optional] 
**values** | [**List[ClosedPeriod]**](ClosedPeriod.md) |  | 
**href** | **str** |  | [optional] 
**links** | [**List[Link]**](Link.md) |  | [optional] 

## Example

```python
from lusid.models.paged_resource_list_of_closed_period import PagedResourceListOfClosedPeriod

# TODO update the JSON string below
json = "{}"
# create an instance of PagedResourceListOfClosedPeriod from a JSON string
paged_resource_list_of_closed_period_instance = PagedResourceListOfClosedPeriod.from_json(json)
# print the JSON string representation of the object
print PagedResourceListOfClosedPeriod.to_json()

# convert the object into a dict
paged_resource_list_of_closed_period_dict = paged_resource_list_of_closed_period_instance.to_dict()
# create an instance of PagedResourceListOfClosedPeriod from a dict
paged_resource_list_of_closed_period_form_dict = paged_resource_list_of_closed_period.from_dict(paged_resource_list_of_closed_period_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

