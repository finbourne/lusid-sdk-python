# PropertyKeyComplianceParameter


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | **str** | The key that uniquely identifies the property. It has the format {domain}/{scope}/{code}. | 
**compliance_parameter_type** | **str** | The parameter type. The available values are: BoolComplianceParameter, StringComplianceParameter, DecimalComplianceParameter, DateTimeComplianceParameter, PropertyKeyComplianceParameter, AddressKeyComplianceParameter, PortfolioIdComplianceParameter, PortfolioGroupIdComplianceParameter, StringListComplianceParameter, BoolListComplianceParameter, DateTimeListComplianceParameter, DecimalListComplianceParameter, PropertyKeyListComplianceParameter, AddressKeyListComplianceParameter, PortfolioIdListComplianceParameter, PortfolioGroupIdListComplianceParameter, InstrumentListComplianceParameter, FilterPredicateComplianceParameter, GroupFilterPredicateComplianceParameter, GroupBySelectorComplianceParameter, PropertyListComplianceParameter, GroupCalculationComplianceParameter | 

## Example

```python
from lusid.models.property_key_compliance_parameter import PropertyKeyComplianceParameter

# TODO update the JSON string below
json = "{}"
# create an instance of PropertyKeyComplianceParameter from a JSON string
property_key_compliance_parameter_instance = PropertyKeyComplianceParameter.from_json(json)
# print the JSON string representation of the object
print PropertyKeyComplianceParameter.to_json()

# convert the object into a dict
property_key_compliance_parameter_dict = property_key_compliance_parameter_instance.to_dict()
# create an instance of PropertyKeyComplianceParameter from a dict
property_key_compliance_parameter_form_dict = property_key_compliance_parameter.from_dict(property_key_compliance_parameter_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


