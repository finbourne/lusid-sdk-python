# AddressKeyListComplianceParameter


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**ResourceId**](ResourceId.md) |  | 
**compliance_parameter_type** | **str** | The parameter type. The available values are: BoolComplianceParameter, StringComplianceParameter, DecimalComplianceParameter, DateTimeComplianceParameter, PropertyKeyComplianceParameter, AddressKeyComplianceParameter, PortfolioIdComplianceParameter, PortfolioGroupIdComplianceParameter, StringListComplianceParameter, BoolListComplianceParameter, DateTimeListComplianceParameter, DecimalListComplianceParameter, PropertyKeyListComplianceParameter, AddressKeyListComplianceParameter, PortfolioIdListComplianceParameter, PortfolioGroupIdListComplianceParameter, InstrumentListComplianceParameter, FilterPredicateComplianceParameter, GroupFilterPredicateComplianceParameter, GroupBySelectorComplianceParameter, PropertyListComplianceParameter, GroupCalculationComplianceParameter | 

## Example

```python
from lusid.models.address_key_list_compliance_parameter import AddressKeyListComplianceParameter

# TODO update the JSON string below
json = "{}"
# create an instance of AddressKeyListComplianceParameter from a JSON string
address_key_list_compliance_parameter_instance = AddressKeyListComplianceParameter.from_json(json)
# print the JSON string representation of the object
print AddressKeyListComplianceParameter.to_json()

# convert the object into a dict
address_key_list_compliance_parameter_dict = address_key_list_compliance_parameter_instance.to_dict()
# create an instance of AddressKeyListComplianceParameter from a dict
address_key_list_compliance_parameter_form_dict = address_key_list_compliance_parameter.from_dict(address_key_list_compliance_parameter_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


