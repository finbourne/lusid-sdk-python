# Account

An account

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** | The code given for the account. | 
**description** | **str** | The description for the account. | [optional] 
**type** | **str** | The account type. Can have the values: Asset/Liabilities/Income/Expense/Capital/Revenue. | 
**status** | **str** | The account status. Can be Active, Inactive or Deleted. Defaults to Active. The available values are: Active, Inactive, Deleted | 
**control** | **str** | This allows users to specify whether this a protected account that prevents direct manual journal adjustment. Can have the values: System/ManualIt will default to “Manual”. | 
**properties** | [**Dict[str, ModelProperty]**](ModelProperty.md) | Account properties to add to the account. | [optional] 

## Example

```python
from lusid.models.account import Account

# TODO update the JSON string below
json = "{}"
# create an instance of Account from a JSON string
account_instance = Account.from_json(json)
# print the JSON string representation of the object
print Account.to_json()

# convert the object into a dict
account_dict = account_instance.to_dict()
# create an instance of Account from a dict
account_form_dict = account.from_dict(account_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


