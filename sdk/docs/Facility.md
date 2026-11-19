# Facility

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**href** | **str** | The specific Uniform Resource Identifier (URI) for this resource at the requested effective and asAt datetime. | [optional] 
**facility_code** | **str** | The code of the Facility, unique within the Fund. | [optional] 
**display_name** | **str** | The name of the Facility. | 
**description** | **str** | A description for the Facility. | [optional] 
**lender** | **str** | The name of the lender providing the Facility. | 
**limit** | **float** | The committed limit of the Facility. Must be greater than zero. | 
**currency** | **str** | The three-letter currency code in which the Facility is denominated. | 
**rate_reference** | **str** | The reference rate the Facility interest is based on, for example SOFR. Optional. | [optional] 
**margin** | **float** | The margin over the reference rate, expressed as a decimal. Must be zero or greater. | 
**commitment_fee_rate** | **float** | The annual commitment fee rate charged on the undrawn balance, expressed as a decimal. Must be zero or greater. | 
**day_count_convention** | **str** | The day count convention used to accrue interest. One of: Act360, Act365, Act365F, Thirty360. | 
**available_from** | **datetime** | The first date the Facility may be drawn, inclusive. A draw dated before it is refused. Required on creation; a Facility stored without one may be drawn on any date. | [optional] 
**maturity_date** | **datetime** | The last date the Facility may be drawn, inclusive. A draw dated after it is refused; a repayment is not. Optional; omit for a Facility with no maturity. | [optional] 
**limit_changes** | [**List[FacilityLimitChange]**](FacilityLimitChange.md) | Changes to the committed limit after the initial limit, each in force from its effective date until the next. Each must take effect after AvailableFrom and, when set, on or before MaturityDate. A draw is held to the limit in force on its date. | [optional] 
**warnings** | [**List[Warning]**](Warning.md) | Warnings about the Facility as stored, for example that its limit is now below what is already drawn. Only present on a successful update. | [optional] 
**version** | [**Version**](Version.md) |  | [optional] 
**links** | [**List[Link]**](Link.md) |  | [optional] 
## Example

```python
from lusid.models.facility import Facility
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

href: Optional[StrictStr] = "example_href"
facility_code: Optional[StrictStr] = "example_facility_code"
display_name: StrictStr = "example_display_name"
description: Optional[StrictStr] = "example_description"
lender: StrictStr = "example_lender"
limit: Union[StrictFloat, StrictInt] = # Replace with your value
currency: StrictStr = "example_currency"
rate_reference: Optional[StrictStr] = "example_rate_reference"
margin: Union[StrictFloat, StrictInt] = # Replace with your value
commitment_fee_rate: Union[StrictFloat, StrictInt] = # Replace with your value
day_count_convention: StrictStr = "example_day_count_convention"
available_from: Optional[datetime] = # Replace with your value
maturity_date: Optional[datetime] = # Replace with your value
limit_changes: Optional[List[FacilityLimitChange]] = # Replace with your value
warnings: Optional[List[Warning]] = # Replace with your value
version: Optional[Version] = None
links: Optional[List[Link]] = None
facility_instance = Facility(href=href, facility_code=facility_code, display_name=display_name, description=description, lender=lender, limit=limit, currency=currency, rate_reference=rate_reference, margin=margin, commitment_fee_rate=commitment_fee_rate, day_count_convention=day_count_convention, available_from=available_from, maturity_date=maturity_date, limit_changes=limit_changes, warnings=warnings, version=version, links=links)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

