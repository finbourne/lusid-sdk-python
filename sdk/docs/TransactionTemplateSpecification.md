# TransactionTemplateSpecification

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**instrument_event_type** | **str** |  | 
**supported_instrument_types** | **List[str]** |  | 
**supported_participation_types** | **List[str]** |  | 
**supported_election_types** | [**List[ElectionSpecification]**](ElectionSpecification.md) |  | 
**supported_template_fields** | [**List[TemplateField]**](TemplateField.md) |  | 
**eligibility_calculation** | [**EligibilityCalculation**](EligibilityCalculation.md) |  | 
## Example

```python
from lusid.models.transaction_template_specification import TransactionTemplateSpecification
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

instrument_event_type: StrictStr = "example_instrument_event_type"
supported_instrument_types: List[StrictStr] = # Replace with your value
supported_participation_types: List[StrictStr] = # Replace with your value
supported_election_types: List[ElectionSpecification] = # Replace with your value
supported_template_fields: List[TemplateField] = # Replace with your value
eligibility_calculation: EligibilityCalculation = # Replace with your value
transaction_template_specification_instance = TransactionTemplateSpecification(instrument_event_type=instrument_event_type, supported_instrument_types=supported_instrument_types, supported_participation_types=supported_participation_types, supported_election_types=supported_election_types, supported_template_fields=supported_template_fields, eligibility_calculation=eligibility_calculation)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

