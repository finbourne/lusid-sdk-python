# TaxProvision

The deferred tax provision struck for a fund at a valuation point: the realised and notionally realised  (deemed disposal) gains it is built from, the indexation and loss relief applied, the rate, the resulting  provision amount, its movement since the previous valuation point and, once approved, who approved it.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**href** | **str** | The specific Uniform Resource Identifier (URI) for this resource at the requested effective and asAt datetime. | [optional] 
**fund** | [**ResourceId**](ResourceId.md) |  | 
**nav_type_code** | **str** | The NAV type the provision was struck for. | 
**diary_entry_code** | **str** | The diary entry code of the valuation point the provision was struck at. | 
**effective_at** | **datetime** | The effective date of the valuation point the provision was struck at. | 
**as_at** | **datetime** | The asAt datetime at which this version of the provision was recorded. | 
**status** | **str** | Whether the provision is an Estimate or has been Approved. An approved provision has been posted to the fund as an accrual. | 
**realised_gains** | **float** | The chargeable gains realised by disposals since the start of the tax period, after indexation allowance. | 
**unrealised_gains** | **float** | The chargeable gains that would arise on a notional deemed disposal of the fund&#39;s holdings at the valuation point. | 
**indexation_allowance** | **float** | The indexation allowance taken against the gains in this provision. | 
**losses_brought_forward** | **float** | The allowable losses standing at the start of the tax period and available to offset gains. | 
**losses_used** | **float** | The losses brought forward that were used against the gains in this provision. | 
**losses_carried_forward** | **float** | The allowable losses remaining after this provision, to be carried forward to the next tax period. Only realised losses are carried; a notional loss on the deemed disposal is not. | 
**rate_applied** | **float** | The tax rate applied to the net chargeable gains to arrive at the provision amount. | 
**provision_amount** | **float** | The deferred tax provision amount at the valuation point. | 
**movement** | [**TaxProvisionMovement**](TaxProvisionMovement.md) |  | 
**approved_by** | **str** | The user who approved the provision, if it has been approved. | [optional] 
**approved_at** | **datetime** | The asAt datetime at which the provision was approved, if it has been approved. | [optional] 
**links** | [**List[Link]**](Link.md) |  | [optional] 
## Example

```python
from lusid.models.tax_provision import TaxProvision
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

href: Optional[StrictStr] = "example_href"
fund: ResourceId
nav_type_code: StrictStr = "example_nav_type_code"
diary_entry_code: StrictStr = "example_diary_entry_code"
effective_at: datetime = # Replace with your value
as_at: datetime = # Replace with your value
status: StrictStr = "example_status"
realised_gains: Union[StrictFloat, StrictInt] = # Replace with your value
unrealised_gains: Union[StrictFloat, StrictInt] = # Replace with your value
indexation_allowance: Union[StrictFloat, StrictInt] = # Replace with your value
losses_brought_forward: Union[StrictFloat, StrictInt] = # Replace with your value
losses_used: Union[StrictFloat, StrictInt] = # Replace with your value
losses_carried_forward: Union[StrictFloat, StrictInt] = # Replace with your value
rate_applied: Union[StrictFloat, StrictInt] = # Replace with your value
provision_amount: Union[StrictFloat, StrictInt] = # Replace with your value
movement: TaxProvisionMovement
approved_by: Optional[StrictStr] = "example_approved_by"
approved_at: Optional[datetime] = # Replace with your value
links: Optional[List[Link]] = None
tax_provision_instance = TaxProvision(href=href, fund=fund, nav_type_code=nav_type_code, diary_entry_code=diary_entry_code, effective_at=effective_at, as_at=as_at, status=status, realised_gains=realised_gains, unrealised_gains=unrealised_gains, indexation_allowance=indexation_allowance, losses_brought_forward=losses_brought_forward, losses_used=losses_used, losses_carried_forward=losses_carried_forward, rate_applied=rate_applied, provision_amount=provision_amount, movement=movement, approved_by=approved_by, approved_at=approved_at, links=links)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

