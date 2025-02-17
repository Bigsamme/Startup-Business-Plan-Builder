
from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv() 

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

client = OpenAI(api_key=OPENAI_API_KEY)

gpt_model = "gpt-4o-mini"

def generate_business_plan(name, mission, product_description, target_market, competitive_landscape, revenue_model,
                           company_history, problem_statement, founding_team, uvp, milestones,
                           market_research, go_to_market, financial_data, risks, future_roadmap):
    prompt = f"""
    You are a helpful assistant skilled in business strategy and planning. Based on the details below, generate a detailed, professional business plan that is suitable for pitching to investors.

    Business Details:
    - Business Name: {name}
    - Mission: {mission}
    - Product Description: {product_description}
    - Target Market: {target_market}
    - Competitive Landscape: {competitive_landscape}
    - Revenue Model: {revenue_model}

    Additional Information:
    - Company History: {company_history}
    - Problem Statement: {problem_statement}
    - Founding Team & Management: {founding_team}
    - Unique Value Proposition (UVP): {uvp}
    - Milestones & Traction: {milestones}
    - Detailed Market Research: {market_research}
    - Go-to-Market Strategy: {go_to_market}
    - Financial Data & Assumptions: {financial_data}
    - Risks & Challenges: {risks}
    - Future Roadmap: {future_roadmap}

    The business plan should include the following sections:
    1. Executive Summary
    2. Company Description
    3. Market Analysis
    4. Organization & Management
    5. Product or Service Line
    6. Marketing & Sales Strategy
    7. Funding Request
    8. Financial Projections
    9. Appendix (if applicable)

    Please format the response with clear headings and bullet points where relevant.
    """
    completion = client.chat.completions.create(
        model=gpt_model,
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt}
        ]
    )
    return completion

# Hard-coded test values for comprehensive business details
name = "Acme Innovations"
mission = "Revolutionize productivity through cutting-edge AI solutions."
product_description = "An AI-driven analytics platform that simplifies complex data analysis and provides actionable insights."
target_market = "Small and medium-sized enterprises looking for scalable tech solutions."
competitive_landscape = "A competitive field with both established legacy software providers and emerging cloud-based solutions."
revenue_model = "Recurring subscription model with tiered pricing plans."

company_history = "Founded in 2020, Acme Innovations was created to simplify business operations through advanced AI technologies."
problem_statement = "Many businesses struggle to analyze complex datasets quickly, leading to missed opportunities and inefficient decision-making."
founding_team = "A diverse team of experienced entrepreneurs and AI experts, with backgrounds in technology, business strategy, and product development."
uvp = "Our platform leverages cutting-edge machine learning algorithms to deliver real-time, customized insights that competitors can't match."
milestones = "Achieved 20% month-over-month user growth, secured a pilot program with a major industry partner, and received early positive reviews from beta users."
market_research = "The market for AI-driven analytics is rapidly expanding, with SMEs increasingly seeking affordable, scalable solutions to remain competitive."
go_to_market = "Our strategy involves targeted digital marketing, strategic partnerships, and direct outreach to key decision-makers within our target market."
financial_data = "Initial funding of $500k has been raised; projections indicate break-even within 18 months, with multiple pricing tiers to cater to varying business sizes."
risks = "Primary risks include aggressive competition and scaling challenges; mitigation plans involve continuous R&D and forming strategic alliances."
future_roadmap = "In the short term, focus on product refinement and customer acquisition; in the long term, plan to expand globally and integrate additional data sources for enhanced analytics."


response = generate_business_plan(name, mission, product_description, target_market, competitive_landscape, revenue_model,
                                  company_history, problem_statement, founding_team, uvp, milestones,
                                  market_research, go_to_market, financial_data, risks, future_roadmap)

# Extract the formatted content from the first choice
formatted_plan = response['choices'][0]['message']['content']

# Print the formatted business plan (which includes headings and bullet points)
print(formatted_plan)