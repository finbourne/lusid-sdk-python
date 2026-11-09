# TaxClassification

The UK life-company tax classification of one instrument at one effective and asAt point.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**href** | **str** | The specific Uniform Resource Identifier (URI) for this resource at the requested effective and asAt datetime. | [optional] 
**luid** | **str** | The LUSID instrument identifier of the classified instrument. | 
**instrument_name** | **str** | The name of the classified instrument. | [optional] 
**instrument_type** | **str** | The LUSID instrument type of the classified instrument, where known. | [optional] 
**within_blagab** | **bool** | Whether the instrument is held within the basic life assurance and general annuity business of the fund. Absent when the input has not been set. | [optional] 
**inputs** | [**TaxClassificationInputs**](TaxClassificationInputs.md) |  | 
**treatment_override** | **str** | The user-supplied treatment leaf that replaces the system-derived one, if any. Available values: OutsideBlagab, LoanRelationship, IndexLinkedGilt, PrivateEquity, RealEstate, FinancialFuture, PooledDerivative, DerivativeProfitAndLoss, NonTransparentScheme, BondFund, TransparentScheme, StandardEquity, Exempt. | [optional] 
**leaf** | **str** | The treatment leaf the decision tree arrived at. Absent when the instrument could not be classified. Available values: OutsideBlagab, LoanRelationship, IndexLinkedGilt, PrivateEquity, RealEstate, FinancialFuture, PooledDerivative, DerivativeProfitAndLoss, NonTransparentScheme, BondFund, TransparentScheme, StandardEquity, Exempt. | [optional] 
**treatment** | **str** | The tax treatment class implied by the leaf: ChargeableGains, LoanRelationship, Excluded or Unclassified. Available values: ChargeableGains, LoanRelationship, Excluded, Unclassified. | 
**status** | **str** | Classified, Overridden, Rejected or Unclassified. Available values: Classified, Overridden, Rejected, Unclassified. | 
**source** | **str** | Whether the leaf came from the System decision tree or a User override. Available values: System, User. | 
**rule_fired** | **str** | The name of the decision-tree rule that produced the leaf. | 
**trace** | [**List[TaxClassificationDecisionStep]**](TaxClassificationDecisionStep.md) | The ordered questions the decision tree asked and the answers it took, for audit. | [optional] 
**exception** | [**TaxClassificationException**](TaxClassificationException.md) |  | [optional] 
**effective_at** | **datetime** | The effective date the classification was evaluated at. | 
**as_at** | **datetime** | The asAt time the classification was evaluated at. | 
**links** | [**List[Link]**](Link.md) |  | [optional] 
## Example

```python
from lusid.models.tax_classification import TaxClassification
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

href: Optional[StrictStr] = "example_href"
luid: StrictStr = "example_luid"
instrument_name: Optional[StrictStr] = "example_instrument_name"
instrument_type: Optional[StrictStr] = "example_instrument_type"
within_blagab: Optional[StrictBool] = # Replace with your value
within_blagab:Optional[StrictBool] = None
inputs: TaxClassificationInputs
treatment_override: Optional[StrictStr] = "example_treatment_override"
leaf: Optional[StrictStr] = "example_leaf"
treatment: StrictStr = "example_treatment"
status: StrictStr = "example_status"
source: StrictStr = "example_source"
rule_fired: StrictStr = "example_rule_fired"
trace: Optional[List[TaxClassificationDecisionStep]] = # Replace with your value
exception: Optional[TaxClassificationException] = None
effective_at: datetime = # Replace with your value
as_at: datetime = # Replace with your value
links: Optional[List[Link]] = None
tax_classification_instance = TaxClassification(href=href, luid=luid, instrument_name=instrument_name, instrument_type=instrument_type, within_blagab=within_blagab, inputs=inputs, treatment_override=treatment_override, leaf=leaf, treatment=treatment, status=status, source=source, rule_fired=rule_fired, trace=trace, exception=exception, effective_at=effective_at, as_at=as_at, links=links)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

