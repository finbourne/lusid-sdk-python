# InstrumentListComplianceParameter


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**ResourceId**](ResourceId.md) |  | 
**compliance_parameter_type** | **str** | The parameter type. The available values are: BoolComplianceParameter, StringComplianceParameter, DecimalComplianceParameter, DateTimeComplianceParameter, PropertyKeyComplianceParameter, AddressKeyComplianceParameter, PortfolioIdComplianceParameter, PortfolioGroupIdComplianceParameter, StringListComplianceParameter, BoolListComplianceParameter, DateTimeListComplianceParameter, DecimalListComplianceParameter, PropertyKeyListComplianceParameter, AddressKeyListComplianceParameter, PortfolioIdListComplianceParameter, PortfolioGroupIdListComplianceParameter, InstrumentListComplianceParameter | 

## Example

```python
from lusid.models.instrument_list_compliance_parameter import InstrumentListComplianceParameter

# TODO update the JSON string below
json = "{}"
# create an instance of InstrumentListComplianceParameter from a JSON string
instrument_list_compliance_parameter_instance = InstrumentListComplianceParameter.from_json(json)
# print the JSON string representation of the object
print InstrumentListComplianceParameter.to_json()

# convert the object into a dict
instrument_list_compliance_parameter_dict = instrument_list_compliance_parameter_instance.to_dict()
# create an instance of InstrumentListComplianceParameter from a dict
instrument_list_compliance_parameter_form_dict = instrument_list_compliance_parameter.from_dict(instrument_list_compliance_parameter_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


