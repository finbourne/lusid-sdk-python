# DecimalComplianceParameter


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | **float** |  | 
**compliance_parameter_type** | **str** | The parameter type. The available values are: BoolComplianceParameter, StringComplianceParameter, DecimalComplianceParameter, DateTimeComplianceParameter, PropertyKeyComplianceParameter, AddressKeyComplianceParameter, PortfolioIdComplianceParameter, PortfolioGroupIdComplianceParameter, StringListComplianceParameter, BoolListComplianceParameter, DateTimeListComplianceParameter, DecimalListComplianceParameter, PropertyKeyListComplianceParameter, AddressKeyListComplianceParameter, PortfolioIdListComplianceParameter, PortfolioGroupIdListComplianceParameter, InstrumentListComplianceParameter, FilterPredicateComplianceParameter, GroupFilterPredicateComplianceParameter, GroupBySelectorComplianceParameter | 

## Example

```python
from lusid.models.decimal_compliance_parameter import DecimalComplianceParameter

# TODO update the JSON string below
json = "{}"
# create an instance of DecimalComplianceParameter from a JSON string
decimal_compliance_parameter_instance = DecimalComplianceParameter.from_json(json)
# print the JSON string representation of the object
print DecimalComplianceParameter.to_json()

# convert the object into a dict
decimal_compliance_parameter_dict = decimal_compliance_parameter_instance.to_dict()
# create an instance of DecimalComplianceParameter from a dict
decimal_compliance_parameter_form_dict = decimal_compliance_parameter.from_dict(decimal_compliance_parameter_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


