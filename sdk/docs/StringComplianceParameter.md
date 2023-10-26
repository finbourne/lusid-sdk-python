# StringComplianceParameter


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | **str** |  | 
**compliance_parameter_type** | **str** | The parameter type. The available values are: BoolComplianceParameter, StringComplianceParameter, DecimalComplianceParameter, DateTimeComplianceParameter, PropertyKeyComplianceParameter, AddressKeyComplianceParameter, PortfolioIdComplianceParameter, PortfolioGroupIdComplianceParameter, StringListComplianceParameter, BoolListComplianceParameter, DateTimeListComplianceParameter, DecimalListComplianceParameter, PropertyKeyListComplianceParameter, AddressKeyListComplianceParameter, PortfolioIdListComplianceParameter, PortfolioGroupIdListComplianceParameter, InstrumentListComplianceParameter | 

## Example

```python
from lusid.models.string_compliance_parameter import StringComplianceParameter

# TODO update the JSON string below
json = "{}"
# create an instance of StringComplianceParameter from a JSON string
string_compliance_parameter_instance = StringComplianceParameter.from_json(json)
# print the JSON string representation of the object
print StringComplianceParameter.to_json()

# convert the object into a dict
string_compliance_parameter_dict = string_compliance_parameter_instance.to_dict()
# create an instance of StringComplianceParameter from a dict
string_compliance_parameter_form_dict = string_compliance_parameter.from_dict(string_compliance_parameter_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


