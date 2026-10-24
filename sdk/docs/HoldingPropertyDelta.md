# HoldingPropertyDelta

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**holding_property_key** | **str** | The running balance on the holding to adjust. Allowed values: &#39;CommittedCapital&#39;, &#39;UncalledCommitment&#39;, &#39;PaidInCapital&#39;, &#39;ReturnedCapital&#39;, &#39;RecallableCapital&#39;, &#39;NonRecallableCapital&#39;, &#39;ExcessCapitalReturned&#39;, &#39;PaidInCapitalPortfolioCcy&#39;, &#39;ReturnedCapitalPortfolioCcy&#39;, &#39;ExcessCapitalReturnedPortfolioCcy&#39;, &#39;FundedCapital&#39; and &#39;UnfundedCapital&#39;. The &#39;...PortfolioCcy&#39; balances are the same balances in the portfolio&#39;s base currency, each movement converted at its own RateToPortfolio on the day it was booked and never re-translated at a later spot rate; source them from &#39;PortfolioAmount&#39;. &#39;ExcessCapitalReturned&#39; is the cumulative excess capital the fund has handed back, kept separately because a return of excess lowers PaidInCapital and restores UncalledCommitment at the same time. &#39;UnfundedCapital&#39; is a deprecated alias of &#39;UncalledCommitment&#39;; &#39;FundedCapital&#39; is served as PaidInCapital less ReturnedCapital and new configuration should target those two instead. Available values: CommittedCapital, FundedCapital, UnfundedCapital, RecallableCapital, NonRecallableCapital, PaidInCapital, ReturnedCapital, UncalledCommitment, ExcessCapitalReturned, PaidInCapitalPortfolioCcy, ReturnedCapitalPortfolioCcy, ExcessCapitalReturnedPortfolioCcy. | 
**source** | **str** | The movement value that sources the adjustment. Allowed values: &#39;Amount&#39; (the movement&#39;s signed amount in transaction currency), &#39;Units&#39; (the movement&#39;s signed units), &#39;PortfolioAmount&#39; (the movement&#39;s signed amount converted to portfolio currency) and &#39;ProportionOfBalance&#39; (the movement&#39;s amount is read as a proportion between 0 and 1 of the balance already held under the key, and the adjustment is that proportion of the balance rounded to the holding currency&#39;s minor unit). &#39;PortfolioAmount&#39; is accepted only on the &#39;...PortfolioCcy&#39; keys, which are kept in the portfolio&#39;s base currency; &#39;Units&#39; is not accepted on any key. Available values: Amount, Units, PortfolioAmount, ProportionOfBalance. | 
**direction** | **str** | Whether the sourced value increases or decreases the balance. Allowed values: &#39;Increase&#39; and &#39;Decrease&#39;. Available values: Increase, Decrease. | 
## Example

```python
from lusid.models.holding_property_delta import HoldingPropertyDelta
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

holding_property_key: StrictStr = "example_holding_property_key"
source: StrictStr = "example_source"
direction: StrictStr = "example_direction"
holding_property_delta_instance = HoldingPropertyDelta(holding_property_key=holding_property_key, source=source, direction=direction)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

