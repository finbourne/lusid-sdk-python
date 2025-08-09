# Fee

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**href** | **str** | The specific Uniform Resource Identifier (URI) for this resource at the requested effective and asAt datetime. | [optional] 
**fee_code** | **str** | The code of the Fee. | [optional] 
**fee_type_id** | [**ResourceId**](ResourceId.md) |  | 
**display_name** | **str** | The name of the Fee. | 
**description** | **str** | A description for the Fee. | [optional] 
**origin** | **str** | The origin or source of the Fee accrual. | [optional] 
**calculation_base** | **str** | The calculation base for a Fee that is calculated using a percentage (TotalAnnualAccrualAmount and CalculationBase cannot both be present). When the Fee is a ShareClass Fee (i.e: when ShareClasses contains at least one value), each of the following would be a valid CalculationBase: \&quot;10000.00\&quot;, \&quot;ShareClass.GAV\&quot;, \&quot;ShareClass.GAV - ShareClass.Fees[ShareClassFeeCode1].Amount\&quot;, \&quot;ShareClass.Fees[ShareClassFeeCode1].CalculationBase\&quot;. When the Fee is a NonShareClassSpecific Fee (i.e: when ShareClasses contains no values), each of the following would be a valid CalculationBase: \&quot;10000.00\&quot;, \&quot;GAV\&quot;, \&quot;GAV - Fees[NonClassSpecificFeeCode1].Amount\&quot;, \&quot;Fees[NonClassSpecificFeeCode1].CalculationBase\&quot;.  | [optional] 
**accrual_currency** | **str** | The accrual currency. | 
**treatment** | **str** | The accrual period of the Fee; &#39;Monthly&#39; or &#39;Daily&#39;. | 
**total_annual_accrual_amount** | **float** | The total annual accrued amount for the Fee. (TotalAnnualAccrualAmount and CalculationBase cannot both be present) | [optional] 
**fee_rate_percentage** | **float** | The fee rate percentage. (Required when CalculationBase is present and not compatible with TotalAnnualAccrualAmount) | [optional] 
**payable_frequency** | **str** | The payable frequency for the Fee; &#39;Annually&#39;, &#39;Quarterly&#39; or &#39;Monthly&#39;. | 
**business_day_convention** | **str** | The business day convention to use for Fee calculations on weekends or holidays. Supported string values are: [Previous, P, Following, F, None]. | 
**start_date** | **datetime** | The start date of the Fee. | 
**end_date** | **datetime** | The end date of the Fee. | [optional] 
**anchor_date** | [**DayMonth**](DayMonth.md) |  | [optional] 
**properties** | [**Dict[str, ModelProperty]**](ModelProperty.md) | The Fee properties. These will be from the &#39;Fee&#39; domain. | [optional] 
**version** | [**Version**](Version.md) |  | [optional] 
**portfolio_id** | [**ResourceId**](ResourceId.md) |  | [optional] 
**share_classes** | **List[str]** | The short codes of the ShareClasses that the Fee should be applied to. Optional: if this is null or empty, then the Fee will be divided between all the ShareClasses of the Fund according to the capital ratio. | [optional] 
**nav_type_code** | **str** | When provided runs against the specified NAV Type, otherwise the Primary NAV Type will be used. | [optional] 
**links** | [**List[Link]**](Link.md) |  | [optional] 
## Example

```python
from lusid.models.fee import Fee
from typing import Any, Dict, List, Optional, Union
from pydantic.v1 import BaseModel, Field, StrictFloat, StrictInt, StrictStr, conlist, constr, validator
from datetime import datetime
href: Optional[StrictStr] = "example_href"
fee_code: Optional[StrictStr] = "example_fee_code"
fee_type_id: ResourceId = # Replace with your value
display_name: StrictStr = "example_display_name"
description: Optional[StrictStr] = "example_description"
origin: Optional[StrictStr] = "example_origin"
calculation_base: Optional[StrictStr] = "example_calculation_base"
accrual_currency: StrictStr = "example_accrual_currency"
treatment: StrictStr = "example_treatment"
total_annual_accrual_amount: Optional[Union[StrictFloat, StrictInt]] = # Replace with your value
fee_rate_percentage: Optional[Union[StrictFloat, StrictInt]] = # Replace with your value
payable_frequency: StrictStr = "example_payable_frequency"
business_day_convention: StrictStr = "example_business_day_convention"
start_date: datetime = # Replace with your value
end_date: Optional[datetime] = # Replace with your value
anchor_date: Optional[DayMonth] = # Replace with your value
properties: Optional[Dict[str, ModelProperty]] = # Replace with your value
version: Optional[Version] = None
portfolio_id: Optional[ResourceId] = # Replace with your value
share_classes: Optional[conlist(StrictStr)] = # Replace with your value
nav_type_code: Optional[StrictStr] = "example_nav_type_code"
links: Optional[conlist(Link)] = None
fee_instance = Fee(href=href, fee_code=fee_code, fee_type_id=fee_type_id, display_name=display_name, description=description, origin=origin, calculation_base=calculation_base, accrual_currency=accrual_currency, treatment=treatment, total_annual_accrual_amount=total_annual_accrual_amount, fee_rate_percentage=fee_rate_percentage, payable_frequency=payable_frequency, business_day_convention=business_day_convention, start_date=start_date, end_date=end_date, anchor_date=anchor_date, properties=properties, version=version, portfolio_id=portfolio_id, share_classes=share_classes, nav_type_code=nav_type_code, links=links)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

