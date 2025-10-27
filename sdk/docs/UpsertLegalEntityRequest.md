# UpsertLegalEntityRequest

Request to create or update an legal entity
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**identifiers** | [**Dict[str, ModelProperty]**](ModelProperty.md) | The identifiers the legal entity will be upserted with.The provided keys should be idTypeScope, idTypeCode, code | 
**properties** | [**Dict[str, ModelProperty]**](ModelProperty.md) | A set of properties associated to the Legal Entity. | [optional] 
**display_name** | **str** | The display name of the Legal Entity | 
**description** | **str** | The description of the Legal Entity | [optional] 
**counterparty_risk_information** | [**CounterpartyRiskInformation**](CounterpartyRiskInformation.md) |  | [optional] 
## Example

```python
from lusid.models.upsert_legal_entity_request import UpsertLegalEntityRequest
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

identifiers: Dict[str, ModelProperty] = # Replace with your value
properties: Optional[Dict[str, ModelProperty]] = # Replace with your value
display_name: StrictStr = "example_display_name"
description: Optional[StrictStr] = "example_description"
counterparty_risk_information: Optional[CounterpartyRiskInformation] = # Replace with your value
upsert_legal_entity_request_instance = UpsertLegalEntityRequest(identifiers=identifiers, properties=properties, display_name=display_name, description=description, counterparty_risk_information=counterparty_risk_information)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

