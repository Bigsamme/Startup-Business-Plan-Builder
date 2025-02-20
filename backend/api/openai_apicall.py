from dotenv import load_dotenv
import os
from openai import OpenAI
from rich.console import Console
from rich.markdown import Markdown


ai_model = "gpt-4o-mini"

load_dotenv() 

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=OPENAI_API_KEY)


def generate_investor_pitch(one_sentence_description, long_term_vision, uvp, problem, solution, target_market, market_trends, revenue_model, milestones, key_team_members, financial_projections, investment_amount, anticipated_returns):
    system_prompt = f"""
    You are an expert on making high converting copy for investor pitches.

    Purpose: Attracting investment by clearly outlining the business opportunity.
    Key Slides: Problem, Solution, Market Opportunity, Business Model, Traction, Team, Financial Projections, and the Ask.
    Text Focus: Formal, data-driven, and visionary language.
    """
    # Incorporate questions with the responses provided (hard-coded for testing):
    user_prompt = f"""
    1. Can you describe your company in one sentence?
       Response: {one_sentence_description}
    
    2. What is your long-term vision and mission?
       Response: {long_term_vision}
    
    3. What is your Unique Value Proposition (UVP)?
       Response: {uvp}
    
    4. What specific problem or market gap are you addressing?
       Response: {problem}
    
    5. How does your product/service provide a unique solution?
       Response: {solution}
    
    6. Who is your target market and what is its estimated size?
       Response: {target_market}
    
    7. What trends or data support the growth potential of your market?
       Response: {market_trends}
    
    8. How do you generate revenue?
       Response: {revenue_model}
    
    9. What milestones or key achievements have you reached so far?
       Response: {milestones}
    
    10. Who are the key team members and what unique skills do they bring?
        Response: {key_team_members}
    
    11. Can you share any financial projections or current metrics?
        Response: {financial_projections}
    
    12. What investment amount are you seeking and how will it be utilized?
        Response: {investment_amount}
    
    13. What are the anticipated returns or milestones post-funding?
        Response: {anticipated_returns}
    """
    
    chat = client.chat.completions.create(
        model=ai_model,
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt}
        ],
        max_tokens=5000
    )
    return chat


def generate_sales_pitch(ideal_customer_challenges, solution, measurable_benefits, differentiator,
                         testimonials, pricing, call_to_action):
    system_prompt = """
    You are an expert on crafting persuasive sales pitch decks.

    Purpose: Persuade potential clients to engage with your product or service.
    Key Slides: Audience & Pain Points, Solution, Benefits, Value Proposition, Testimonials, Pricing, Call-to-Action.
    Text Focus: Persuasive, customer-centric, and benefit-oriented language.
    """
    user_prompt = f"""
    1. Who is your ideal customer, and what challenges do they face?
       Response: {ideal_customer_challenges}
    
    2. How does your product/service address these challenges?
       Response: {solution}
    
    3. What measurable benefits or ROI can customers expect?
       Response: {measurable_benefits}
    
    4. What makes your solution stand out from competitors?
       Response: {differentiator}
    
    5. Do you have any customer testimonials or case studies?
       Response: {testimonials}
    
    6. What is your pricing structure or available plans?
       Response: {pricing}
    
    7. What is the primary action you want the prospect to take?
       Response: {call_to_action}
    """
    chat = client.chat.completions.create(
        model=ai_model,
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt}
        ],
        max_tokens=500
    )
    return chat


def generate_product_overview(core_features, feature_benefits, common_use_cases, differentiator,
                              technical_aspects, upcoming_features):
    system_prompt = """
    You are an expert on creating detailed product overview decks.

    Purpose: Provide a comprehensive view of the product features and use cases.
    Key Slides: Product Features, Use Cases, Competitive Differentiators, Integration Details, Future Roadmap.
    Text Focus: Informative, descriptive, and balanced between technical and accessible language.
    """
    user_prompt = f"""
    1. What are the core features of your product/service?
       Response: {core_features}
    
    2. How does each feature benefit the user?
       Response: {feature_benefits}
    
    3. What are the most common use cases for your product?
       Response: {common_use_cases}
    
    4. How does your product differentiate itself from competitors?
       Response: {differentiator}
    
    5. Are there any technical aspects or integrations that are key selling points?
       Response: {technical_aspects}
    
    6. Do you have upcoming features or plans you can share?
       Response: {upcoming_features}
    """
    chat = client.chat.completions.create(
        model=ai_model,
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt}
        ],
        max_tokens=500
    )
    return chat


if __name__ == '__main__':
    console = Console()

    # Testing generate_investor_pitch with hard-coded responses
    investor_response = generate_investor_pitch(
        one_sentence_description="We revolutionize the fintech space with cutting-edge blockchain solutions.",
        long_term_vision="To create a seamless, transparent, and secure financial ecosystem for all.",
        uvp="Our proprietary technology integrates blockchain with AI for unmatched efficiency.",
        problem="Traditional financial systems are slow, opaque, and vulnerable to fraud.",
        solution="We leverage blockchain and AI to ensure faster transactions and enhanced security.",
        target_market="Tech-savvy financial institutions and startups looking for innovative solutions.",
        market_trends="Growing demand for digital transformation in finance and increased regulatory scrutiny.",
        revenue_model="Subscription-based model with tiered pricing for different enterprise sizes.",
        milestones="Secured partnerships with major banks and completed a successful pilot program.",
        key_team_members="Experts in blockchain, AI, and financial technology with proven industry experience.",
        financial_projections="Projected 200% growth in revenue within the next two years.",
        investment_amount="$5M for scaling operations and expanding market reach.",
        anticipated_returns="Expected ROI of 20-30% within the first three years post-investment."
    )
    formatted_investor = investor_response.choices[0].message.content
    console.print(Markdown("### Investor Pitch Response"))
    console.print(Markdown(formatted_investor))

    # Testing generate_sales_pitch with hard-coded responses
    sales_response = generate_sales_pitch(
        ideal_customer_challenges="Our ideal customers are mid-sized tech companies facing digital transformation challenges.",
        solution="We provide a robust platform that simplifies workflow and enhances productivity.",
        measurable_benefits="Customers typically see a 30% increase in efficiency and cost reduction.",
        differentiator="Our solution uniquely integrates AI with an intuitive design.",
        testimonials="Several clients have reported outstanding results, including a 40% boost in productivity.",
        pricing="We offer a tiered pricing model tailored to various business sizes.",
        call_to_action="Schedule a demo to see our solution in action."
    )
    formatted_sales = sales_response.choices[0].message.content
    console.print(Markdown("### Sales Pitch Response"))
    console.print(Markdown(formatted_sales))

    # Testing generate_product_overview with hard-coded responses
    product_response = generate_product_overview(
        core_features="Robust analytics, real-time collaboration, and seamless integration with popular tools.",
        feature_benefits="Analytics provide actionable insights, collaboration improves efficiency, and integrations streamline workflows.",
        common_use_cases="Team collaboration, project management, and data-driven decision making.",
        differentiator="Our product offers a unique combination of AI-driven insights and intuitive design.",
        technical_aspects="Integrates effortlessly with major CRM and ERP systems.",
        upcoming_features="Advanced predictive analytics and enhanced mobile functionality are on the horizon."
    )
    formatted_product = product_response.choices[0].message.content
    console.print(Markdown("### Product Overview Response"))
    console.print(Markdown(formatted_product))