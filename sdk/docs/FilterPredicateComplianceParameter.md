# FilterPredicateComplianceParameter


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | **str** |  | 
**compliance_parameter_type** | **str** | The parameter type. The available values are: BoolComplianceParameter, StringComplianceParameter, DecimalComplianceParameter, DateTimeComplianceParameter, PropertyKeyComplianceParameter, AddressKeyComplianceParameter, PortfolioIdComplianceParameter, PortfolioGroupIdComplianceParameter, StringListComplianceParameter, BoolListComplianceParameter, DateTimeListComplianceParameter, DecimalListComplianceParameter, PropertyKeyListComplianceParameter, AddressKeyListComplianceParameter, PortfolioIdListComplianceParameter, PortfolioGroupIdListComplianceParameter, InstrumentListComplianceParameter, FilterPredicateComplianceParameter, GroupFilterPredicateComplianceParameter | 

## Example

```python
from lusid.models.filter_predicate_compliance_parameter import FilterPredicateComplianceParameter

# TODO update the JSON string below
json = "{}"
# create an instance of FilterPredicateComplianceParameter from a JSON string
filter_predicate_compliance_parameter_instance = FilterPredicateComplianceParameter.from_json(json)
# print the JSON string representation of the object
print FilterPredicateComplianceParameter.to_json()

# convert the object into a dict
filter_predicate_compliance_parameter_dict = filter_predicate_compliance_parameter_instance.to_dict()
# create an instance of FilterPredicateComplianceParameter from a dict
filter_predicate_compliance_parameter_form_dict = filter_predicate_compliance_parameter.from_dict(filter_predicate_compliance_parameter_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


