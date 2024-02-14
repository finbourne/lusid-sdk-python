# BoolComplianceParameter


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | **bool** |  | 
**compliance_parameter_type** | **str** | The parameter type. The available values are: BoolComplianceParameter, StringComplianceParameter, DecimalComplianceParameter, DateTimeComplianceParameter, PropertyKeyComplianceParameter, AddressKeyComplianceParameter, PortfolioIdComplianceParameter, PortfolioGroupIdComplianceParameter, StringListComplianceParameter, BoolListComplianceParameter, DateTimeListComplianceParameter, DecimalListComplianceParameter, PropertyKeyListComplianceParameter, AddressKeyListComplianceParameter, PortfolioIdListComplianceParameter, PortfolioGroupIdListComplianceParameter, InstrumentListComplianceParameter, FilterPredicateComplianceParameter, GroupFilterPredicateComplianceParameter, GroupBySelectorComplianceParameter | 

## Example

```python
from lusid.models.bool_compliance_parameter import BoolComplianceParameter

# TODO update the JSON string below
json = "{}"
# create an instance of BoolComplianceParameter from a JSON string
bool_compliance_parameter_instance = BoolComplianceParameter.from_json(json)
# print the JSON string representation of the object
print BoolComplianceParameter.to_json()

# convert the object into a dict
bool_compliance_parameter_dict = bool_compliance_parameter_instance.to_dict()
# create an instance of BoolComplianceParameter from a dict
bool_compliance_parameter_form_dict = bool_compliance_parameter.from_dict(bool_compliance_parameter_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


