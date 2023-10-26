# ChartOfAccountsRequest

The request used to create a chart of account.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** | The code given for the Chart of Accounts. | 
**display_name** | **str** | The name of the Chart of Account. | [optional] 
**description** | **str** | A description of the Chart of Accounts. | [optional] 
**properties** | [**Dict[str, ModelProperty]**](ModelProperty.md) | A set of properties for the Chart of Accounts. | [optional] 

## Example

```python
from lusid.models.chart_of_accounts_request import ChartOfAccountsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ChartOfAccountsRequest from a JSON string
chart_of_accounts_request_instance = ChartOfAccountsRequest.from_json(json)
# print the JSON string representation of the object
print ChartOfAccountsRequest.to_json()

# convert the object into a dict
chart_of_accounts_request_dict = chart_of_accounts_request_instance.to_dict()
# create an instance of ChartOfAccountsRequest from a dict
chart_of_accounts_request_form_dict = chart_of_accounts_request.from_dict(chart_of_accounts_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


