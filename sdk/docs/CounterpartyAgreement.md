# CounterpartyAgreement

Represents the legal agreement between two parties engaged in an OTC transaction.  A typical example would be a 2002 ISDA Master Agreement, signed by two legal entities on a given date.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**display_name** | **str** | A user-defined display label for the Counterparty Agreement. | 
**agreement_type** | **str** | A user-defined field to capture the type of agreement this represents. Examples might be \&quot;ISDA 2002 Master Agreement\&quot; or \&quot;ISDA 1992 Master Agreement\&quot;. | 
**counterparty_signatory** | [**CounterpartySignatory**](CounterpartySignatory.md) |  | 
**dated_as_of** | **datetime** | The date on which the CounterpartyAgreement was signed by both parties. | 
**credit_support_annex_id** | [**ResourceId**](ResourceId.md) |  | 
**id** | [**ResourceId**](ResourceId.md) |  | 

## Example

```python
from lusid.models.counterparty_agreement import CounterpartyAgreement

# TODO update the JSON string below
json = "{}"
# create an instance of CounterpartyAgreement from a JSON string
counterparty_agreement_instance = CounterpartyAgreement.from_json(json)
# print the JSON string representation of the object
print CounterpartyAgreement.to_json()

# convert the object into a dict
counterparty_agreement_dict = counterparty_agreement_instance.to_dict()
# create an instance of CounterpartyAgreement from a dict
counterparty_agreement_form_dict = counterparty_agreement.from_dict(counterparty_agreement_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


