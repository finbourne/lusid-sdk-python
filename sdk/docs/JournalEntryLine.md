# JournalEntryLine

A Journal Entry line entity.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accounting_date** | **datetime** | The Journal Entry Line accounting date. | 
**activity_date** | **datetime** | The actual date of the activity. Differs from the accounting date when creating journals that would occur in a closed period. | 
**portfolio_id** | [**ResourceId**](ResourceId.md) |  | 
**instrument_id** | **str** | To indicate the instrument of the transaction that the Journal Entry Line posted for, if applicable. | 
**instrument_scope** | **str** | The scope in which the Journal Entry Line instrument is in. | 
**sub_holding_keys** | [**Dict[str, PerpetualProperty]**](PerpetualProperty.md) | The sub-holding properties which are part of the AccountingKey. | [optional] 
**tax_lot_id** | **str** | If the holding type is &#39;B&#39; (settled cash balance), this is 1. Otherwise, this is the ID of a tax lot if applicable, or the source ID of the original transaction if not. | [optional] 
**general_ledger_account_code** | **str** | The code of the account in the general ledger the Journal Entry was posted to. | 
**local** | [**CurrencyAndAmount**](CurrencyAndAmount.md) |  | 
**base** | [**CurrencyAndAmount**](CurrencyAndAmount.md) |  | 
**units** | **float** | Units held for the Journal Entry Line. | 
**posting_module_code** | **str** | The code of the posting module where the posting rules derived the Journal Entry lines. | [optional] 
**posting_rule** | **str** | The rule generating the Journal Entry Line. | 
**as_at_date** | **datetime** | The corresponding input date and time of the Transaction generating the Journal Entry Line. | 
**activities_description** | **str** | This would be the description of the business activities this Journal Entry Line is for. | [optional] 
**source_type** | **str** | So far are 4 types: LusidTxn, LusidValuation, Manual and External. | 
**source_id** | **str** | For the Lusid Source Type this will be the txn Id. For the rest will be what the user populates. | 
**properties** | [**Dict[str, ModelProperty]**](ModelProperty.md) | A set of properties for the Abor. | [optional] 
**movement_name** | **str** | If the JE Line is generated from a transaction, the name of the side in the transaction type&#39;s movement. If from a valuation, this is &#39;MarkToMarket&#39;. | [optional] 
**holding_type** | **str** | One of the LUSID holding types such as &#39;P&#39; for position or &#39;B&#39; for settled cash balance. | 
**economic_bucket** | **str** | LUSID automatically categorises a JE Line into a broad economic bucket such as &#39;NA_Cost&#39; or &#39;PL_RealPriceGL&#39;. | 
**economic_bucket_component** | **str** | Sub bucket of the economic bucket. | [optional] 
**economic_bucket_variant** | **str** | Categorisation of a Mark-to-market journal entry line into LongTerm or ShortTerm based on whether the ActivityDate is more than a year after the purchase trade date or not. | [optional] 
**levels** | **List[str]** | Resolved data from the general ledger profile where the GeneralLedgerProfileCode is specified in the GetJournalEntryLines request body. | [optional] 
**source_levels** | **List[str]** | Source data from the general ledger profile where the GeneralLedgerProfileCode is specified in the GetJournalEntryLines request body. | [optional] 
**movement_sign** | **str** | Indicates if the Journal Entry Line corresponds to a Long or Short movement. | [optional] 
**holding_sign** | **str** | Indicates if the Journal Entry Line is operating against a Long or Short holding. | [optional] 
**ledger_column** | **str** | Indicates if the Journal Entry Line is credit or debit. | [optional] 
**journal_entry_line_type** | **str** | Indicates the Journal Entry Line type | [optional] 
**links** | [**List[Link]**](Link.md) |  | [optional] 

## Example

```python
from lusid.models.journal_entry_line import JournalEntryLine

# TODO update the JSON string below
json = "{}"
# create an instance of JournalEntryLine from a JSON string
journal_entry_line_instance = JournalEntryLine.from_json(json)
# print the JSON string representation of the object
print JournalEntryLine.to_json()

# convert the object into a dict
journal_entry_line_dict = journal_entry_line_instance.to_dict()
# create an instance of JournalEntryLine from a dict
journal_entry_line_form_dict = journal_entry_line.from_dict(journal_entry_line_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


