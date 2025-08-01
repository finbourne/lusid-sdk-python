# UpsertInvestorRecordRequest

Request to create or update an investor record
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**identifiers** | [**Dict[str, ModelProperty]**](ModelProperty.md) | Unique client-defined identifiers of the Investor Record. | 
**properties** | [**Dict[str, ModelProperty]**](ModelProperty.md) | A set of properties associated to the Investor Record. | [optional] 
**display_name** | **str** | The display name of the Investor Record | 
**description** | **str** | The description of the Investor Record | [optional] 
**investor** | [**InvestorIdentifier**](InvestorIdentifier.md) |  | 
## Example

```python
from lusid.models.upsert_investor_record_request import UpsertInvestorRecordRequest
from typing import Any, Dict, Optional
from pydantic.v1 import BaseModel, Field, constr, validator

identifiers: Dict[str, ModelProperty] = # Replace with your value
properties: Optional[Dict[str, ModelProperty]] = # Replace with your value
display_name: StrictStr = "example_display_name"
description: Optional[StrictStr] = "example_description"
investor: InvestorIdentifier = # Replace with your value
upsert_investor_record_request_instance = UpsertInvestorRecordRequest(identifiers=identifiers, properties=properties, display_name=display_name, description=description, investor=investor)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

