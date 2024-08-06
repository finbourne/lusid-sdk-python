# PagedResourceListOfChartOfAccounts


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**next_page** | **str** |  | [optional] 
**previous_page** | **str** |  | [optional] 
**values** | [**List[ChartOfAccounts]**](ChartOfAccounts.md) |  | 
**href** | **str** |  | [optional] 
**links** | [**List[Link]**](Link.md) |  | [optional] 

## Example

```python
from lusid.models.paged_resource_list_of_chart_of_accounts import PagedResourceListOfChartOfAccounts

# TODO update the JSON string below
json = "{}"
# create an instance of PagedResourceListOfChartOfAccounts from a JSON string
paged_resource_list_of_chart_of_accounts_instance = PagedResourceListOfChartOfAccounts.from_json(json)
# print the JSON string representation of the object
print PagedResourceListOfChartOfAccounts.to_json()

# convert the object into a dict
paged_resource_list_of_chart_of_accounts_dict = paged_resource_list_of_chart_of_accounts_instance.to_dict()
# create an instance of PagedResourceListOfChartOfAccounts from a dict
paged_resource_list_of_chart_of_accounts_form_dict = paged_resource_list_of_chart_of_accounts.from_dict(paged_resource_list_of_chart_of_accounts_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


