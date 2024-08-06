# Account

An account

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** | The code given for the Account. | 
**description** | **str** | A description for the Account. | [optional] 
**type** | **str** | The Account type. Can have the values: Asset/Liabilities/Income/Expense/Capital/Revenue. | 
**status** | **str** | The Account status. Can be Active, Inactive or Deleted. The available values are: Active, Inactive, Deleted | 
**control** | **str** | This allows users to specify whether this a protected Account that prevents direct manual journal adjustment. Can have the values: System/ManualIt will default to “Manual”. | [optional] 
**properties** | [**Dict[str, ModelProperty]**](ModelProperty.md) | A set of properties for the Account. | [optional] 

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
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


