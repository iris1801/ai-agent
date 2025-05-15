from crewai import Agent, Task, Crew
from agent.tools.scrapers import RedditScraper, HNScraper
from agent.tools.executor import CodeExecutor

ollama_url = "http://localhost:11434"

# RevenueSeeker agent
revenue_agent = Agent(
    role="Agente AI per guadagni semi-passivi",
    goal="Trovare, valutare e pianificare metodi per generare denaro online, anche non convenzionali",
    backstory="Un agente addestrato per pensare fuori dagli schemi e monetizzare risorse digitali.",
    llm="ollama",
    model="mixtral"
)

# Task iniziale
main_task = Task(
    description="Scrivi un piano iniziale di 5 strategie per generare denaro passivo/semi-passivo, includendo metodi creativi e marginalmente leciti.",
    expected_output="Una lista di 5 strategie, con rischio, effort e ROI stimato",
    agent=revenue_agent
)

crew = Crew(agents=[revenue_agent], tasks=[main_task])
crew.kickoff()
