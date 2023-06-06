# CompletePortfolio


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | [**ResourceId**](ResourceId.md) |  | 
**href** | **str** | The specific Uniform Resource Identifier (URI) for this resource at the requested effective and asAt datetime. | [optional] 
**description** | **str** | The long form description of the portfolio. | [optional] 
**display_name** | **str** | The name of the portfolio. | [optional] 
**created** | **datetime** | The effective datetime at which the portfolio was created. No transactions or constituents can be added to the portfolio before this date. | [optional] 
**parent_portfolio_id** | [**ResourceId**](ResourceId.md) |  | [optional] 
**is_derived** | **bool** | Whether or not this is a derived portfolio. | [optional] [readonly] 
**type** | **str** | The type of the portfolio. The available values are: Transaction, Reference, DerivedTransaction | [optional] 
**version** | [**Version**](Version.md) |  | 
**properties** | [**List[ModelProperty]**](ModelProperty.md) | The requested portfolio properties. These will be from the &#39;Portfolio&#39; domain. | [optional] 
**base_currency** | **str** | If the portfolio is a transaction portfolio or derived transaction portfolio, this is the base currency of the portfolio. | [optional] 
**links** | [**List[Link]**](Link.md) |  | [optional] 

## Example

```python
from lusid.models.complete_portfolio import CompletePortfolio

# TODO update the JSON string below
json = "{}"
# create an instance of CompletePortfolio from a JSON string
complete_portfolio_instance = CompletePortfolio.from_json(json)
# print the JSON string representation of the object
print CompletePortfolio.to_json()

# convert the object into a dict
complete_portfolio_dict = complete_portfolio_instance.to_dict()
# create an instance of CompletePortfolio from a dict
complete_portfolio_form_dict = complete_portfolio.from_dict(complete_portfolio_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


