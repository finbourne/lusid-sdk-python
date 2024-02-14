# BoolListComplianceParameter


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**ResourceId**](ResourceId.md) |  | 
**compliance_parameter_type** | **str** | The parameter type. The available values are: BoolComplianceParameter, StringComplianceParameter, DecimalComplianceParameter, DateTimeComplianceParameter, PropertyKeyComplianceParameter, AddressKeyComplianceParameter, PortfolioIdComplianceParameter, PortfolioGroupIdComplianceParameter, StringListComplianceParameter, BoolListComplianceParameter, DateTimeListComplianceParameter, DecimalListComplianceParameter, PropertyKeyListComplianceParameter, AddressKeyListComplianceParameter, PortfolioIdListComplianceParameter, PortfolioGroupIdListComplianceParameter, InstrumentListComplianceParameter, FilterPredicateComplianceParameter, GroupFilterPredicateComplianceParameter, GroupBySelectorComplianceParameter | 

## Example

```python
from lusid.models.bool_list_compliance_parameter import BoolListComplianceParameter

# TODO update the JSON string below
json = "{}"
# create an instance of BoolListComplianceParameter from a JSON string
bool_list_compliance_parameter_instance = BoolListComplianceParameter.from_json(json)
# print the JSON string representation of the object
print BoolListComplianceParameter.to_json()

# convert the object into a dict
bool_list_compliance_parameter_dict = bool_list_compliance_parameter_instance.to_dict()
# create an instance of BoolListComplianceParameter from a dict
bool_list_compliance_parameter_form_dict = bool_list_compliance_parameter.from_dict(bool_list_compliance_parameter_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


