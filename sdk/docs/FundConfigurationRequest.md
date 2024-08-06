# FundConfigurationRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** |  | 
**display_name** | **str** | The name of the Fund. | [optional] 
**description** | **str** | A description for the Fund. | [optional] 
**dealing_rule** | [**ComponentRule**](ComponentRule.md) |  | 
**fund_pnl_rule** | [**ComponentRule**](ComponentRule.md) |  | 
**back_out_rule** | [**ComponentRule**](ComponentRule.md) |  | 
**properties** | [**Dict[str, ModelProperty]**](ModelProperty.md) | A set of properties for the Fund Configuration. | [optional] 

## Example

```python
from lusid.models.fund_configuration_request import FundConfigurationRequest

# TODO update the JSON string below
json = "{}"
# create an instance of FundConfigurationRequest from a JSON string
fund_configuration_request_instance = FundConfigurationRequest.from_json(json)
# print the JSON string representation of the object
print FundConfigurationRequest.to_json()

# convert the object into a dict
fund_configuration_request_dict = fund_configuration_request_instance.to_dict()
# create an instance of FundConfigurationRequest from a dict
fund_configuration_request_form_dict = fund_configuration_request.from_dict(fund_configuration_request_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


