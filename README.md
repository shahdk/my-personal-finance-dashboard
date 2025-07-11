# Personal Finance Dashboard 💰

> AI-Generated Doc

> This is not tested on Windows, and this is NOT production ready code

A comprehensive personal finance tracking and visualization dashboard built with Streamlit, PostgreSQL, and AI-powered chat assistance. Track your income, expenses, net worth, vacations, and get insights through natural language queries.

## 🎥 Dashboard Demo

[![Dashboard Demo](https://img.youtube.com/vi/gFE5ggBpX3Y/0.jpg)](https://www.youtube.com/watch?v=gFE5ggBpX3Y)


*Interactive demo showing key features of the Personal Finance Dashboard*

## 🌟 Features

### 📊 Financial Visualization
- **Cash Flow Analysis**: Interactive Sankey diagrams showing money flow
- **Budget Tables**: Yearly and monthly budget views with editing capabilities
- **Time Series Charts**: Income and expense trends over time
- **Net Worth Tracking**: Progress bars and growth metrics
- **Vacation Analytics**: Interactive map and spending analysis

### 🤖 AI Assistant
- **Natural Language Queries**: Ask questions about your finances in plain English
- **SQL-powered RAG**: Uses LLM + SQL for accurate data analysis
- **Smart Verification**: Dual-model approach for query accuracy
- **Response Correction**: AI-enhanced responses for clarity and accuracy

### 💾 Data Management
- **PostgreSQL Database**: Robust data storage and querying
- **Account Management**: Searchable account directory with categories
- **Real-time Updates**: Live data editing and synchronization
- **Full-text Search**: Advanced search capabilities

## 🚀 Quick Start with Docker

### Prerequisites
- Docker and Docker Compose installed
- [Ollama for AI chat features](./OLLAMA_CONNECTION.md)

### 1. Clone the Repository
```bash
git clone https://github.com/yourusername/my-personal-finance-dashboard.git
cd my-personal-finance-dashboard
```

### 2. Start the Application
```bash
docker-compose up -d
```

### 3. Access the Dashboard
Open your browser and navigate to: `http://localhost:8501`

The application will automatically:
- Set up PostgreSQL database
- Create all necessary tables
- Load demo data
- Start the Streamlit dashboard

## 📋 Manual Setup

### Prerequisites
- Python 3.11+
- PostgreSQL 13+
- Ollama for AI features

### 1. Database Setup
```bash
# Create database
createdb personal_finance

# Run schema and demo data
psql -d personal_finance -f schema.sql
psql -d personal_finance -f LOAD_DATA-account-info.sql
psql -d personal_finance -f LOAD_DATA-expense-2024.sql
psql -d personal_finance -f LOAD_DATA-expense-2025.sql
psql -d personal_finance -f LOAD_DATA-income-2024.sql
psql -d personal_finance -f LOAD_DATA-income-2025.sql
psql -d personal_finance -f LOAD_DATA-networth.sql
psql -d personal_finance -f LOAD_DATA-vacation.sql
```

### 2. Python Environment
```bash
# Install dependencies
pip install -r requirements.txt

# Set environment variables
export DB_HOST=localhost
export DB_NAME=personal_finance
export DB_USER=your_username
export DB_PASSWORD=your_password
export DB_PORT=5432
```

### 3. Run the Application
```bash
streamlit run viz.py
```

## 🤖 AI Chat Assistant Setup

The dashboard includes an AI-powered chat assistant that can answer questions about your financial data using natural language.

### 1. Install Ollama
```bash
# macOS
brew install ollama

# Linux
curl -fsSL https://ollama.ai/install.sh | sh

# Windows
Download from https://ollama.ai
```

### 2. Install Required Models
```bash
ollama pull gemma3n      # For creative SQL generation
ollama pull phi4-mini-reasoning  # For verification and correction
```

### 3. Start Ollama Service
```bash
ollama serve
```

The chat assistant will automatically detect if Ollama is running and enable AI features.

## 📊 Dashboard Tabs

### 1. At a Glance
- Sankey diagram showing cash flow
- Toggle between years and show/hide values

### 2. Yearly Budget
- Tabular view of income and expenses by year
- Filter by categories and multiple years
- Color-coded category headers

### 3. Monthly Budget
- Editable monthly budget with save functionality
- Month-by-month breakdown
- Direct database updates

### 4. Income & Expense
- Time series charts with filtering
- Group by year or show detailed timeline
- Multi-select categories and sources

### 5. Vacation
- Interactive world map of destinations
- Spending timeline and analytics
- Location-based grouping

### 6. Net Worth
- Progress tracking towards financial goals
- Category-wise breakdown with YoY growth
- Summary statistics and trends

### 7. Net Worth Goals
- Visual progress bars for 2024-2028
- Dual tracking: Net worth + Passive income
- Target vs. actual comparisons

### 8. Account Info
- Searchable account directory
- Category breakdown and statistics
- Clickable website links

### 9. Chat Assistant
- Natural language financial queries
- AI-powered SQL generation and verification
- Debug information with query details

## 🗂️ Database Schema

### Core Tables
- **income**: Track all income sources and categories
- **expense**: Record expenses with detailed categorization
- **net_worth**: Asset tracking across multiple categories
- **vacation**: Travel expenses with location data
- **account_info**: Account directory with descriptions

### Key Features
- Full-text search indexes
- Optimized for time-series queries
- Flexible categorization system
- Geographic data support

## 🎨 Customization

### Adding Your Own Data
1. **Replace Demo Data**: Modify `demo_data.sql` with your actual financial data
2. **Update Categories**: Adjust category constants in `constants.py`
3. **Custom Visualizations**: Extend charts in individual Python modules

### Environment Configuration
```bash
# Database settings
DB_HOST=localhost
DB_NAME=your_db_name
DB_USER=your_username
DB_PASSWORD=your_password
DB_PORT=5432

# AI settings (optional)
OLLAMA_HOST=localhost
OLLAMA_PORT=11434
```

## 🔧 Development

### Project Structure
```
├── viz.py              # Main Streamlit app
├── db.py               # Database connection
├── schema.sql          # Database schema
├── demo_data.sql       # Sample data
├── chatassistant.py    # AI chat functionality
├── budget.py           # Budget management
├── networth.py         # Net worth tracking
├── accountinfo.py      # Account management
├── vacation.py         # Vacation analytics
├── income.py           # Income visualization
├── expense.py          # Expense visualization
├── sankey*.py          # Cash flow diagrams
├── constants.py        # Application constants
├── Dockerfile          # Docker configuration
├── docker-compose.yml  # Multi-container setup
└── requirements.txt    # Python dependencies
```

### Adding New Features
1. Create new Python modules for specific functionality
2. Import and integrate in `viz.py`
3. Add new database tables in `schema.sql` if needed
4. Update constants and categories as required

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch: `git checkout -b feature-name`
3. Make your changes and test thoroughly
4. Commit your changes: `git commit -am 'Add feature'`
5. Push to the branch: `git push origin feature-name`
6. Submit a pull request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

Built with ❤️ using Streamlit, PostgreSQL, and AI (Cursor and Claude Sonnet 4)
