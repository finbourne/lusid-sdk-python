# coding: utf-8

"""
    LUSID API

    FINBOURNE Technology  # noqa: E501

    Contact: info@finbourne.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


import json
import pprint
import re  # noqa: F401
from aenum import Enum, no_arg





class InstrumentEventType(str, Enum):
    """
    The individual event types.
    """

    """
    allowed enum values
    """
    TRANSITIONEVENT = 'TransitionEvent'
    INFORMATIONALEVENT = 'InformationalEvent'
    OPENEVENT = 'OpenEvent'
    CLOSEEVENT = 'CloseEvent'
    STOCKSPLITEVENT = 'StockSplitEvent'
    BONDDEFAULTEVENT = 'BondDefaultEvent'
    CASHDIVIDENDEVENT = 'CashDividendEvent'
    AMORTISATIONEVENT = 'AmortisationEvent'
    CASHFLOWEVENT = 'CashFlowEvent'
    EXERCISEEVENT = 'ExerciseEvent'
    RESETEVENT = 'ResetEvent'
    TRIGGEREVENT = 'TriggerEvent'
    RAWVENDOREVENT = 'RawVendorEvent'
    INFORMATIONALERROREVENT = 'InformationalErrorEvent'
    BONDCOUPONEVENT = 'BondCouponEvent'
    DIVIDENDREINVESTMENTEVENT = 'DividendReinvestmentEvent'
    ACCUMULATIONEVENT = 'AccumulationEvent'
    BONDPRINCIPALEVENT = 'BondPrincipalEvent'
    DIVIDENDOPTIONEVENT = 'DividendOptionEvent'
    MATURITYEVENT = 'MaturityEvent'
    FXFORWARDSETTLEMENTEVENT = 'FxForwardSettlementEvent'
    EXPIRYEVENT = 'ExpiryEvent'
    SCRIPDIVIDENDEVENT = 'ScripDividendEvent'
    STOCKDIVIDENDEVENT = 'StockDividendEvent'
    REVERSESTOCKSPLITEVENT = 'ReverseStockSplitEvent'
    CAPITALDISTRIBUTIONEVENT = 'CapitalDistributionEvent'
    SPINOFFEVENT = 'SpinOffEvent'
    MERGEREVENT = 'MergerEvent'
    FUTUREEXPIRYEVENT = 'FutureExpiryEvent'
    SWAPCASHFLOWEVENT = 'SwapCashFlowEvent'
    SWAPPRINCIPALEVENT = 'SwapPrincipalEvent'
    CREDITPREMIUMCASHFLOWEVENT = 'CreditPremiumCashFlowEvent'
    CDSCREDITEVENT = 'CdsCreditEvent'
    CDXCREDITEVENT = 'CdxCreditEvent'
    MBSCOUPONEVENT = 'MbsCouponEvent'
    MBSPRINCIPALEVENT = 'MbsPrincipalEvent'
    BONUSISSUEEVENT = 'BonusIssueEvent'
    MBSPRINCIPALWRITEOFFEVENT = 'MbsPrincipalWriteOffEvent'
    MBSINTERESTDEFERRALEVENT = 'MbsInterestDeferralEvent'
    MBSINTERESTSHORTFALLEVENT = 'MbsInterestShortfallEvent'
    TENDEREVENT = 'TenderEvent'
    CALLONINTERMEDIATESECURITIESEVENT = 'CallOnIntermediateSecuritiesEvent'
    INTERMEDIATESECURITIESDISTRIBUTIONEVENT = 'IntermediateSecuritiesDistributionEvent'
    OPTIONEXERCISEPHYSICALEVENT = 'OptionExercisePhysicalEvent'
    OPTIONEXERCISECASHEVENT = 'OptionExerciseCashEvent'
    PROTECTIONPAYOUTCASHFLOWEVENT = 'ProtectionPayoutCashFlowEvent'
    TERMDEPOSITINTERESTEVENT = 'TermDepositInterestEvent'
    TERMDEPOSITPRINCIPALEVENT = 'TermDepositPrincipalEvent'
    EARLYREDEMPTIONEVENT = 'EarlyRedemptionEvent'
    FUTUREMARKTOMARKETEVENT = 'FutureMarkToMarketEvent'
    ADJUSTGLOBALCOMMITMENTEVENT = 'AdjustGlobalCommitmentEvent'
    CONTRACTINITIALISATIONEVENT = 'ContractInitialisationEvent'
    DRAWDOWNEVENT = 'DrawdownEvent'
    LOANINTERESTREPAYMENTEVENT = 'LoanInterestRepaymentEvent'
    UPDATEDEPOSITAMOUNTEVENT = 'UpdateDepositAmountEvent'
    LOANPRINCIPALREPAYMENTEVENT = 'LoanPrincipalRepaymentEvent'
    DEPOSITINTERESTPAYMENTEVENT = 'DepositInterestPaymentEvent'
    DEPOSITCLOSEEVENT = 'DepositCloseEvent'
    LOANFACILITYCONTRACTROLLOVEREVENT = 'LoanFacilityContractRolloverEvent'
    REPURCHASEOFFEREVENT = 'RepurchaseOfferEvent'
    REPOPARTIALCLOSUREEVENT = 'RepoPartialClosureEvent'
    REPOCASHFLOWEVENT = 'RepoCashFlowEvent'
    FLEXIBLEREPOINTERESTPAYMENTEVENT = 'FlexibleRepoInterestPaymentEvent'
    FLEXIBLEREPOCASHFLOWEVENT = 'FlexibleRepoCashFlowEvent'
    FLEXIBLEREPOCOLLATERALEVENT = 'FlexibleRepoCollateralEvent'
    CONVERSIONEVENT = 'ConversionEvent'

    @classmethod
    def from_json(cls, json_str: str) -> InstrumentEventType:
        """Create an instance of InstrumentEventType from a JSON string"""
        return InstrumentEventType(json.loads(json_str))
