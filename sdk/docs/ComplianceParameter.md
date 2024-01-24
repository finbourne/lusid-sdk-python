# ComplianceParameter


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**compliance_parameter_type** | **str** | The parameter type. The available values are: BoolComplianceParameter, StringComplianceParameter, DecimalComplianceParameter, DateTimeComplianceParameter, PropertyKeyComplianceParameter, AddressKeyComplianceParameter, PortfolioIdComplianceParameter, PortfolioGroupIdComplianceParameter, StringListComplianceParameter, BoolListComplianceParameter, DateTimeListComplianceParameter, DecimalListComplianceParameter, PropertyKeyListComplianceParameter, AddressKeyListComplianceParameter, PortfolioIdListComplianceParameter, PortfolioGroupIdListComplianceParameter, InstrumentListComplianceParameter, FilterPredicateComplianceParameter, GroupFilterPredicateComplianceParameter | 

## Example

```python
from lusid.models.compliance_parameter import ComplianceParameter

# TODO update the JSON string below
json = "{}"
# create an instance of ComplianceParameter from a JSON string
compliance_parameter_instance = ComplianceParameter.from_json(json)
# print the JSON string representation of the object
print ComplianceParameter.to_json()

# convert the object into a dict
compliance_parameter_dict = compliance_parameter_instance.to_dict()
# create an instance of ComplianceParameter from a dict
compliance_parameter_form_dict = compliance_parameter.from_dict(compliance_parameter_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


