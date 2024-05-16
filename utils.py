# utils.py

import requests

def fetch_data_from_url(url):
    """
    Fetch data from a given URL.
    
    :param url: The URL to fetch data from.
    :return: The data fetched from the URL.
    """
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        response.raise_for_status()

def process_search_results(search_results):
    """
    Process search results and format them for display.
    
    :param search_results: The search results to process.
    :return: The formatted search results.
    """
    processed_results = []
    for result in search_results:
        processed_result = {
            'title': result.get('title', 'No title'),
            'summary': result.get('summary', 'No summary'),
            'url': result.get('url', '#')
        }
        processed_results.append(processed_result)
    return processed_results

def format_report_section(title, details):
    """
    Format a section of the report.
    
    :param title: The title of the section.
    :param details: A list of details to include in the section.
    :return: The formatted section as a string.
    """
    section = f"### {title}\n"
    for detail in details:
        section += f"- **{detail['title']}**: {detail['summary']}\n"
    return section

def generate_final_report(sections):
    """
    Generate the final report by combining all sections.
    
    :param sections: A list of sections to include in the report.
    :return: The final report as a string.
    """
    report = ""
    for section in sections:
        report += format_report_section(section['title'], section['details'])
        report += "\n\n"
    return report

def example_utility_function():
    """
    Example utility function.
    
    :return: A string indicating this is an example function.
    """
    return "This is an example utility function."

