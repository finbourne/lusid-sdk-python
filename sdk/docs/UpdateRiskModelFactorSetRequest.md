# UpdateRiskModelFactorSetRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**display_name** | **str** | Factor Set name. | 

## Example

```python
from lusid.models.update_risk_model_factor_set_request import UpdateRiskModelFactorSetRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateRiskModelFactorSetRequest from a JSON string
update_risk_model_factor_set_request_instance = UpdateRiskModelFactorSetRequest.from_json(json)
# print the JSON string representation of the object
print UpdateRiskModelFactorSetRequest.to_json()

# convert the object into a dict
update_risk_model_factor_set_request_dict = update_risk_model_factor_set_request_instance.to_dict()
# create an instance of UpdateRiskModelFactorSetRequest from a dict
update_risk_model_factor_set_request_form_dict = update_risk_model_factor_set_request.from_dict(update_risk_model_factor_set_request_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


