# CustodianAccount


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**custodian_account_id** | [**ResourceId**](ResourceId.md) |  | 
**status** | **str** | The account status. Can be Active, Inactive or Deleted. Defaults to Active. | 
**account_number** | **str** | The Custodian Account Number | 
**account_name** | **str** | The identifiable name given to the Custodian Account | 
**accounting_method** | **str** | The Accounting method to be used | 
**currency** | **str** | The Currency for the Account | 
**account_type** | **str** | The Type of the Custodian Account. Can be Margin, Cash or Swap. Defaults to Margin. | 
**properties** | [**dict(str, ModelProperty)**](ModelProperty.md) | Set of unique Custodian Account properties and associated values to store with the Custodian Account. Each property must be from the &#39;CustodianAccount&#39; domain. | [optional] 
**custodian** | [**LegalEntity**](LegalEntity.md) |  | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


