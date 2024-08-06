# ResourceListOfPortfolio


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**values** | [**List[Portfolio]**](Portfolio.md) |  | 
**href** | **str** |  | [optional] 
**links** | [**List[Link]**](Link.md) |  | [optional] 
**next_page** | **str** |  | [optional] 
**previous_page** | **str** |  | [optional] 

## Example

```python
from lusid.models.resource_list_of_portfolio import ResourceListOfPortfolio

# TODO update the JSON string below
json = "{}"
# create an instance of ResourceListOfPortfolio from a JSON string
resource_list_of_portfolio_instance = ResourceListOfPortfolio.from_json(json)
# print the JSON string representation of the object
print ResourceListOfPortfolio.to_json()

# convert the object into a dict
resource_list_of_portfolio_dict = resource_list_of_portfolio_instance.to_dict()
# create an instance of ResourceListOfPortfolio from a dict
resource_list_of_portfolio_form_dict = resource_list_of_portfolio.from_dict(resource_list_of_portfolio_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


