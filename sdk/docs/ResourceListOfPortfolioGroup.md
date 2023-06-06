# ResourceListOfPortfolioGroup


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**values** | [**List[PortfolioGroup]**](PortfolioGroup.md) |  | 
**href** | **str** |  | [optional] 
**links** | [**List[Link]**](Link.md) |  | [optional] 
**next_page** | **str** |  | [optional] 
**previous_page** | **str** |  | [optional] 

## Example

```python
from lusid.models.resource_list_of_portfolio_group import ResourceListOfPortfolioGroup

# TODO update the JSON string below
json = "{}"
# create an instance of ResourceListOfPortfolioGroup from a JSON string
resource_list_of_portfolio_group_instance = ResourceListOfPortfolioGroup.from_json(json)
# print the JSON string representation of the object
print ResourceListOfPortfolioGroup.to_json()

# convert the object into a dict
resource_list_of_portfolio_group_dict = resource_list_of_portfolio_group_instance.to_dict()
# create an instance of ResourceListOfPortfolioGroup from a dict
resource_list_of_portfolio_group_form_dict = resource_list_of_portfolio_group.from_dict(resource_list_of_portfolio_group_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


