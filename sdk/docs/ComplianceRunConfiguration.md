# ComplianceRunConfiguration

Specification object for the configuration parameters of a compliance run

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pre_trade_configuration** | [**PreTradeConfiguration**](PreTradeConfiguration.md) |  | 

## Example

```python
from lusid.models.compliance_run_configuration import ComplianceRunConfiguration

# TODO update the JSON string below
json = "{}"
# create an instance of ComplianceRunConfiguration from a JSON string
compliance_run_configuration_instance = ComplianceRunConfiguration.from_json(json)
# print the JSON string representation of the object
print ComplianceRunConfiguration.to_json()

# convert the object into a dict
compliance_run_configuration_dict = compliance_run_configuration_instance.to_dict()
# create an instance of ComplianceRunConfiguration from a dict
compliance_run_configuration_form_dict = compliance_run_configuration.from_dict(compliance_run_configuration_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


