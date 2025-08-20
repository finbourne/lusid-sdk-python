# CounterpartySignatory

The counterpartyAgreement is signed by two parties, one of which is implicitly the LUSID user. The CounterpartySignatory represents the 'other side' of the agreement. It comprises a name and identifier for a Legal Entity in LUSID.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | A user-defined name or label for the counterparty signatory.  There is no requirement for this to match the \&quot;displayName\&quot; of the legal entity. | 
**legal_entity_identifier** | [**TypedResourceId**](TypedResourceId.md) |  | 
## Example

```python
from lusid.models.counterparty_signatory import CounterpartySignatory
from typing import Any, Dict
from pydantic.v1 import BaseModel, Field, constr

name: StrictStr = "example_name"
legal_entity_identifier: TypedResourceId = # Replace with your value
counterparty_signatory_instance = CounterpartySignatory(name=name, legal_entity_identifier=legal_entity_identifier)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

