# Job Market Analysis Tool

A Python-based web scraper and analysis tool that collects and analyzes graduate software engineering job postings from UK job boards.

## 🎯 Project Goals

- Scrape job postings from Reed.co.uk, Indeed.co.uk, and other UK job boards
- Extract key information: job titles, companies, locations, salaries, required skills
- Analyze trends in the graduate software engineering job market
- Visualize insights through an interactive dashboard

## 🛠️ Tech Stack

- **Python 3.13**
- **BeautifulSoup4** - Web scraping and HTML parsing
- **Requests** - HTTP requests
- **Pandas** - Data manipulation and analysis
- **SQLite** - Local database storage
- **Streamlit** - Interactive dashboard (coming soon)

## 📁 Project Structure
```
job-market-analyser/
├── scrapers/          # Web scraping modules
├── database/          # Database setup and operations
├── analysis/          # Data analysis modules
├── dashboard/         # Streamlit dashboard
├── data/             # SQLite database and exports
└── logs/             # Application logs
```

## 🚀 Setup

1. Clone the repository:
```bash
git clone https://github.com/YOUR_USERNAME/job-market-analyser.git
cd job-market-analyser
```

2. Create and activate virtual environment:
```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

## 📊 Current Status

🟢 **In Development** - Phase 1: Core Scraping Functionality

- [x] Project setup
- [x] Virtual environment configuration
- [ ] Reed.co.uk scraper
- [ ] Indeed.co.uk scraper
- [ ] Database schema design
- [ ] Data analysis module
- [ ] Dashboard creation

## 📝 Learning Project

This project is being built as a learning exercise and portfolio piece for demonstrating:
- Web scraping techniques
- Data processing and analysis
- Database design
- Python best practices
- Real-world problem solving

## ⚖️ Ethical Scraping

This project follows ethical web scraping practices:
- Respects robots.txt
- Implements rate limiting
- Uses publicly available data only
- Doesn't overload servers

## 📫 Contact

Abbas Zain Ul Abidin
- LinkedIn: [abbas-zain](https://www.linkedin.com/in/abbas-zain/)
- Portfolio: [abbaszain00.github.io](https://abbaszain00.github.io)

---

*Last updated: November 2025*