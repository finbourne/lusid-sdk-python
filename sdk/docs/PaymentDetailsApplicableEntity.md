# PaymentDetailsApplicableEntity

Identifies the LUSID entity that holds the payment details (e.g. an InvestorRecord or Portfolio).
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**entity_type** | **str** | The type of the LUSID entity holding the payment details. e.g. \&quot;InvestorRecord\&quot;, \&quot;InvestmentAccount\&quot;, \&quot;Portfolio\&quot;. | 
**entity_scope** | **str** | The scope of the entity. Optional — required depends on the entity type. | [optional] 
**identifier_type** | **str** | The identifier type used to identify the entity. e.g. \&quot;lusidInvestmentAccountId\&quot;. | 
**identifier_scope** | **str** | The scope of the identifier used to identify the entity. Optional — null for native LUSID identifiers such as code. | [optional] 
**identifier_value** | **str** | The identifier value for the entity. e.g. \&quot;LUID_00003DNL\&quot;. | 
## Example

```python
from lusid.models.payment_details_applicable_entity import PaymentDetailsApplicableEntity
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

entity_type: StrictStr = "example_entity_type"
entity_scope: Optional[StrictStr] = "example_entity_scope"
identifier_type: StrictStr = "example_identifier_type"
identifier_scope: Optional[StrictStr] = "example_identifier_scope"
identifier_value: StrictStr = "example_identifier_value"
payment_details_applicable_entity_instance = PaymentDetailsApplicableEntity(entity_type=entity_type, entity_scope=entity_scope, identifier_type=identifier_type, identifier_scope=identifier_scope, identifier_value=identifier_value)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

