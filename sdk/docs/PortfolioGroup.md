# PortfolioGroup


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**href** | **str** | The specific Uniform Resource Identifier (URI) for this resource at the requested effective and asAt datetime. | [optional] 
**id** | [**ResourceId**](ResourceId.md) |  | 
**display_name** | **str** | The name of the portfolio group. | 
**description** | **str** | The long form description of the portfolio group. | [optional] 
**created** | **datetime** | The effective datetime at which the portfolio group was created. No portfolios or sub groups can be added to the group before this date. | [optional] 
**portfolios** | [**List[ResourceId]**](ResourceId.md) | The collection of resource identifiers for the portfolios contained in the portfolio group. | [optional] 
**sub_groups** | [**List[ResourceId]**](ResourceId.md) | The collection of resource identifiers for the portfolio groups contained in the portfolio group as sub groups. | [optional] 
**relationships** | [**List[Relationship]**](Relationship.md) | A set of relationships associated to the portfolio group. | [optional] 
**version** | [**Version**](Version.md) |  | [optional] 
**links** | [**List[Link]**](Link.md) |  | [optional] 

## Example

```python
from lusid.models.portfolio_group import PortfolioGroup

# TODO update the JSON string below
json = "{}"
# create an instance of PortfolioGroup from a JSON string
portfolio_group_instance = PortfolioGroup.from_json(json)
# print the JSON string representation of the object
print PortfolioGroup.to_json()

# convert the object into a dict
portfolio_group_dict = portfolio_group_instance.to_dict()
# create an instance of PortfolioGroup from a dict
portfolio_group_form_dict = portfolio_group.from_dict(portfolio_group_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


