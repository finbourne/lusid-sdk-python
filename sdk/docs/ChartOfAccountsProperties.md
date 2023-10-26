# ChartOfAccountsProperties


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**href** | **str** | The specific Uniform Resource Identifier (URI) for this resource at the requested effective and asAt datetime. | [optional] 
**properties** | [**Dict[str, ModelProperty]**](ModelProperty.md) | The Chart of Accounts properties. These will be from the &#39;ChartOfAccounts&#39; domain. | [optional] 
**version** | [**Version**](Version.md) |  | [optional] 
**links** | [**List[Link]**](Link.md) |  | [optional] 

## Example

```python
from lusid.models.chart_of_accounts_properties import ChartOfAccountsProperties

# TODO update the JSON string below
json = "{}"
# create an instance of ChartOfAccountsProperties from a JSON string
chart_of_accounts_properties_instance = ChartOfAccountsProperties.from_json(json)
# print the JSON string representation of the object
print ChartOfAccountsProperties.to_json()

# convert the object into a dict
chart_of_accounts_properties_dict = chart_of_accounts_properties_instance.to_dict()
# create an instance of ChartOfAccountsProperties from a dict
chart_of_accounts_properties_form_dict = chart_of_accounts_properties.from_dict(chart_of_accounts_properties_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


