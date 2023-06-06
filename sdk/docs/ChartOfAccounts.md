# ChartOfAccounts

A chart of account.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**href** | **str** | The specific Uniform Resource Identifier (URI) for this resource at the requested effective and asAt datetime. | [optional] 
**id** | [**ResourceId**](ResourceId.md) |  | 
**name** | **str** | The given name for the chart of account. | [optional] 
**description** | **str** | The description for the chart of account. | [optional] 
**properties** | [**Dict[str, ModelProperty]**](ModelProperty.md) | Chart of Accounts properties to add to the chart of account. | [optional] 
**version** | [**Version**](Version.md) |  | [optional] 
**links** | [**List[Link]**](Link.md) |  | [optional] 

## Example

```python
from lusid.models.chart_of_accounts import ChartOfAccounts

# TODO update the JSON string below
json = "{}"
# create an instance of ChartOfAccounts from a JSON string
chart_of_accounts_instance = ChartOfAccounts.from_json(json)
# print the JSON string representation of the object
print ChartOfAccounts.to_json()

# convert the object into a dict
chart_of_accounts_dict = chart_of_accounts_instance.to_dict()
# create an instance of ChartOfAccounts from a dict
chart_of_accounts_form_dict = chart_of_accounts.from_dict(chart_of_accounts_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


