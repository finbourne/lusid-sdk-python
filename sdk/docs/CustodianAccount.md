# CustodianAccount


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**custodian_account_id** | [**ResourceId**](ResourceId.md) |  | 
**status** | **str** | The Account status. Can be Active, Inactive or Deleted. | 
**account_number** | **str** | The Custodian Account Number | 
**account_name** | **str** | The identifiable name given to the Custodian Account | 
**accounting_method** | **str** | The Accounting method to be used | 
**currency** | **str** | The Currency for the Account | 
**properties** | [**Dict[str, ModelProperty]**](ModelProperty.md) | Set of unique Custodian Account properties and associated values to store with the Custodian Account. Each property must be from the &#39;CustodianAccount&#39; domain. | [optional] 
**custodian** | [**LegalEntity**](LegalEntity.md) |  | 
**account_type** | **str** | The Type of the Custodian Account. Can be Margin, Cash or Swap. Defaults to Margin. | 

## Example

```python
from lusid.models.custodian_account import CustodianAccount

# TODO update the JSON string below
json = "{}"
# create an instance of CustodianAccount from a JSON string
custodian_account_instance = CustodianAccount.from_json(json)
# print the JSON string representation of the object
print CustodianAccount.to_json()

# convert the object into a dict
custodian_account_dict = custodian_account_instance.to_dict()
# create an instance of CustodianAccount from a dict
custodian_account_form_dict = custodian_account.from_dict(custodian_account_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


