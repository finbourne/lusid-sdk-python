# AddressKeyComplianceParameter


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | **str** | The key that uniquely identifies a queryable address in Lusid. | 
**compliance_parameter_type** | **str** | The parameter type. The available values are: BoolComplianceParameter, StringComplianceParameter, DecimalComplianceParameter, DateTimeComplianceParameter, PropertyKeyComplianceParameter, AddressKeyComplianceParameter, PortfolioIdComplianceParameter, PortfolioGroupIdComplianceParameter, StringListComplianceParameter, BoolListComplianceParameter, DateTimeListComplianceParameter, DecimalListComplianceParameter, PropertyKeyListComplianceParameter, AddressKeyListComplianceParameter, PortfolioIdListComplianceParameter, PortfolioGroupIdListComplianceParameter, InstrumentListComplianceParameter | 

## Example

```python
from lusid.models.address_key_compliance_parameter import AddressKeyComplianceParameter

# TODO update the JSON string below
json = "{}"
# create an instance of AddressKeyComplianceParameter from a JSON string
address_key_compliance_parameter_instance = AddressKeyComplianceParameter.from_json(json)
# print the JSON string representation of the object
print AddressKeyComplianceParameter.to_json()

# convert the object into a dict
address_key_compliance_parameter_dict = address_key_compliance_parameter_instance.to_dict()
# create an instance of AddressKeyComplianceParameter from a dict
address_key_compliance_parameter_form_dict = address_key_compliance_parameter.from_dict(address_key_compliance_parameter_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


