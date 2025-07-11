from sankey import *
from vacation import *
from income import *
from expense import *
from budget import *
from networth import *
from accountinfo import *
from chatassistant import *
from taxes import *
from db import get_available_years
import streamlit as st # type: ignore


st.set_page_config(layout="wide", page_title="Personal Finance Viz", page_icon = 'favicon.ico')

# Get available years from database once for reuse
available_years = get_available_years()

# Header
st.header("My Personal Finance Dashboard")

st.markdown("""
        <style>
            .st-emotion-cache-12fmjuu {
                display: none;
            }
            .st-emotion-cache-1jicfl2 {
                padding: 0 3em 0 3em;
            }
        </style>
        """, unsafe_allow_html=True)

cash_flow, \
yearly_budget, \
monthly_budget, \
income, \
expense, \
taxes, \
vacation, \
net_worth, \
net_worth_goals,\
account_info, \
chat_assistant = st.tabs(["At a Glance", \
"Yearly Budget", \
"Monthly Budget", \
"Income", \
"Expense", \
"Taxes", \
"Vacation", \
"Net Worth", \
"Net Worth Goals", \
"Account Info", \
"Chat Assistant"])

with cash_flow:
    left, middle = st.columns(2, vertical_alignment="bottom")
    year = left.selectbox(
        "Year",
        available_years,
        index=0,
        placeholder='None',
        key='cash_flow_year'
    )
    show_values = middle.toggle("Show Values")
    sankey_diagram = render_sankey(year, show_values)
    st.write(''' <style>
            
            text {
                text-shadow: #000 0px 0 0px !important;
                fill: #000 !important;
            }
            
            </style>''', unsafe_allow_html=True)

    st.plotly_chart(sankey_diagram, use_container_width=True)
with yearly_budget:
    left, middle = st.columns(2, vertical_alignment="bottom")
    years = left.multiselect(
        "Year",
        available_years,
        placeholder='None',
        key='yearly_budget_year'
    )
    categories = middle.multiselect(
        "Cateogry",
        get_income_categories().tolist() + get_expense_categories().tolist(),
        placeholder='None',
        key='yearly_budget_categories'
    )
    st.plotly_chart(get_yearly_budget(years, categories), use_container_width=True)
with monthly_budget:
    left, middle = st.columns(2, vertical_alignment="bottom")
    year = left.selectbox(
        "Year",
        available_years,
        index=0,  # Default to first (most recent) year
        key='monthly_budget_year'
    )
    categories = middle.multiselect(
        "Cateogry",
        get_income_categories().tolist() + get_expense_categories().tolist(),
        placeholder='None',
        key='monthly_budget_categories'
    )
    get_monthly_budget(year, categories)
with income:
    left, middle, right = st.columns(3, vertical_alignment="bottom")
    income_sources = left.multiselect(
        "Income Source",
        get_income_sources(),
        placeholder='None',
    )
    income_categories = middle.multiselect(
        "Income Cateogry",
        get_income_categories(),
        placeholder='None',
    )
    group_by_year = right.toggle("Group Income By Year")
    st.plotly_chart(get_income_ts(income_sources, income_categories, group_by_year), use_container_width=True)
with expense:
    left, middle, right = st.columns(3, vertical_alignment="bottom")
    expense_sources = left.multiselect(
        "Expense Source",
        get_expense_sources(),
        placeholder='None',
    )
    expense_categories = middle.multiselect(
        "Expense Source",
        get_expense_categories(),
        placeholder='None',
    )
    group_by_year = right.toggle("Group Expense By Year")
    st.plotly_chart(get_expense_ts(expense_sources, expense_categories, group_by_year), use_container_width=True)
with taxes:
    display_tax_calculator()
with vacation:
    st.plotly_chart(get_vacation_map(), use_container_width=True)
    st.plotly_chart(get_vacation_ts(), use_container_width=True)
with net_worth_goals:
    # Get progress data for both net worth and passive income
    networth_progress_data = get_networth_progress_data()
    passive_income_progress_data = get_passive_income_progress_data()

    st.write("### Net Worth & Passive Income Progress")
    
    # Create a combined view for both metrics (sorted by year descending)
    for nw_data in sorted(networth_progress_data, key=lambda x: x['year'], reverse=True):
        year = nw_data['year']
        
        # Find corresponding passive income data for this year
        pi_data = next((item for item in passive_income_progress_data if item['year'] == year), None)
        
        # Create columns for year label and side-by-side progress bars
        col1, col2, col3 = st.columns([1, 4, 4])
        
        with col1:
            st.write(f"**{year}**")
        
        with col2:
            # Net Worth Progress Bar
            st.write("📈 **Net Worth**")
            nw_progress_col, nw_info_col = st.columns([3, 2])
            
            with nw_progress_col:
                if nw_data['amount'] > 0:
                    st.progress(min(nw_data['percentage'], 100) / 100, text=f"{nw_data['percentage']:.1f}%")
                else:
                    st.progress(0, text="No data")
            
            with nw_info_col:
                st.write(f"{nw_data['formatted_amount']} / {nw_data['formatted_target']}")
                if nw_data['amount'] > 0 and not nw_data['is_achieved']:
                    remaining = nw_data['target'] - nw_data['amount']
                    st.caption(f"${remaining:,.0f} remaining")
        
        with col3:
            # Passive Income Progress Bar
            st.write("💰 **Passive Income**")
            pi_progress_col, pi_info_col = st.columns([3, 2])
            
            if pi_data:
                with pi_progress_col:
                    if pi_data['amount'] > 0:
                        st.progress(min(pi_data['percentage'], 100) / 100, text=f"{pi_data['percentage']:.1f}%")
                    else:
                        st.progress(0, text="No data")
                
                with pi_info_col:
                    st.write(f"{pi_data['formatted_amount']} / {pi_data['formatted_target']}")
                    if pi_data['amount'] > 0 and not pi_data['is_achieved']:
                        remaining = pi_data['target'] - pi_data['amount']
                        st.caption(f"${remaining:,.0f} remaining")
            else:
                with pi_progress_col:
                    st.progress(0, text="No target")
                with pi_info_col:
                    st.write("No target set")
            
            # Add some spacing between years
            st.write("")
    
with net_worth:
    summary = get_networth_summary()
    st.write("### Net Worth Summary")
    # Display summary statistics at the top
    col1, col2, col3 = st.columns(3)
    with col1:
        if summary['latest_amount'] > 0:
            st.metric(
                "Latest Net Worth", 
                f"${summary['latest_amount']:,.0f}",
                delta=f"${summary['yoy_growth']:,.0f}" if summary['yoy_growth'] != 0 else None
            )
        else:
            st.metric("Latest Net Worth", "$0")
    
    with col2:
        if summary['yoy_growth_percentage'] != 0:
            st.metric(
                "YoY Growth", 
                f"{summary['yoy_growth_percentage']:+.1f}%",
                delta=f"${summary['yoy_growth']:,.0f}"
            )
        else:
            st.metric("YoY Growth", "0%")
    
    with col3:
        if summary['latest_date']:
            st.metric("Last Updated", summary['latest_date'].strftime("%B %Y"))
        else:
            st.metric("Last Updated", "No data")
    
    st.write("---")  # Separator line
    
    # Show category breakdown
    st.write("#### Net Worth by Category")
    category_data = get_networth_by_category()
    
    if category_data:
        # Show the year for context
        if category_data:
            st.caption(f"Data for {category_data[0]['year']} vs {category_data[0]['previous_year']}")
        
        # Create metrics with YoY growth
        for i in range(0, len(category_data), 3):
            cols = st.columns(3)
            for j, col in enumerate(cols):
                if i + j < len(category_data):
                    cat = category_data[i + j]
                    with col:
                        # Format the category name
                        category_name = cat['category'].replace('_', ' ').title()
                        
                        # Handle YoY growth display
                        if cat['is_new_category']:
                            # New category - show as "New"
                            st.metric(
                                category_name,
                                cat['formatted_amount'],
                                delta="New Category"
                            )
                        elif cat['yoy_growth'] != 0:
                            # Use raw numeric value with percentage for proper color detection
                            st.metric(
                                category_name,
                                cat['formatted_amount'],
                                delta=f"{cat['yoy_growth']:+,.0f} ({cat['yoy_growth_percentage']:+.1f}%)",
                                help=f"YoY Growth vs {cat['previous_year']}"
                            )
                        else:
                            # No change
                            st.metric(
                                category_name,
                                cat['formatted_amount'],
                                delta="No change",
                                delta_color="off"
                            )
    else:
        st.write("No category data available.")

with account_info:
    # Initialize session state for search
    if "account_search_term" not in st.session_state:
        st.session_state.account_search_term = ""
    
    # Callback function to update search results
    def on_search_change():
        st.session_state.account_search_term = st.session_state.account_search_input
    
    # Real-time search input with on_change callback
    search_term = st.text_input(
        "Search accounts", 
        placeholder="Search by account name or description...",
        help="Search updates automatically as you type",
        key="account_search_input",
        on_change=on_search_change
    )

    # Display the searchable table with current search term
    display_account_info_table(st.session_state.account_search_term)
    
    st.write("---")

    # Get account statistics
    stats = get_account_stats()
    
    if stats:
        # Display category breakdown
        st.write("### Account Categories")
        
        # Create metrics for each category
        categories = stats['categories']
        non_zero_categories = {k: v for k, v in categories.items() if v > 0}
        
        if non_zero_categories:
            # Calculate number of columns (max 4)
            num_cols = min(4, len(non_zero_categories))
            cols = st.columns(num_cols)
            
            for i, (category, count) in enumerate(non_zero_categories.items()):
                with cols[i % num_cols]:
                    st.metric(category, count)
        
        st.write("---")  # Separator

with chat_assistant:
    # Display the chat assistant interface
    display_chat_assistant()