# PropertyKeyComplianceParameter

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | **str** | The key that uniquely identifies the property. It has the format {domain}/{scope}/{code}. | 
**compliance_parameter_type** | **str** | The parameter type. The available values are: BoolComplianceParameter, StringComplianceParameter, DecimalComplianceParameter, DateTimeComplianceParameter, PropertyKeyComplianceParameter, AddressKeyComplianceParameter, PortfolioIdComplianceParameter, PortfolioGroupIdComplianceParameter, StringListComplianceParameter, BoolListComplianceParameter, DateTimeListComplianceParameter, DecimalListComplianceParameter, PropertyKeyListComplianceParameter, AddressKeyListComplianceParameter, PortfolioIdListComplianceParameter, PortfolioGroupIdListComplianceParameter, InstrumentListComplianceParameter, FilterPredicateComplianceParameter, GroupFilterPredicateComplianceParameter, GroupBySelectorComplianceParameter, PropertyListComplianceParameter, GroupCalculationComplianceParameter | 
## Example

```python
from lusid.models.property_key_compliance_parameter import PropertyKeyComplianceParameter
from typing import Any, Dict
from pydantic.v1 import Field, StrictStr, validator

value: StrictStr = "example_value"
compliance_parameter_type: StrictStr = "example_compliance_parameter_type"
property_key_compliance_parameter_instance = PropertyKeyComplianceParameter(value=value, compliance_parameter_type=compliance_parameter_type)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

