# PagedResourceListOfValuationPointOverview


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**next_page** | **str** |  | [optional] 
**previous_page** | **str** |  | [optional] 
**values** | [**List[ValuationPointOverview]**](ValuationPointOverview.md) |  | 
**href** | **str** |  | [optional] 
**links** | [**List[Link]**](Link.md) |  | [optional] 

## Example

```python
from lusid.models.paged_resource_list_of_valuation_point_overview import PagedResourceListOfValuationPointOverview

# TODO update the JSON string below
json = "{}"
# create an instance of PagedResourceListOfValuationPointOverview from a JSON string
paged_resource_list_of_valuation_point_overview_instance = PagedResourceListOfValuationPointOverview.from_json(json)
# print the JSON string representation of the object
print PagedResourceListOfValuationPointOverview.to_json()

# convert the object into a dict
paged_resource_list_of_valuation_point_overview_dict = paged_resource_list_of_valuation_point_overview_instance.to_dict()
# create an instance of PagedResourceListOfValuationPointOverview from a dict
paged_resource_list_of_valuation_point_overview_form_dict = paged_resource_list_of_valuation_point_overview.from_dict(paged_resource_list_of_valuation_point_overview_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


