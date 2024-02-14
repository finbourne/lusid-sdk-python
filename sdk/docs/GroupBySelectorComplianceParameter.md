# GroupBySelectorComplianceParameter


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | **str** |  | 
**compliance_parameter_type** | **str** | The parameter type. The available values are: BoolComplianceParameter, StringComplianceParameter, DecimalComplianceParameter, DateTimeComplianceParameter, PropertyKeyComplianceParameter, AddressKeyComplianceParameter, PortfolioIdComplianceParameter, PortfolioGroupIdComplianceParameter, StringListComplianceParameter, BoolListComplianceParameter, DateTimeListComplianceParameter, DecimalListComplianceParameter, PropertyKeyListComplianceParameter, AddressKeyListComplianceParameter, PortfolioIdListComplianceParameter, PortfolioGroupIdListComplianceParameter, InstrumentListComplianceParameter, FilterPredicateComplianceParameter, GroupFilterPredicateComplianceParameter, GroupBySelectorComplianceParameter | 

## Example

```python
from lusid.models.group_by_selector_compliance_parameter import GroupBySelectorComplianceParameter

# TODO update the JSON string below
json = "{}"
# create an instance of GroupBySelectorComplianceParameter from a JSON string
group_by_selector_compliance_parameter_instance = GroupBySelectorComplianceParameter.from_json(json)
# print the JSON string representation of the object
print GroupBySelectorComplianceParameter.to_json()

# convert the object into a dict
group_by_selector_compliance_parameter_dict = group_by_selector_compliance_parameter_instance.to_dict()
# create an instance of GroupBySelectorComplianceParameter from a dict
group_by_selector_compliance_parameter_form_dict = group_by_selector_compliance_parameter.from_dict(group_by_selector_compliance_parameter_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


