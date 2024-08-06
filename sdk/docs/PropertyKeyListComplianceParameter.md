# PropertyKeyListComplianceParameter


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**ResourceId**](ResourceId.md) |  | 
**compliance_parameter_type** | **str** | The parameter type. The available values are: BoolComplianceParameter, StringComplianceParameter, DecimalComplianceParameter, DateTimeComplianceParameter, PropertyKeyComplianceParameter, AddressKeyComplianceParameter, PortfolioIdComplianceParameter, PortfolioGroupIdComplianceParameter, StringListComplianceParameter, BoolListComplianceParameter, DateTimeListComplianceParameter, DecimalListComplianceParameter, PropertyKeyListComplianceParameter, AddressKeyListComplianceParameter, PortfolioIdListComplianceParameter, PortfolioGroupIdListComplianceParameter, InstrumentListComplianceParameter, FilterPredicateComplianceParameter, GroupFilterPredicateComplianceParameter, GroupBySelectorComplianceParameter, PropertyListComplianceParameter, GroupCalculationComplianceParameter | 

## Example

```python
from lusid.models.property_key_list_compliance_parameter import PropertyKeyListComplianceParameter

# TODO update the JSON string below
json = "{}"
# create an instance of PropertyKeyListComplianceParameter from a JSON string
property_key_list_compliance_parameter_instance = PropertyKeyListComplianceParameter.from_json(json)
# print the JSON string representation of the object
print PropertyKeyListComplianceParameter.to_json()

# convert the object into a dict
property_key_list_compliance_parameter_dict = property_key_list_compliance_parameter_instance.to_dict()
# create an instance of PropertyKeyListComplianceParameter from a dict
property_key_list_compliance_parameter_form_dict = property_key_list_compliance_parameter.from_dict(property_key_list_compliance_parameter_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


