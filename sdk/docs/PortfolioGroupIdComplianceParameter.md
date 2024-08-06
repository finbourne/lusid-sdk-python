# PortfolioGroupIdComplianceParameter


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**ResourceId**](ResourceId.md) |  | 
**compliance_parameter_type** | **str** | The parameter type. The available values are: BoolComplianceParameter, StringComplianceParameter, DecimalComplianceParameter, DateTimeComplianceParameter, PropertyKeyComplianceParameter, AddressKeyComplianceParameter, PortfolioIdComplianceParameter, PortfolioGroupIdComplianceParameter, StringListComplianceParameter, BoolListComplianceParameter, DateTimeListComplianceParameter, DecimalListComplianceParameter, PropertyKeyListComplianceParameter, AddressKeyListComplianceParameter, PortfolioIdListComplianceParameter, PortfolioGroupIdListComplianceParameter, InstrumentListComplianceParameter, FilterPredicateComplianceParameter, GroupFilterPredicateComplianceParameter, GroupBySelectorComplianceParameter, PropertyListComplianceParameter, GroupCalculationComplianceParameter | 

## Example

```python
from lusid.models.portfolio_group_id_compliance_parameter import PortfolioGroupIdComplianceParameter

# TODO update the JSON string below
json = "{}"
# create an instance of PortfolioGroupIdComplianceParameter from a JSON string
portfolio_group_id_compliance_parameter_instance = PortfolioGroupIdComplianceParameter.from_json(json)
# print the JSON string representation of the object
print PortfolioGroupIdComplianceParameter.to_json()

# convert the object into a dict
portfolio_group_id_compliance_parameter_dict = portfolio_group_id_compliance_parameter_instance.to_dict()
# create an instance of PortfolioGroupIdComplianceParameter from a dict
portfolio_group_id_compliance_parameter_form_dict = portfolio_group_id_compliance_parameter.from_dict(portfolio_group_id_compliance_parameter_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


