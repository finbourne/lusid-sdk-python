# PricingMethodologyAudit

The working behind a share class's dealing price: the net cashflow it was decided on, the spread applied and  what the methodology alone proposed, with how any Market swing triggers were evaluated.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**net_cashflow** | **float** | The fund&#39;s net dealing cashflow for the valuation point, in the fund currency. An inflow is positive and an outflow negative. | 
**net_cashflow_pct_of_nav** | **float** | The net cashflow as a percentage of the previous valuation point&#39;s NAV. Absent when there is no previous NAV to measure it against. | [optional] 
**spreads_applied** | [**SwingSpreadApplied**](SwingSpreadApplied.md) |  | [optional] 
**engine_proposal** | [**PricingMethodologyEngineProposal**](PricingMethodologyEngineProposal.md) |  | 
**override** | [**PricingMethodologyOverride**](PricingMethodologyOverride.md) |  | [optional] 
**inflow_trigger** | [**SwingTriggerEvaluation**](SwingTriggerEvaluation.md) |  | [optional] 
**outflow_trigger** | [**SwingTriggerEvaluation**](SwingTriggerEvaluation.md) |  | [optional] 
**dealing_flows** | [**DealingFlowSummary**](DealingFlowSummary.md) |  | [optional] 
**estimate_valuation** | [**EstimateValuation**](EstimateValuation.md) |  | [optional] 
**approval_status** | **str** | Where a manually approved swing decision stands. Pending until a manager approves or overrides the engine&#39;s proposal, or when the proposal has changed since the decision was taken; Approved when the decision equals the proposal; Overridden when it differs. Absent when the swing policy approves automatically. | [optional] 
**dealing_lines_not_valued** | [**List[DealingLineNotValued]**](DealingLineNotValued.md) | The dealing lines read for the swing decision that could not be valued into the share class currency: an amount in a currency that is neither the fund&#39;s nor any share class&#39;s, or a weight-only line. While any are present and no pricingMethodologyOverride has been submitted, no swing decision is taken, the dealing price is absent and the valuation point cannot be finalised; under an override the override&#39;s price stands and the lines remain listed here. Absent when every line was valued or the methodology does not swing. | [optional] 
**completeness** | [**DealingBookCompleteness**](DealingBookCompleteness.md) |  | [optional] 
## Example

```python
from lusid.models.pricing_methodology_audit import PricingMethodologyAudit
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

net_cashflow: Union[StrictFloat, StrictInt] = # Replace with your value
net_cashflow_pct_of_nav: Optional[Union[StrictFloat, StrictInt]] = # Replace with your value
spreads_applied: Optional[SwingSpreadApplied] = # Replace with your value
engine_proposal: PricingMethodologyEngineProposal = # Replace with your value
override: Optional[PricingMethodologyOverride] = None
inflow_trigger: Optional[SwingTriggerEvaluation] = # Replace with your value
outflow_trigger: Optional[SwingTriggerEvaluation] = # Replace with your value
dealing_flows: Optional[DealingFlowSummary] = # Replace with your value
estimate_valuation: Optional[EstimateValuation] = # Replace with your value
approval_status: Optional[StrictStr] = "example_approval_status"
dealing_lines_not_valued: Optional[List[DealingLineNotValued]] = # Replace with your value
completeness: Optional[DealingBookCompleteness] = None
pricing_methodology_audit_instance = PricingMethodologyAudit(net_cashflow=net_cashflow, net_cashflow_pct_of_nav=net_cashflow_pct_of_nav, spreads_applied=spreads_applied, engine_proposal=engine_proposal, override=override, inflow_trigger=inflow_trigger, outflow_trigger=outflow_trigger, dealing_flows=dealing_flows, estimate_valuation=estimate_valuation, approval_status=approval_status, dealing_lines_not_valued=dealing_lines_not_valued, completeness=completeness)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

