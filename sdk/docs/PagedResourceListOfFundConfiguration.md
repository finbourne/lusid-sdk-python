# PagedResourceListOfFundConfiguration


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**next_page** | **str** |  | [optional] 
**previous_page** | **str** |  | [optional] 
**values** | [**List[FundConfiguration]**](FundConfiguration.md) |  | 
**href** | **str** |  | [optional] 
**links** | [**List[Link]**](Link.md) |  | [optional] 

## Example

```python
from lusid.models.paged_resource_list_of_fund_configuration import PagedResourceListOfFundConfiguration

# TODO update the JSON string below
json = "{}"
# create an instance of PagedResourceListOfFundConfiguration from a JSON string
paged_resource_list_of_fund_configuration_instance = PagedResourceListOfFundConfiguration.from_json(json)
# print the JSON string representation of the object
print PagedResourceListOfFundConfiguration.to_json()

# convert the object into a dict
paged_resource_list_of_fund_configuration_dict = paged_resource_list_of_fund_configuration_instance.to_dict()
# create an instance of PagedResourceListOfFundConfiguration from a dict
paged_resource_list_of_fund_configuration_form_dict = paged_resource_list_of_fund_configuration.from_dict(paged_resource_list_of_fund_configuration_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


