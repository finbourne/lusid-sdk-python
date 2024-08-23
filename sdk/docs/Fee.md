# Fee


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**href** | **str** | The specific Uniform Resource Identifier (URI) for this resource at the requested effective and asAt datetime. | [optional] 
**fee_code** | **str** | The code of the Fee. | [optional] 
**fee_type** | [**ResourceId**](ResourceId.md) |  | 
**name** | **str** | The name of the Fee. | 
**description** | **str** | A description for the Fee. | [optional] 
**origin** | **str** | The origin or source of the Fee accrual. | [optional] 
**calculation_base** | **str** | The calculation base for the Fee that is calculated using a percentage. (TotalAnnualAccrualAmount and CalculationBase cannot both be present) | [optional] 
**accrual_currency** | **str** | The accrual currency. | 
**treatment** | **str** | The accrual period of the Fee; &#39;Monthly&#39; or &#39;Daily&#39;. | 
**total_annual_accrual_amount** | **float** | The total annual accrued amount for the Fee. (TotalAnnualAccrualAmount and CalculationBase cannot both be present) | [optional] 
**fee_rate_percentage** | **float** | The fee rate percentage. (Required when CalculationBase is present and not compatible with TotalAnnualAccrualAmount) | [optional] 
**payable_frequency** | **str** | The payable frequency for the Fee; &#39;Annually&#39;, &#39;Quarterly&#39; or &#39;Monthly&#39;. | 
**business_day_convention** | **str** | The business day convention to use for Fee calculations on weekends. Supported string values are: [Previous, P, Following, F]. | 
**start_date** | **datetime** | The start date of the Fee. | 
**end_date** | **datetime** | The end date of the Fee. | [optional] 
**anchor_date** | [**DayMonth**](DayMonth.md) |  | [optional] 
**properties** | [**Dict[str, ModelProperty]**](ModelProperty.md) | The Fee properties. These will be from the &#39;Fee&#39; domain. | [optional] 
**version** | [**Version**](Version.md) |  | [optional] 
**portfolio_id** | [**ResourceId**](ResourceId.md) |  | [optional] 
**links** | [**List[Link]**](Link.md) |  | [optional] 

## Example

```python
from lusid.models.fee import Fee

# TODO update the JSON string below
json = "{}"
# create an instance of Fee from a JSON string
fee_instance = Fee.from_json(json)
# print the JSON string representation of the object
print Fee.to_json()

# convert the object into a dict
fee_dict = fee_instance.to_dict()
# create an instance of Fee from a dict
fee_form_dict = fee.from_dict(fee_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


