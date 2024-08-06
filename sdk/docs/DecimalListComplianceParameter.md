# DecimalListComplianceParameter


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**ResourceId**](ResourceId.md) |  | 
**compliance_parameter_type** | **str** | The parameter type. The available values are: BoolComplianceParameter, StringComplianceParameter, DecimalComplianceParameter, DateTimeComplianceParameter, PropertyKeyComplianceParameter, AddressKeyComplianceParameter, PortfolioIdComplianceParameter, PortfolioGroupIdComplianceParameter, StringListComplianceParameter, BoolListComplianceParameter, DateTimeListComplianceParameter, DecimalListComplianceParameter, PropertyKeyListComplianceParameter, AddressKeyListComplianceParameter, PortfolioIdListComplianceParameter, PortfolioGroupIdListComplianceParameter, InstrumentListComplianceParameter, FilterPredicateComplianceParameter, GroupFilterPredicateComplianceParameter, GroupBySelectorComplianceParameter, PropertyListComplianceParameter, GroupCalculationComplianceParameter | 

## Example

```python
from lusid.models.decimal_list_compliance_parameter import DecimalListComplianceParameter

# TODO update the JSON string below
json = "{}"
# create an instance of DecimalListComplianceParameter from a JSON string
decimal_list_compliance_parameter_instance = DecimalListComplianceParameter.from_json(json)
# print the JSON string representation of the object
print DecimalListComplianceParameter.to_json()

# convert the object into a dict
decimal_list_compliance_parameter_dict = decimal_list_compliance_parameter_instance.to_dict()
# create an instance of DecimalListComplianceParameter from a dict
decimal_list_compliance_parameter_form_dict = decimal_list_compliance_parameter.from_dict(decimal_list_compliance_parameter_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


