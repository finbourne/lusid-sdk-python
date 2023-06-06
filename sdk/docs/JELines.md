# JELines

An JELines entity.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accounting_date** | **datetime** | The JELines accounting date. | 
**activity_date** | **datetime** | The actual date of the activity. Differs from the accounting date when creating journals that would occur in a closed period. | 
**portfolio_id** | [**ResourceId**](ResourceId.md) |  | 
**instrument_id** | **str** | To indicate the instrument of the transaction that the JE line posted for, if applicable. | 
**instrument_scope** | **str** | The scope in which the JELines instrument is in. | 
**sub_holding_keys** | [**Dict[str, PerpetualProperty]**](PerpetualProperty.md) | The sub-holding properties which are part of the AccountingKey. | [optional] 
**tax_lot_id** | **str** | The tax lot Id that JE line is impacting. | 
**gl_code** | **str** | Code of general ledger the JE lines posting to. | 
**local** | [**CurrencyAndAmount**](CurrencyAndAmount.md) |  | 
**base** | [**CurrencyAndAmount**](CurrencyAndAmount.md) |  | 
**posting_module_id** | [**ResourceId**](ResourceId.md) |  | 
**posting_rule** | **str** | The rule generating the JELinse. | 
**as_at_date** | **datetime** | The corresponding input date and time of the Transaction generating the JELine. | 
**activities_description** | **str** | This would be the description of the business activities where these JE lines are posting for. | [optional] 
**source_type** | **str** | So far are 4 types: LusidTxn, LusidValuation, Manual and External. | 
**source_id** | **str** | For the Lusid Source Type this will be the txn Id. For the rest will be what the user populates. | 
**properties** | [**Dict[str, ModelProperty]**](ModelProperty.md) | Properties to add to the Abor. | [optional] 
**movement_name** | **str** | The name of the movement. | 
**holding_type** | **str** | Defines the broad category holding within the portfolio. | 
**economic_bucket** | **str** | Raw JE Line details of the economic bucket for the JE Line. | 
**links** | [**List[Link]**](Link.md) |  | [optional] 

## Example

```python
from lusid.models.je_lines import JELines

# TODO update the JSON string below
json = "{}"
# create an instance of JELines from a JSON string
je_lines_instance = JELines.from_json(json)
# print the JSON string representation of the object
print JELines.to_json()

# convert the object into a dict
je_lines_dict = je_lines_instance.to_dict()
# create an instance of JELines from a dict
je_lines_form_dict = je_lines.from_dict(je_lines_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


