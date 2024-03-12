# PagedResourceListOfFund


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**next_page** | **str** |  | [optional] 
**previous_page** | **str** |  | [optional] 
**values** | [**List[Fund]**](Fund.md) |  | 
**href** | **str** |  | [optional] 
**links** | [**List[Link]**](Link.md) |  | [optional] 

## Example

```python
from lusid.models.paged_resource_list_of_fund import PagedResourceListOfFund

# TODO update the JSON string below
json = "{}"
# create an instance of PagedResourceListOfFund from a JSON string
paged_resource_list_of_fund_instance = PagedResourceListOfFund.from_json(json)
# print the JSON string representation of the object
print PagedResourceListOfFund.to_json()

# convert the object into a dict
paged_resource_list_of_fund_dict = paged_resource_list_of_fund_instance.to_dict()
# create an instance of PagedResourceListOfFund from a dict
paged_resource_list_of_fund_form_dict = paged_resource_list_of_fund.from_dict(paged_resource_list_of_fund_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


