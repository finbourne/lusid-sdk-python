# CalculationInfo


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**calculation_method** | **str** | Method of calculating the fees or commission among: BasisPoints, Percentage, Rate, Flat etc. | 
**multiplier** | **str** | Field by which to multiply the numerical amount. Eg: Quantity, Value | 
**calculation_amount** | **float** | Numerical fee amount | 

## Example

```python
from lusid.models.calculation_info import CalculationInfo

# TODO update the JSON string below
json = "{}"
# create an instance of CalculationInfo from a JSON string
calculation_info_instance = CalculationInfo.from_json(json)
# print the JSON string representation of the object
print CalculationInfo.to_json()

# convert the object into a dict
calculation_info_dict = calculation_info_instance.to_dict()
# create an instance of CalculationInfo from a dict
calculation_info_form_dict = calculation_info.from_dict(calculation_info_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


