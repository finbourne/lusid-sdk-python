# InvestorIdentifier

Identification of an Investor on the LUSID API.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**investor_type** | **str** | The type of the investor of the Investor Record. Can be either a Person or a LegalEntity | [optional] 
**investor_identifiers** | [**Dict[str, ModelProperty]**](ModelProperty.md) | Single identifier that should target the desired person or legal entity | [optional] 
## Example

```python
from lusid.models.investor_identifier import InvestorIdentifier
from typing import Any, Dict, Optional
from pydantic.v1 import BaseModel, Field, StrictStr

investor_type: Optional[StrictStr] = "example_investor_type"
investor_identifiers: Optional[Dict[str, ModelProperty]] = # Replace with your value
investor_identifier_instance = InvestorIdentifier(investor_type=investor_type, investor_identifiers=investor_identifiers)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

