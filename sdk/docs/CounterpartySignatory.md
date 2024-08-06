# CounterpartySignatory

The counterpartyAgreement is signed by two parties, one of which is implicitly the LUSID user.  The CounterpartySignatory represents the 'other side' of the agreement.  It comprises a name and identifier for a Legal Entity in LUSID.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | A user-defined name or label for the counterparty signatory.  There is no requirement for this to match the \&quot;displayName\&quot; of the legal entity. | 
**legal_entity_identifier** | [**TypedResourceId**](TypedResourceId.md) |  | 

## Example

```python
from lusid.models.counterparty_signatory import CounterpartySignatory

# TODO update the JSON string below
json = "{}"
# create an instance of CounterpartySignatory from a JSON string
counterparty_signatory_instance = CounterpartySignatory.from_json(json)
# print the JSON string representation of the object
print CounterpartySignatory.to_json()

# convert the object into a dict
counterparty_signatory_dict = counterparty_signatory_instance.to_dict()
# create an instance of CounterpartySignatory from a dict
counterparty_signatory_form_dict = counterparty_signatory.from_dict(counterparty_signatory_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


