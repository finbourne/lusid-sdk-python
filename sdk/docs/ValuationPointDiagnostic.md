# ValuationPointDiagnostic

Something found while striking a valuation point that did not stop it but should be looked at.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | What kind of finding this is. &#39;OwnershipDrift&#39;: a fund structure holder&#39;s declared sharing percentage in a held member differs from the share its contributions make of that member&#39;s capital by enough to misallocate more of the period&#39;s P&amp;L than the holder&#39;s drift materiality warning amount allows. &#39;FeeStrikeFailed&#39;: the fees struck when the valuation point was last created or updated failed, so its lines carry no fee transactions and it cannot be accepted until they are struck again. &#39;FeeInvoiceOutsideTolerance&#39;: the invoices booked for a fee in the valuation point&#39;s window, tagged with a Transaction/&lt;fund scope&gt;/InvoicedFeeCode property, differ from the fee&#39;s accrual for the period they cover by more than its Fee/&lt;scope&gt;/InvoiceTolerance, or else its fund&#39;s Fund/&lt;scope&gt;/InvoiceTolerance, allows; they are booked as they are. &#39;FeeInvoiceNotChecked&#39;: such an invoice could not be checked, because no final valuation point holds its period&#39;s accrual, it is not in the fee&#39;s currency, or the tolerance cannot be read. Neither stops the valuation point. &#39;PrepaidFeeSplitStale&#39;: a partnership fund&#39;s prepaid management fee period that ended more than 366 days before the valuation point, outside the year its valuation points re-split, had a transaction other than a fee booked, amended or cancelled in it since its split between the fee payable and the receivable from the manager was written, so the split may be out of date: re-split the period with the fund&#39;s fees/$resplit endpoint, which is post-close activity if the period is final. &#39;PrepaidFeeResplitFailed&#39;: a partnership fund&#39;s estimate could not re-split the prepaid management fee periods in its year when it was struck, so it was struck on their split as it stood and cannot be accepted until they are re-split: correct the cause and strike the estimate again. | 
**message** | **str** | What was found and what to do about it. | 
**details** | **Dict[str, Optional[str]]** | The values the finding was made on, by name. For &#39;OwnershipDrift&#39;: holder, member, declaredShare, actualShare, delta (actual less declared) and impact (the P&amp;L the drift would misallocate this period). For &#39;FeeStrikeFailed&#39;: failureType and failureMessage, the cause of the failed strike. For &#39;FeeInvoiceOutsideTolerance&#39;: feeCode, feeName, periodEnd (the payable date ending the period), accrualValuationPoint, currency, accrual, invoice, difference (invoice less accrual), differencePercent, tolerancePercent, toleranceFloor, tolerance (the larger of the percentage of the accrual and the floor), toleranceProperty and transactionIds. For &#39;FeeInvoiceNotChecked&#39;: feeCode, feeName, reason (AccrualNotFound, CurrencyMismatch or ToleranceUnreadable), transactionIds, and the figures it was found on. For &#39;PrepaidFeeSplitStale&#39;: prepaidRunId, periodStart, periodEnd and transactionIds (the transactions changed in the period since its split was written). For &#39;PrepaidFeeResplitFailed&#39;: failureType and failureMessage, the cause of the failed re-split. | [optional] 
## Example

```python
from lusid.models.valuation_point_diagnostic import ValuationPointDiagnostic
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

type: StrictStr = "example_type"
message: StrictStr = "example_message"
details: Optional[Dict[str, Optional[StrictStr]]] = # Replace with your value
valuation_point_diagnostic_instance = ValuationPointDiagnostic(type=type, message=message, details=details)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

