# PortfolioGroupIdComplianceParameter

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**ResourceId**](ResourceId.md) |  | 
**compliance_parameter_type** | **str** | The parameter type. The available values are: BoolComplianceParameter, StringComplianceParameter, DecimalComplianceParameter, DateTimeComplianceParameter, PropertyKeyComplianceParameter, AddressKeyComplianceParameter, PortfolioIdComplianceParameter, PortfolioGroupIdComplianceParameter, StringListComplianceParameter, BoolListComplianceParameter, DateTimeListComplianceParameter, DecimalListComplianceParameter, PropertyKeyListComplianceParameter, AddressKeyListComplianceParameter, PortfolioIdListComplianceParameter, PortfolioGroupIdListComplianceParameter, InstrumentListComplianceParameter, FilterPredicateComplianceParameter, GroupFilterPredicateComplianceParameter, GroupBySelectorComplianceParameter, PropertyListComplianceParameter, GroupCalculationComplianceParameter | 
## Example

```python
from lusid.models.portfolio_group_id_compliance_parameter import PortfolioGroupIdComplianceParameter
from typing import Any, Dict
from pydantic.v1 import Field, StrictStr, validator

value: ResourceId = # Replace with your value
compliance_parameter_type: StrictStr = "example_compliance_parameter_type"
portfolio_group_id_compliance_parameter_instance = PortfolioGroupIdComplianceParameter(value=value, compliance_parameter_type=compliance_parameter_type)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

