from db import *
import pandas as pd # type: ignore
import streamlit as st # type: ignore
import plotly.express as px # type: ignore
import plotly.graph_objects as go # type: ignore
from datetime import datetime


# 2025 US Federal Tax Brackets (Single Filer)
TAX_BRACKETS_SINGLE = [
    (11925, 0.10),      # 10% on income up to $11,925
    (48475, 0.12),      # 12% on income from $11,926 to $48,475
    (103350, 0.22),      # 22% on income from $48,476 to $103,350
    (197300, 0.24),     # 24% on income from $103,351 to $197,300
    (250525, 0.32),     # 32% on income from $197,301 to $250,525
    (626350, 0.35),     # 35% on income from $250,526 to $626,350
    (float('inf'), 0.37) # 37% on income over $626,350
]

# 2025 US Federal Tax Brackets (Married Filer)
TAX_BRACKETS_MARRIED = [
    (23850, 0.10),      # 10% on income up to $23,850
    (96950, 0.12),      # 12% on income from $23,851 to $96,950
    (206700, 0.22),      # 22% on income from $96,951 to $206,700
    (394600, 0.24),     # 24% on income from $206,701 to $394,600
    (501050, 0.32),     # 32% on income from $394,601 to $501,050
    (751600, 0.35),     # 35% on income from $501,051 to $751,600
    (float('inf'), 0.37) # 37% on income over $751,600
]

# Standard deduction for 2025
STANDARD_DEDUCTION_SINGLE = 15000
STANDARD_DEDUCTION_MARRIED = 30000

# Indiana State Tax Information (2025)
INDIANA_STATE_TAX = {
    'rate': 0.0411,  # Indiana has a flat 3.0% state income tax rate + 1.11% County Income Tax
    'exemption_single': 1000,
    'exemption_married': 2000,
    'exemption_dependent': 1500
}


def get_latest_year():
    """Get the latest year from income data."""
    query = "SELECT MAX(EXTRACT(YEAR FROM source_date)) FROM income"
    result = run_query(query)
    return int(result[0][0]) if result and result[0][0] else datetime.now().year


def get_investment_income(year):
    """Get investment income for NIIT calculation."""
    query = """
        SELECT 
            SUM(amount) as total_investment_income
        FROM income 
        WHERE EXTRACT(YEAR FROM source_date) = %s
        AND category = 'passive_income'
    """
    result = run_query(query, (year,))
    
    investment_income = 0
    if result and result[0][0]:
        investment_income = float(result[0][0])
    
    return investment_income


def get_preferential_income(year):
    """Get qualifying dividends and long-term capital gains for preferential tax treatment."""
    query = """
        SELECT 
            source,
            SUM(amount) as total_amount
        FROM income 
        WHERE EXTRACT(YEAR FROM source_date) = %s
        AND source IN ('qualifying_dividends', 'long_term_gains')
        GROUP BY source
    """
    result = run_query(query, (year,))
    
    qualifying_dividends = 0
    long_term_gains = 0
    
    if result:
        for row in result:
            source, amount = row
            if source == 'qualifying_dividends':
                qualifying_dividends = float(amount)
            elif source == 'long_term_gains':
                long_term_gains = float(amount)
    
    return qualifying_dividends, long_term_gains


def get_total_income(year):
    """Get total income for a given year."""
    query = """
        SELECT 
            category,
            SUM(amount) as total_amount,
            COUNT(*) as transaction_count
        FROM income 
        WHERE EXTRACT(YEAR FROM source_date) = 2025
        GROUP BY category
        ORDER BY total_amount DESC
    """
    result = run_query(query, (year,))
    
    total_income = 0
    income_breakdown = []
    
    if result:
        for row in result:
            category, amount, count = row
            total_income += float(amount)
            income_breakdown.append({
                'category': category.replace('_', ' ').title(),
                'amount': float(amount),
                'count': count
            })
    
    return total_income, income_breakdown


def get_potential_deductions(year):
    """Get potential tax deductions from expense data."""
    # Common deductible expenses mapping
    deductible_categories = {
        'mortgage_interest': ['mortgage', 'interest'],
        'property_tax': ['property_tax', 'property tax'],
        'charitable_donations': ['charity', 'donation', 'charitable'],
        'medical_expenses': ['medical', 'health', 'dental', 'vision'],
        'business_expenses': ['business', 'office', 'professional']
    }
    
    query = """
        SELECT 
            source,
            SUM(amount) as total_amount
        FROM expense 
        WHERE EXTRACT(YEAR FROM source_date) = %s
        GROUP BY source
        ORDER BY total_amount DESC
    """
    result = run_query(query, (year,))
    
    deductions = {
        'mortgage_interest': 0,
        'property_tax': 0,
        'charitable_donations': 0,
        'medical_expenses': 0,
        'business_expenses': 0,
        'other': 0
    }
    
    unmatched_expenses = []
    
    if result:
        for row in result:
            source, amount = row
            source_lower = source.lower()
            matched = False
            
            for deduction_type, keywords in deductible_categories.items():
                if any(keyword in source_lower for keyword in keywords):
                    deductions[deduction_type] += float(amount)
                    matched = True
                    break
            
            if not matched:
                unmatched_expenses.append({
                    'source': source,
                    'amount': float(amount)
                })
    
    return deductions, unmatched_expenses


def calculate_federal_tax(taxable_income, filing_status='married', gross_income=None, investment_income=None, qualifying_dividends=0, long_term_gains=0):
    """Calculate federal tax including income tax, Social Security, Medicare, and Net Investment Income taxes based on 2025 rates."""
    if filing_status == 'single':
        brackets = TAX_BRACKETS_SINGLE
    else:
        brackets = TAX_BRACKETS_MARRIED
    
    # Use gross_income for payroll taxes if provided, otherwise use taxable_income
    wages_for_payroll = gross_income if gross_income is not None else taxable_income
    
    # Preferential Income Tax Calculation (15% rate for qualified dividends and long-term gains)
    total_preferential_income = qualifying_dividends + long_term_gains
    preferential_tax_rate = 0.15
    preferential_income_tax = total_preferential_income * preferential_tax_rate
    
    # Federal Income Tax Calculation (ordinary income only)
    # Subtract preferential income from taxable income for ordinary tax calculation
    ordinary_taxable_income = max(0, taxable_income - total_preferential_income)
    income_tax = 0
    remaining_income = ordinary_taxable_income
    previous_bracket = 0
    
    income_tax_breakdown = []
    
    for bracket_limit, rate in brackets:
        if remaining_income <= 0:
            break
            
        taxable_at_bracket = min(remaining_income, bracket_limit - previous_bracket)
        tax_at_bracket = taxable_at_bracket * rate
        income_tax += tax_at_bracket
        
        if taxable_at_bracket > 0:
            income_tax_breakdown.append({
                'bracket': f"${previous_bracket:,} - ${bracket_limit:,}" if bracket_limit != float('inf') else f"${previous_bracket:,}+",
                'rate': f"{rate:.1%}",
                'taxable_income': taxable_at_bracket,
                'tax_amount': tax_at_bracket,
                'tax_type': 'Federal Income Tax (Ordinary)'
            })
        
        remaining_income -= taxable_at_bracket
        previous_bracket = bracket_limit
        
        if bracket_limit == float('inf'):
            break
    
    # Add preferential income tax to breakdown
    if total_preferential_income > 0:
        income_tax_breakdown.append({
            'bracket': f"Preferential Income",
            'rate': f"{preferential_tax_rate:.1%}",
            'taxable_income': total_preferential_income,
            'tax_amount': preferential_income_tax,
            'tax_type': 'Federal Income Tax (Preferential)'
        })
    
    # Total income tax (ordinary + preferential)
    total_income_tax = income_tax + preferential_income_tax
    
    # Social Security Tax (6.2% on wages up to $168,600 for 2025)
    social_security_wage_base = 176100  # 2025 wage base
    social_security_rate = 0.062
    social_security_taxable = min(wages_for_payroll, social_security_wage_base)
    social_security_tax = social_security_taxable * social_security_rate
    
    # Medicare Tax (1.45% on all wages)
    medicare_rate = 0.0145
    medicare_tax = wages_for_payroll * medicare_rate
    
    # Additional Medicare Tax (0.9% on wages over threshold)
    additional_medicare_threshold = 250000 if filing_status == 'married' else 200000
    additional_medicare_rate = 0.009
    additional_medicare_tax = 0
    
    if wages_for_payroll > additional_medicare_threshold:
        additional_medicare_taxable = wages_for_payroll - additional_medicare_threshold
        additional_medicare_tax = additional_medicare_taxable * additional_medicare_rate
    
    # Total Medicare Tax
    total_medicare_tax = medicare_tax + additional_medicare_tax
    
    # Net Investment Income Tax (3.8% on investment income for high earners)
    niit_rate = 0.038
    niit_threshold = 250000 if filing_status == 'married' else 200000
    niit_tax = 0
    niit_taxable_income = 0
    
    if investment_income and investment_income > 0:
        # NIIT applies to the lesser of:
        # 1. Net investment income, or
        # 2. The amount by which MAGI exceeds the threshold
        magi = gross_income if gross_income else taxable_income  # Simplified MAGI calculation
        
        if magi > niit_threshold:
            excess_magi = magi - niit_threshold
            niit_taxable_income = min(investment_income, excess_magi)
            niit_tax = niit_taxable_income * niit_rate
    
    # Payroll Tax Breakdown
    payroll_breakdown = []
    
    if social_security_tax > 0:
        payroll_breakdown.append({
            'bracket': f"Up to ${social_security_wage_base:,}",
            'rate': f"{social_security_rate:.2%}",
            'taxable_income': social_security_taxable,
            'tax_amount': social_security_tax,
            'tax_type': 'Social Security'
        })
    
    if medicare_tax > 0:
        payroll_breakdown.append({
            'bracket': "All wages",
            'rate': f"{medicare_rate:.2%}",
            'taxable_income': wages_for_payroll,
            'tax_amount': medicare_tax,
            'tax_type': 'Medicare'
        })
    
    if additional_medicare_tax > 0:
        payroll_breakdown.append({
            'bracket': f"Over ${additional_medicare_threshold:,}",
            'rate': f"{additional_medicare_rate:.2%}",
            'taxable_income': additional_medicare_taxable,
            'tax_amount': additional_medicare_tax,
            'tax_type': 'Additional Medicare'
        })
    
    if niit_tax > 0:
        payroll_breakdown.append({
            'bracket': f"Investment income over ${niit_threshold:,} MAGI",
            'rate': f"{niit_rate:.1%}",
            'taxable_income': niit_taxable_income,
            'tax_amount': niit_tax,
            'tax_type': 'Net Investment Income Tax'
        })
    
    # Combined breakdown
    tax_breakdown = income_tax_breakdown + payroll_breakdown
    
    # Total federal taxes
    total_federal_tax = total_income_tax + social_security_tax + total_medicare_tax + niit_tax
    
    return total_federal_tax, tax_breakdown, {
        'income_tax': total_income_tax,
        'ordinary_income_tax': income_tax,
        'preferential_income_tax': preferential_income_tax,
        'social_security_tax': social_security_tax,
        'medicare_tax': medicare_tax,
        'additional_medicare_tax': additional_medicare_tax,
        'total_medicare_tax': total_medicare_tax,
        'niit_tax': niit_tax,
        'total_payroll_tax': social_security_tax + total_medicare_tax,
        'total_other_taxes': niit_tax,
        'total_non_income_tax': social_security_tax + total_medicare_tax + niit_tax
    }


def calculate_indiana_state_tax(taxable_income, filing_status='married', property_tax_deduction=0, plan_529_deduction=0):
    """Calculate Indiana state tax based on flat rate plus exemptions and Indiana-specific deductions."""
    # Indiana uses a flat rate with exemptions
    if filing_status == 'married':
        exemption = INDIANA_STATE_TAX['exemption_married']
    else:
        exemption = INDIANA_STATE_TAX['exemption_single']
    
    # Apply Indiana-specific deductions
    total_indiana_deductions = exemption + property_tax_deduction + plan_529_deduction
    
    # Apply exemption and Indiana deductions
    taxable_after_exemption_and_deductions = max(0, taxable_income)
    
    # Calculate tax at flat rate
    state_tax = taxable_after_exemption_and_deductions * INDIANA_STATE_TAX['rate']
    
    tax_breakdown = []
    if state_tax > 0 or total_indiana_deductions > 0:
        tax_breakdown.append({
            'bracket': f"All Income",
            'rate': f"{INDIANA_STATE_TAX['rate']:.2%}",
            'taxable_income': taxable_after_exemption_and_deductions,
            'tax_amount': state_tax,
            'exemption': exemption,
            'property_tax_deduction': property_tax_deduction,
            'plan_529_deduction': plan_529_deduction,
            'total_indiana_deductions': total_indiana_deductions
        })
    
    return state_tax, tax_breakdown


def get_taxes_paid(year):
    """Get actual taxes paid from expense data, separated by federal and state."""
    query = """
        SELECT 
            source,
            SUM(amount) as total_amount
        FROM expense 
        WHERE EXTRACT(YEAR FROM source_date) = %s 
        AND source IN ('federal_income_tax_person1', 'federal_income_tax_person2', 
                       'state_income_tax_person1', 'state_income_tax_person2', 
                       'medicare_person1', 'medicare_person2', 
                       'social_security_person1', 'social_security_person2')
        GROUP BY source
        ORDER BY total_amount DESC
    """
    result = run_query(query, (year,))
    
    federal_paid = 0
    federal_refund_eligible_paid = 0  # Only income tax, additional medicare, NIIT
    state_paid = 0
    federal_payments = []
    state_payments = []
    
    # Define which sources are federal vs state
    federal_sources = ['federal_income_tax_person1', 'federal_income_tax_person2', 
                      'medicare_person1', 'medicare_person2', 
                      'social_security_person1', 'social_security_person2']
    # Sources eligible for refund calculation (exclude regular medicare and social security)
    federal_refund_eligible_sources = ['federal_income_tax_person1', 'federal_income_tax_person2']
    state_sources = ['state_income_tax_person1', 'state_income_tax_person2']
    
    if result:
        for row in result:
            source, amount = row
            
            payment_info = {
                'source': source.replace('_', ' ').title(),
                'amount': float(amount)
            }
            
            if source in federal_sources:
                federal_paid += float(amount)
                federal_payments.append(payment_info)
                
                # Only include income tax payments for refund calculation
                if source in federal_refund_eligible_sources:
                    federal_refund_eligible_paid += float(amount)
                    
            elif source in state_sources:
                state_paid += float(amount)
                state_payments.append(payment_info)
    
    return {
        'federal': {
            'total': federal_paid, 
            'refund_eligible_total': federal_refund_eligible_paid,
            'payments': federal_payments
        },
        'state': {'total': state_paid, 'payments': state_payments}
    }


def get_refund_eligible_federal_tax(federal_tax_components):
    """Calculate federal tax eligible for refund (income tax + additional medicare + NIIT only)."""
    return (federal_tax_components['income_tax'] + 
            federal_tax_components['additional_medicare_tax'] + 
            federal_tax_components['niit_tax'])


def get_529_contributions(year):
    """Get 529 plan contributions for Indiana state tax deduction."""
    query = """
        SELECT 
            SUM(amount) as total_529_contributions
        FROM expense 
        WHERE EXTRACT(YEAR FROM source_date) = %s
        AND source = 'edu_529'
    """
    result = run_query(query, (year,))
    
    total_529 = 0
    if result and result[0][0]:
        total_529 = float(result[0][0])
    
    return total_529


def display_tax_calculator(filing_status='married', paidPropertyTax=True):
    """Display the tax calculation component with separate federal and Indiana state calculations."""
    
    st.write("### 🧮 Tax Calculator & Analysis")
    
    # Get latest year
    latest_year = get_latest_year()
    
    # Get basic data for calculations
    total_income, income_breakdown = get_total_income(latest_year)
    deductions, unmatched_expenses = get_potential_deductions(latest_year)
    investment_income = get_investment_income(latest_year)
    qualifying_dividends, long_term_gains = get_preferential_income(latest_year)
    
    # Calculate additional pre-tax deductions
    query_pretax = """
        SELECT 
            source,
            SUM(amount) as total_amount
        FROM expense 
        WHERE EXTRACT(YEAR FROM source_date) = %s
        AND source IN ('401k_person1', '401k_person2', 'HSA', 'health_insurance')
        GROUP BY source
        ORDER BY total_amount DESC
    """
    result_pretax = run_query(query_pretax, (latest_year,))
    
    # Initialize pre-tax contribution variables
    _401k_contribution = 0
    health_insurance_payment = 0
    hsa_contribution = 0
    
    if result_pretax:
        for row in result_pretax:
            source, amount = row
            
            # 401k contributions (both person1 and person2)
            if source in ['401k_person1', '401k_person2']:
                _401k_contribution += float(amount)
            
            # Health insurance premiums (pre-tax)
            elif source == 'health_insurance':
                health_insurance_payment += float(amount)
            
            # HSA contributions
            elif source == 'HSA':
                hsa_contribution += float(amount)
    
    # Calculate federal deductions
    total_itemized = sum(deductions.values())
    federal_standard = STANDARD_DEDUCTION_MARRIED if filing_status == 'married' else STANDARD_DEDUCTION_SINGLE
    use_standard_federal = total_itemized < federal_standard
    federal_deduction_amount = max(total_itemized, federal_standard)
    
    # Calculate federal taxable income and tax
    federal_taxable_income = max(0, total_income - federal_deduction_amount - _401k_contribution - health_insurance_payment - hsa_contribution)
    federal_estimated_tax, federal_tax_breakdown, federal_tax_components = calculate_federal_tax(federal_taxable_income, filing_status, federal_taxable_income+federal_deduction_amount, investment_income, qualifying_dividends, long_term_gains)
    
    # Calculate Indiana state deductions and taxable income
    indiana_standard = INDIANA_STATE_TAX['exemption_married'] if filing_status == 'married' else INDIANA_STATE_TAX['exemption_single']
    state_deduction_amount = indiana_standard
    
    # Calculate Indiana-specific deductions
    # Property tax deduction: $2500 if paidPropertyTax is True
    property_tax_deduction = 2500 if paidPropertyTax else 0
    
    # 529 plan deduction: min of 20% of contributions or $1500
    total_529_contributions = get_529_contributions(latest_year)
    plan_529_deduction = min(total_529_contributions * 0.20, 1500) if total_529_contributions > 0 else 0
    
    state_taxable_income = max(0, total_income - state_deduction_amount - _401k_contribution - health_insurance_payment - hsa_contribution - property_tax_deduction - plan_529_deduction)
    state_estimated_tax, state_tax_breakdown = calculate_indiana_state_tax(state_taxable_income, filing_status, property_tax_deduction, plan_529_deduction)
    
    # Get actual taxes paid (separated)
    taxes_paid_data = get_taxes_paid(latest_year)
    federal_paid = taxes_paid_data['federal']['total']
    federal_refund_eligible_paid = taxes_paid_data['federal']['refund_eligible_total']
    state_paid = taxes_paid_data['state']['total']
    federal_payments = taxes_paid_data['federal']['payments']
    state_payments = taxes_paid_data['state']['payments']
    
    # Calculate refund-eligible federal tax (income tax + additional medicare + NIIT only)
    federal_refund_eligible_estimated = get_refund_eligible_federal_tax(federal_tax_components)
    
    
    st.write(f"**Tax Year: {latest_year} | State: Indiana**")
    # Combined Summary
    # st.write("---")
    st.write("### 📊 Combined Tax Summary")
    st.caption("*Refund calculation includes: Federal Income Tax + Additional Medicare Tax + NIIT (excludes Social Security & regular Medicare)")
    
    # Use refund-eligible amounts for refund calculation
    total_estimated = federal_refund_eligible_estimated + state_estimated_tax
    total_paid = federal_refund_eligible_paid + state_paid
    total_difference = total_paid - total_estimated
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric("Total Income", f"${total_income:,.0f}")
    
    with col2:
        st.metric("Total Tax Estimated", f"${total_estimated:,.0f}")
    
    with col3:
        st.metric("Total Taxes Paid", f"${total_paid:,.0f}")
    
    with col4:
        if total_difference > 0:
            st.metric("Total Refund Expected", f"${total_difference:,.0f}", delta="Refund", delta_color="normal")
        elif total_difference < 0:
            st.metric("Total Amount Owed", f"${abs(total_difference):,.0f}", delta="Owed", delta_color="inverse")
        else:
            st.metric("Tax Status", "Balanced", delta="Even", delta_color="off")
    
    
    # Income and Deduction Analysis (shared for both federal and state)
    st.write("---")
    col1, col2 = st.columns(2)
    
    with col1:
        st.write("#### 💰 Income Summary")
        st.metric("Total Income", f"${total_income:,.0f}")
        
        # Show income details
        with st.expander("📋 Income Details"):
            for item in income_breakdown:
                st.write(f"**{item['category']}**: ${item['amount']:,.0f} ({item['count']} transactions)")
            
            # Show preferential income breakdown
            if qualifying_dividends > 0 or long_term_gains > 0:
                st.write("---")
                st.write("**Preferential Tax Rate Income (15%):**")
                if qualifying_dividends > 0:
                    st.write(f"• **Qualifying Dividends**: ${qualifying_dividends:,.0f}")
                if long_term_gains > 0:
                    st.write(f"• **Long-term Capital Gains**: ${long_term_gains:,.0f}")
                st.write(f"• **Total Preferential**: ${qualifying_dividends + long_term_gains:,.0f}")
    
    with col2:
        st.write("#### 📋 Federal Deductions")
        
        st.success(f"✅ Using {_401k_contribution:,.0f} as 401k deduction")
        st.success(f"✅ Using {health_insurance_payment:,.0f} as health insurance deduction")
        st.success(f"✅ Using {hsa_contribution:,.0f} as HSA deduction")
        
        if use_standard_federal:
            st.success(f"✅ Using Standard Deduction: ${federal_standard:,.0f}")
            federal_deduction_amount = federal_standard
        else:
            st.success(f"✅ Using Itemized Deductions: ${total_itemized:,.0f}")
            federal_deduction_amount = total_itemized
    

        # Show deduction breakdown
        with st.expander("🔍 Federal Deduction Details"):
            st.write(f"**Standard Deduction (2025)**: ${federal_standard:,.0f}")
            st.write(f"**Total Itemized**: ${total_itemized:,.0f}")
            st.write("---")
            
            for deduction_type, amount in deductions.items():
                if amount > 0:
                    st.write(f"**{deduction_type.replace('_', ' ').title()}**: ${amount:,.0f}")
    
    # Detailed Tax Analysis
    st.write("---")
    
    # Display tax calculations in columns
    col1, col2 = st.columns(2)
    
    with col1:
        st.write("#### 🇺🇸 Federal Taxes (Income + Payroll + NIIT)")
        st.caption("*Refund calculation excludes Social Security & regular Medicare taxes")
        
        # Federal metrics
        subcol1, subcol2 = st.columns(2)
        with subcol1:
            st.metric("Federal Taxable Income", f"${federal_taxable_income:,.0f}")
            st.metric("Total Federal Tax Estimated", f"${federal_estimated_tax:,.0f}")
            caption_parts = []
            if federal_tax_components['ordinary_income_tax'] > 0:
                caption_parts.append(f"Ordinary: ${federal_tax_components['ordinary_income_tax']:,.0f}")
            if federal_tax_components['preferential_income_tax'] > 0:
                caption_parts.append(f"Preferential: ${federal_tax_components['preferential_income_tax']:,.0f}")
            caption_parts.append(f"Payroll: ${federal_tax_components['total_payroll_tax']:,.0f}")
            if federal_tax_components['total_other_taxes'] > 0:
                caption_parts.append(f"NIIT: ${federal_tax_components['total_other_taxes']:,.0f}")
            st.caption(" | ".join(caption_parts))
        with subcol2:
            st.metric("Federal Taxes Paid", f"${federal_paid:,.0f}")
            st.caption(f"Refund eligible: ${federal_refund_eligible_paid:,.0f}")
            # Use refund-eligible amounts for refund calculation
            federal_difference = federal_refund_eligible_paid - federal_refund_eligible_estimated
            if federal_difference > 0:
                st.metric("Federal Refund", f"${federal_difference:,.0f}", delta="Refund", delta_color="normal")
            elif federal_difference < 0:
                st.metric("Federal Owed", f"${abs(federal_difference):,.0f}", delta="Owed", delta_color="inverse")
            else:
                st.metric("Federal Status", "Balanced", delta="Even", delta_color="off")
        
        # Federal tax breakdown
        with st.expander("📊 Federal Tax Breakdown"):
            if federal_tax_breakdown:
                # Group by tax type
                ordinary_income_tax_items = [item for item in federal_tax_breakdown if item.get('tax_type') == 'Federal Income Tax (Ordinary)']
                preferential_income_tax_items = [item for item in federal_tax_breakdown if item.get('tax_type') == 'Federal Income Tax (Preferential)']
                payroll_tax_items = [item for item in federal_tax_breakdown if item.get('tax_type') in ['Social Security', 'Medicare', 'Additional Medicare']]
                other_tax_items = [item for item in federal_tax_breakdown if item.get('tax_type') in ['Net Investment Income Tax']]
                
                # Display ordinary income tax brackets
                if ordinary_income_tax_items:
                    st.write("**Federal Income Tax (Ordinary Rates):**")
                    for row in ordinary_income_tax_items:
                        st.write(f"  • {row['bracket']} ({row['rate']}): ${row['tax_amount']:,.0f}")
                    st.write(f"  • **Total Ordinary Income Tax**: ${federal_tax_components['ordinary_income_tax']:,.0f}")
                
                # Display preferential income tax
                if preferential_income_tax_items:
                    st.write("**Federal Income Tax (Preferential Rates):**")
                    for row in preferential_income_tax_items:
                        st.write(f"  • {row['bracket']} ({row['rate']}): ${row['tax_amount']:,.0f}")
                    st.write(f"  • **Total Preferential Income Tax**: ${federal_tax_components['preferential_income_tax']:,.0f}")
                
                # Show combined income tax total
                if ordinary_income_tax_items or preferential_income_tax_items:
                    st.write(f"  • **Total Income Tax**: ${federal_tax_components['income_tax']:,.0f}")
                
                # Display payroll taxes
                if payroll_tax_items:
                    st.write("**Payroll Taxes:**")
                    for row in payroll_tax_items:
                        st.write(f"  • {row['tax_type']} ({row['rate']}): ${row['tax_amount']:,.0f}")
                    st.write(f"  • **Total Payroll Tax**: ${federal_tax_components['total_payroll_tax']:,.0f}")
                
                # Display other taxes (NIIT)
                if other_tax_items:
                    st.write("**Other Federal Taxes:**")
                    for row in other_tax_items:
                        st.write(f"  • {row['tax_type']} ({row['rate']}): ${row['tax_amount']:,.0f}")
                    if investment_income > 0:
                        st.write(f"  • **Investment Income**: ${investment_income:,.0f}")
                
                st.write("---")
                st.write(f"**Total Federal Taxes**: ${federal_estimated_tax:,.0f}")
                
                # Effective vs Marginal tax rate
                effective_rate = (federal_estimated_tax / total_income) * 100 if total_income > 0 else 0
                income_effective_rate = (federal_tax_components['income_tax'] / total_income) * 100 if total_income > 0 else 0
                payroll_effective_rate = (federal_tax_components['total_payroll_tax'] / total_income) * 100 if total_income > 0 else 0
                other_effective_rate = (federal_tax_components['total_other_taxes'] / total_income) * 100 if total_income > 0 else 0
                
                marginal_rate = ordinary_income_tax_items[-1]['rate'] if ordinary_income_tax_items else "0%"
                
                st.write("---")
                st.write(f"**Income Tax Effective Rate**: {income_effective_rate:.1f}%")
                st.write(f"**Payroll Tax Effective Rate**: {payroll_effective_rate:.1f}%")
                if other_effective_rate > 0:
                    st.write(f"**NIIT Effective Rate**: {other_effective_rate:.1f}%")
                st.write(f"**Total Effective Rate**: {effective_rate:.1f}%")
                st.write(f"**Marginal Income Tax Rate**: {marginal_rate}")
        
        # Federal payments made
        with st.expander("💳 Federal Tax Payments Made"):
            if federal_payments:
                for payment in federal_payments:
                    st.write(f"**{payment['source']}**: ${payment['amount']:,.0f}")
            else:
                st.write("No federal tax payments recorded.")
    
    with col2:
        st.write("#### 🏛️ Indiana State Taxes")
        
        indiana_deductions_summary = []
        indiana_deductions_summary.append(f"Standard Exemption: ${indiana_standard:,.0f}")

        # Show Indiana deductions summary
        if property_tax_deduction > 0 or plan_529_deduction > 0:    
            if property_tax_deduction > 0:
                indiana_deductions_summary.append(f"Property Tax: ${property_tax_deduction:,.0f}")
            if plan_529_deduction > 0:
                indiana_deductions_summary.append(f"529 Plan: ${plan_529_deduction:,.0f}")
        
        for deduction in indiana_deductions_summary:
            st.success(f"✅ Indiana Deductions: {deduction}")
        
        # State metrics
        subcol1, subcol2 = st.columns(2)
        with subcol1:
            st.metric("State Taxable Income", f"${state_taxable_income:,.0f}")
            st.metric("State Tax Estimated", f"${state_estimated_tax:,.0f}")
        with subcol2:
            st.metric("State Taxes Paid", f"${state_paid:,.0f}")
            state_difference = state_paid - state_estimated_tax
            if state_difference > 0:
                st.metric("State Refund", f"${state_difference:,.0f}", delta="Refund", delta_color="normal")
            elif state_difference < 0:
                st.metric("State Owed", f"${abs(state_difference):,.0f}", delta="Owed", delta_color="inverse")
            else:
                st.metric("State Status", "Balanced", delta="Even", delta_color="off")
        
        # Indiana state tax breakdown
        with st.expander("📊 Indiana State Tax Breakdown"):
            if state_tax_breakdown:
                for row in state_tax_breakdown:
                    st.write(f"**Tax Rate**: {row['rate']}")
                    st.write(f"**Exemption**: ${row['exemption']:,.0f}")
                    
                    # Show Indiana-specific deductions
                    if row.get('total_indiana_deductions', 0) > 0:
                        st.write("**Indiana Deductions:**")
                        if row.get('property_tax_deduction', 0) > 0:
                            st.write(f"  • Property Tax Deduction: ${row['property_tax_deduction']:,.0f}")
                        if row.get('plan_529_deduction', 0) > 0:
                            st.write(f"  • 529 Plan Deduction: ${row['plan_529_deduction']:,.0f}")
                            if total_529_contributions > 0:
                                st.write(f"    (20% of ${total_529_contributions:,.0f} contributions, max $1,500)")
                        st.write(f"  • **Total Indiana Deductions**: ${row['total_indiana_deductions']:,.0f}")
                    
                    st.write(f"**Taxable After Exemption & Deductions**: ${row['taxable_income']:,.0f}")
                    st.write(f"**Tax Amount**: ${row['tax_amount']:,.0f}")
                
                # State effective rate
                state_effective_rate = (state_estimated_tax / total_income) * 100 if total_income > 0 else 0
                
                st.write("---")
                st.write(f"**Indiana Effective Rate**: {state_effective_rate:.2f}%")
                st.write(f"**Indiana Flat Rate**: {INDIANA_STATE_TAX['rate']:.2%}")
        
        # State payments made
        with st.expander("💳 Indiana Tax Payments Made"):
            if state_payments:
                for payment in state_payments:
                    st.write(f"**{payment['source']}**: ${payment['amount']:,.0f}")
            else:
                st.write("No Indiana state tax payments recorded.")
    



def get_tax_summary_metrics(filing_status='married'):
    """Get summary metrics for tax overview with separated federal and Indiana state taxes."""
    latest_year = get_latest_year()
    total_income, _ = get_total_income(latest_year)
    investment_income = get_investment_income(latest_year)
    deductions, _ = get_potential_deductions(latest_year)
    total_itemized = sum(deductions.values())
    
    # Calculate additional pre-tax deductions (same as display_tax_calculator)
    query_pretax = """
        SELECT 
            source,
            SUM(amount) as total_amount
        FROM expense 
        WHERE EXTRACT(YEAR FROM source_date) = %s
        AND source IN ('401k_person1', '401k_person2', 'HSA', 'health_insurance')
        GROUP BY source
        ORDER BY total_amount DESC
    """
    result_pretax = run_query(query_pretax, (latest_year,))
    
    # Initialize pre-tax contribution variables
    _401k_contribution = 0
    health_insurance_payment = 0
    hsa_contribution = 0
    
    if result_pretax:
        for row in result_pretax:
            source, amount = row
            
            # 401k contributions (both person1 and person2)
            if source in ['401k_person1', '401k_person2']:
                _401k_contribution += float(amount)
            
            # Health insurance premiums (pre-tax)
            elif source == 'health_insurance':
                health_insurance_payment += float(amount)
            
            # HSA contributions
            elif source == 'HSA':
                hsa_contribution += float(amount)
    
    # Federal calculations
    federal_standard = STANDARD_DEDUCTION_MARRIED if filing_status == 'married' else STANDARD_DEDUCTION_SINGLE
    federal_deduction_amount = max(total_itemized, federal_standard)
    federal_taxable_income = max(0, total_income - federal_deduction_amount - _401k_contribution - health_insurance_payment - hsa_contribution)
    # Use same gross income calculation as display_tax_calculator
    gross_income_for_federal = federal_taxable_income + federal_deduction_amount
    qualifying_dividends, long_term_gains = get_preferential_income(latest_year)
    federal_estimated_tax, _, federal_tax_components = calculate_federal_tax(federal_taxable_income, filing_status, gross_income_for_federal, investment_income, qualifying_dividends, long_term_gains)
    
    # Indiana State calculations
    indiana_standard = INDIANA_STATE_TAX['exemption_married'] if filing_status == 'married' else INDIANA_STATE_TAX['exemption_single']
    state_deduction_amount = max(total_itemized, indiana_standard)
    
    # Calculate Indiana-specific deductions (assuming paidPropertyTax=True for summary)
    property_tax_deduction = 2500  # Default assumption for summary
    total_529_contributions = get_529_contributions(latest_year)
    plan_529_deduction = min(total_529_contributions * 0.20, 1500) if total_529_contributions > 0 else 0
    
    state_taxable_income = max(0, total_income - state_deduction_amount)
    state_estimated_tax, _ = calculate_indiana_state_tax(state_taxable_income, filing_status, property_tax_deduction, plan_529_deduction)
    
    # Get actual taxes paid
    taxes_paid_data = get_taxes_paid(latest_year)
    federal_paid = taxes_paid_data['federal']['total']
    federal_refund_eligible_paid = taxes_paid_data['federal']['refund_eligible_total']
    state_paid = taxes_paid_data['state']['total']
    
    # Calculate refund-eligible federal tax
    federal_refund_eligible_estimated = get_refund_eligible_federal_tax(federal_tax_components)
    
    total_estimated = federal_refund_eligible_estimated + state_estimated_tax
    total_paid = federal_refund_eligible_paid + state_paid
    
    return {
        'year': latest_year,
        'total_income': total_income,
        'federal_estimated_tax': federal_estimated_tax,
        'state_estimated_tax': state_estimated_tax,
        'total_estimated_tax': total_estimated,
        'federal_taxes_paid': federal_paid,
        'state_taxes_paid': state_paid,
        'total_taxes_paid': total_paid,
        'federal_refund_owed': federal_refund_eligible_paid - federal_refund_eligible_estimated,
        'state_refund_owed': state_paid - state_estimated_tax,
        'total_refund_owed': total_paid - total_estimated,
        'effective_rate': (total_estimated / total_income) * 100 if total_income > 0 else 0,
        'federal_effective_rate': (federal_estimated_tax / total_income) * 100 if total_income > 0 else 0,
        'state_effective_rate': (state_estimated_tax / total_income) * 100 if total_income > 0 else 0
    }
