# EligibilityCalculation


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**entitlement_date** | **str** |  | 
**eligible_units** | **str** |  | 
**date_modifiable_by_instruction** | **bool** |  | [optional] 

## Example

```python
from lusid.models.eligibility_calculation import EligibilityCalculation

# TODO update the JSON string below
json = "{}"
# create an instance of EligibilityCalculation from a JSON string
eligibility_calculation_instance = EligibilityCalculation.from_json(json)
# print the JSON string representation of the object
print EligibilityCalculation.to_json()

# convert the object into a dict
eligibility_calculation_dict = eligibility_calculation_instance.to_dict()
# create an instance of EligibilityCalculation from a dict
eligibility_calculation_form_dict = eligibility_calculation.from_dict(eligibility_calculation_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


