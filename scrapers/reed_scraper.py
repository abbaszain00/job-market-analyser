# scrapers/reed_scraper.py

import requests
from bs4 import BeautifulSoup
import time

def scrape_reed():
    """
    Scrape graduate software engineer jobs from Reed.co.uk
    """
    
    # Step 1: Define the URL
    url = "https://www.reed.co.uk/jobs/graduate-software-engineer-jobs-in-london"
    
    # Step 2: Make HTTP request
    print(f"Fetching: {url}")
    response = requests.get(url)
    
    # Step 3: Check if successful
    if response.status_code == 200:
        print("✅ Successfully fetched the page!")
    else:
        print(f"❌ Failed to fetch page. Status code: {response.status_code}")
        return []
    
    # Step 4: Parse HTML
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Step 5: Find all job cards
    job_cards = soup.find_all('article', {'data-qa': 'job-card'})
    print(f"Found {len(job_cards)} job listings!")
    
    # Step 6: Extract data from each job card
    jobs = []
    
    for card in job_cards:
        try:
            # Extract job title
            title_tag = card.find('a', class_='job-card_jobTitle__HORxw')
            title = title_tag.text.strip() if title_tag else "N/A"
            
            # Extract job URL
            job_url = "https://www.reed.co.uk" + title_tag['href'] if title_tag else "N/A"
            
            # Extract company name
            company_tag = card.find('a', class_='job-card_profileUrl__fRi56')
            company = company_tag.text.strip() if company_tag else "N/A"
            
            # Extract location
            location_tag = card.find('li', {'data-qa': 'job-card-location'})
            location = location_tag.text.strip() if location_tag else "N/A"
            
            # Extract salary (first li in the metadata list)
            salary_tag = card.find('li', class_='job-card_jobMetadata__item___QNud')
            salary = salary_tag.text.strip() if salary_tag else "N/A"
            
            # Create job dictionary
            job = {
                'title': title,
                'company': company,
                'location': location,
                'salary': salary,
                'url': job_url
            }
            
            jobs.append(job)
            
        except Exception as e:
            print(f"⚠️  Error parsing job card: {e}")
            continue
    
    return jobs


def print_jobs(jobs):
    """
    Pretty print the jobs list
    """
    print("\n" + "="*80)
    print(f"FOUND {len(jobs)} JOBS")
    print("="*80 + "\n")
    
    for i, job in enumerate(jobs, 1):
        print(f"Job #{i}")
        print(f"  Title:    {job['title']}")
        print(f"  Company:  {job['company']}")
        print(f"  Location: {job['location']}")
        print(f"  Salary:   {job['salary']}")
        print(f"  URL:      {job['url']}")
        print("-" * 80)


# Test the scraper
if __name__ == "__main__":
    print("Starting Reed scraper...")
    print("-" * 80)
    
    jobs = scrape_reed()
    
    if jobs:
        print_jobs(jobs)
        print(f"\n✅ Successfully scraped {len(jobs)} jobs!")
    else:
        print("\n❌ No jobs found or error occurred")