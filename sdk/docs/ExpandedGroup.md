# ExpandedGroup


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**href** | **str** | The specific Uniform Resource Identifier (URI) for this resource at the requested effective and asAt datetime. | [optional] 
**id** | [**ResourceId**](ResourceId.md) |  | 
**display_name** | **str** | The name of the portfolio group. | 
**description** | **str** | The long form description of the portfolio group. | [optional] 
**values** | [**List[CompletePortfolio]**](CompletePortfolio.md) | The collection of resource identifiers for the portfolios contained in the portfolio group. | [optional] 
**sub_groups** | [**List[ExpandedGroup]**](ExpandedGroup.md) | The collection of resource identifiers for the portfolio groups contained in the portfolio group as sub groups. | [optional] 
**version** | [**Version**](Version.md) |  | [optional] 
**links** | [**List[Link]**](Link.md) |  | [optional] 

## Example

```python
from lusid.models.expanded_group import ExpandedGroup

# TODO update the JSON string below
json = "{}"
# create an instance of ExpandedGroup from a JSON string
expanded_group_instance = ExpandedGroup.from_json(json)
# print the JSON string representation of the object
print ExpandedGroup.to_json()

# convert the object into a dict
expanded_group_dict = expanded_group_instance.to_dict()
# create an instance of ExpandedGroup from a dict
expanded_group_form_dict = expanded_group.from_dict(expanded_group_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


