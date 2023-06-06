# CreateDerivedTransactionPortfolioRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**display_name** | **str** | The name of the derived transaction portfolio. | 
**description** | **str** | A description for the derived transaction portfolio. | [optional] 
**code** | **str** | The code of the derived transaction portfolio. Together with the scope this uniquely identifies the derived transaction portfolio. | 
**parent_portfolio_id** | [**ResourceId**](ResourceId.md) |  | 
**created** | **datetime** | This will be auto-populated to be the parent portfolio creation date. | [optional] 
**corporate_action_source_id** | [**ResourceId**](ResourceId.md) |  | [optional] 
**accounting_method** | **str** | . The available values are: Default, AverageCost, FirstInFirstOut, LastInFirstOut, HighestCostFirst, LowestCostFirst | [optional] 
**sub_holding_keys** | **List[str]** | A set of unique transaction properties to group the derived transaction portfolio&#39;s holdings by, perhaps for strategy tagging. Each property must be from the &#39;Transaction&#39; domain and identified by a key in the format {domain}/{scope}/{code}, for example &#39;Transaction/strategies/quantsignal&#39;. See https://support.lusid.com/knowledgebase/article/KA-01879/en-us for more information. | [optional] 
**instrument_scopes** | **List[str]** | The resolution strategy used to resolve instruments of transactions/holdings upserted to this derived portfolio. | [optional] 
**amortisation_method** | **str** | The amortisation method the portfolio is using in the calculation. This can be &#39;NoAmortisation&#39;, &#39;StraightLine&#39; or &#39;EffectiveYield&#39;. | [optional] 
**transaction_type_scope** | **str** | The scope of the transaction types. | [optional] 

## Example

```python
from lusid.models.create_derived_transaction_portfolio_request import CreateDerivedTransactionPortfolioRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateDerivedTransactionPortfolioRequest from a JSON string
create_derived_transaction_portfolio_request_instance = CreateDerivedTransactionPortfolioRequest.from_json(json)
# print the JSON string representation of the object
print CreateDerivedTransactionPortfolioRequest.to_json()

# convert the object into a dict
create_derived_transaction_portfolio_request_dict = create_derived_transaction_portfolio_request_instance.to_dict()
# create an instance of CreateDerivedTransactionPortfolioRequest from a dict
create_derived_transaction_portfolio_request_form_dict = create_derived_transaction_portfolio_request.from_dict(create_derived_transaction_portfolio_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


