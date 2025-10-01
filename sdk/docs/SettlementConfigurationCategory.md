# SettlementConfigurationCategory

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**method** | **str** | The method of settlement for the movements of the relevant type(s). Allowed values: &#39;Automatic&#39; and &#39;Instructed&#39;. A value of &#39;Instructed&#39; means that such movements can only be settled with a SettlementInstruction. A value of &#39;Automatic&#39; means that such movements will settle automatically but a SettlementInstruction will still override automatic settlement. | [optional] 
**calculate_instruction_to_portfolio_rate** | **bool** | An optional flag that allows for the calculation of the instruction to portfolio rate for instructions with settlement category CashSettlement or DeferredCashReceipt, if it is not provided on the settlement instruction. Defaults to false if not specified. | [optional] 
**calculate_in_lieu_settlement_amount** | **bool** | An optional flag that allows for the calculation of the in lieu amount for instructions with settlement category CashSettlement or DeferredCashReceipt, if it is not provided on the settlement instruction. Defaults to false if not specified. | [optional] 
## Example

```python
from lusid.models.settlement_configuration_category import SettlementConfigurationCategory
from typing import Any, Dict, Optional
from pydantic.v1 import BaseModel, Field, StrictBool, StrictStr

method: Optional[StrictStr] = "example_method"
calculate_instruction_to_portfolio_rate: Optional[StrictBool] = # Replace with your value
calculate_instruction_to_portfolio_rate:Optional[StrictBool] = None
calculate_in_lieu_settlement_amount: Optional[StrictBool] = # Replace with your value
calculate_in_lieu_settlement_amount:Optional[StrictBool] = None
settlement_configuration_category_instance = SettlementConfigurationCategory(method=method, calculate_instruction_to_portfolio_rate=calculate_instruction_to_portfolio_rate, calculate_in_lieu_settlement_amount=calculate_in_lieu_settlement_amount)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

