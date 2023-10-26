# CreatePortfolioGroupRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** | The code that the portfolio group will be created with. Together with the scope this uniquely identifies the portfolio group. | 
**created** | **datetime** | The effective datetime at which the portfolio group was created. Defaults to the current LUSID system datetime if not specified. | [optional] 
**values** | [**List[ResourceId]**](ResourceId.md) | The resource identifiers of the portfolios to be contained within the portfolio group. | [optional] 
**sub_groups** | [**List[ResourceId]**](ResourceId.md) | The resource identifiers of the portfolio groups to be contained within the portfolio group as sub groups. | [optional] 
**properties** | [**Dict[str, ModelProperty]**](ModelProperty.md) | A set of unique group properties to add to the portfolio group. Each property must be from the &#39;PortfolioGroup&#39; domain and should be identified by its key which has the format {domain}/{scope}/{code}, e.g. &#39;PortfolioGroup/Manager/Id&#39;. These properties must be pre-defined. | [optional] 
**display_name** | **str** | The name of the portfolio group. | 
**description** | **str** | A long form description of the portfolio group. | [optional] 

## Example

```python
from lusid.models.create_portfolio_group_request import CreatePortfolioGroupRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreatePortfolioGroupRequest from a JSON string
create_portfolio_group_request_instance = CreatePortfolioGroupRequest.from_json(json)
# print the JSON string representation of the object
print CreatePortfolioGroupRequest.to_json()

# convert the object into a dict
create_portfolio_group_request_dict = create_portfolio_group_request_instance.to_dict()
# create an instance of CreatePortfolioGroupRequest from a dict
create_portfolio_group_request_form_dict = create_portfolio_group_request.from_dict(create_portfolio_group_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


