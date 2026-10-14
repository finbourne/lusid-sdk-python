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
**treatment** | **str** | The accrual period of the Fee. Available values: Daily, Monthly. | 
**total_annual_accrual_amount** | **float** | The total annual accrued amount for the Fee. (TotalAnnualAccrualAmount and CalculationBase cannot both be present) | [optional] 
**fee_rate_percentage** | **float** | The annual rate applied to the CalculationBase for a &#39;FixedPercentage&#39; Fee, expressed as a multiplier rather than a percentage: 0.052 means 5.2% of the base per year. (Required when CalculationBase is present and not compatible with TotalAnnualAccrualAmount) | [optional] 
**payable_frequency** | **str** | The payable frequency for the Fee. Available values: Annually, Quarterly, Monthly. | 
**business_day_convention** | **str** | The business day convention to use for Fee calculations on weekends or holidays. Available values: None, P, Previous, F, Following. | 
**start_date** | **datetime** | The start date of the Fee. | 
**end_date** | **datetime** | The end date of the Fee. | [optional] 
**anchor_date** | [**DayMonth**](DayMonth.md) |  | [optional] 
**properties** | [**Dict[str, ModelProperty]**](ModelProperty.md) | The Fee properties. These will be from the &#39;Fee&#39; domain. | [optional] 
**version** | [**Version**](Version.md) |  | [optional] 
**portfolio_id** | [**ResourceId**](ResourceId.md) |  | [optional] 
**share_classes** | **List[str]** | The short codes of the ShareClasses that the Fee should be applied to. Optional: if this is null or empty, then the Fee will be divided between all the ShareClasses of the Fund according to the capital ratio. | [optional] 
**nav_type_code** | **str** | When provided runs against the specified NAV Type, otherwise the Primary NAV Type will be used. | [optional] 
**fee_calculation_type** | **str** | How the Fee accrual amount is calculated. Supported values: &#39;FixedAnnual&#39; (a fixed annual amount, requires TotalAnnualAccrualAmount), &#39;FixedDaily&#39; (a fixed daily amount, requires DailyAccrualAmount), &#39;FixedPercentage&#39; (a fixed percentage of the CalculationBase, requires FeeRatePercentage), &#39;VariablePercentage&#39; (a percentage of the CalculationBase resolved from a rate source at each accrual date, requires VariablePercentageSource), &#39;Tiered&#39; (a single rate applied to the whole CalculationBase, chosen by the tier the base falls in, requires Tiers), &#39;Blended&#39; (each tier&#39;s rate applied to the portion of the CalculationBase within that tier, requires Tiers). Optional: when not provided it is inferred as &#39;FixedAnnual&#39; if TotalAnnualAccrualAmount is populated and &#39;FixedPercentage&#39; otherwise, so existing requests keep their behaviour; the new calculation types must be requested explicitly. Available values: FixedAnnual, FixedDaily, FixedPercentage, VariablePercentage, Tiered, Blended. | [optional] 
**daily_accrual_amount** | **float** | The fixed daily accrued amount for a &#39;FixedDaily&#39; Fee, in the fund currency. The amount accrues for each day of the accrual period with no annualisation or day-count proration; Treatment does not affect it. | [optional] 
**variable_percentage_source** | **str** | The source of the rate for a &#39;VariablePercentage&#39; Fee, in the form \&quot;scope/provider/instrumentIdType/instrumentId\&quot; identifying a Rate quote series in the quote store. At each accrual date the most recent rate at or before that date is used; if no rate can be found the valuation point calculation fails. The quote&#39;s normalised value (its value divided by any scale factor) is applied like FeeRatePercentage, as a multiplier of the CalculationBase: a rate of 5.2% must normalise to 0.052. | [optional] 
**variable_percentage_source_offset** | **float** | An optional adjustment added to the rate resolved from the VariablePercentageSource, expressed as a factor like FeeRatePercentage (e.g. 0.0025 adds 25 basis points). | [optional] 
**tiers** | [**List[FeeRateTier]**](FeeRateTier.md) | The rate tiers for a &#39;Tiered&#39; or &#39;Blended&#39; Fee: between 2 and 10 tiers over the CalculationBase. Every tier except the last must have a Threshold, and thresholds must be positive and strictly increasing; a base equal to a Threshold falls in that tier, and the final tier covers the balance above the last threshold. A &#39;Tiered&#39; Fee applies the rate of the tier the whole base falls in; a &#39;Blended&#39; Fee applies each tier&#39;s rate to the portion of the base within that tier. | [optional] 
**fee_cap** | **float** | An optional annual cap on the accrued fee for &#39;FixedPercentage&#39;, &#39;VariablePercentage&#39;, &#39;Tiered&#39; and &#39;Blended&#39; Fees, in the fund currency and assessed period-to-date. Each day accrues only up to the amount left under the cap for the current fee year, which runs from one AnchorDate to the next; once the cap is reached nothing further accrues until the next AnchorDate. | [optional] 
**fee_floor** | **float** | An optional annual floor on the calculated fee for &#39;FixedPercentage&#39;, &#39;VariablePercentage&#39;, &#39;Tiered&#39; and &#39;Blended&#39; Fees, in the fund currency. The annualised fee amount is raised to the floor before being prorated to each accrual day. | [optional] 
**links** | [**List[Link]**](Link.md) |  | [optional] 
## Example

```python
from lusid.models.fee import Fee
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
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
share_classes: Optional[List[StrictStr]] = # Replace with your value
nav_type_code: Optional[StrictStr] = "example_nav_type_code"
fee_calculation_type: Optional[StrictStr] = "example_fee_calculation_type"
daily_accrual_amount: Optional[Union[StrictFloat, StrictInt]] = # Replace with your value
variable_percentage_source: Optional[StrictStr] = "example_variable_percentage_source"
variable_percentage_source_offset: Optional[Union[StrictFloat, StrictInt]] = # Replace with your value
tiers: Optional[List[FeeRateTier]] = # Replace with your value
fee_cap: Optional[Union[StrictFloat, StrictInt]] = # Replace with your value
fee_floor: Optional[Union[StrictFloat, StrictInt]] = # Replace with your value
links: Optional[List[Link]] = None
fee_instance = Fee(href=href, fee_code=fee_code, fee_type_id=fee_type_id, display_name=display_name, description=description, origin=origin, calculation_base=calculation_base, accrual_currency=accrual_currency, treatment=treatment, total_annual_accrual_amount=total_annual_accrual_amount, fee_rate_percentage=fee_rate_percentage, payable_frequency=payable_frequency, business_day_convention=business_day_convention, start_date=start_date, end_date=end_date, anchor_date=anchor_date, properties=properties, version=version, portfolio_id=portfolio_id, share_classes=share_classes, nav_type_code=nav_type_code, fee_calculation_type=fee_calculation_type, daily_accrual_amount=daily_accrual_amount, variable_percentage_source=variable_percentage_source, variable_percentage_source_offset=variable_percentage_source_offset, tiers=tiers, fee_cap=fee_cap, fee_floor=fee_floor, links=links)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

