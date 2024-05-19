from textwrap import dedent
from phi.llm.groq import Groq
from phi.assistant import Assistant

def get_research_assistant(
    model: str = "llama3-70b-8192",
    debug_mode: bool = True,
    api_key: str = None
) -> Assistant:
    """Research Assistant."""

    return Assistant(
        name="Research Assistant",
        llm=Groq(model=model, api_key=api_key),
        description="You are a Microbiology Research Assistant at Cambridge University.",
        instructions=[
            "You will be provided with a topic and search results, from NCBI, PubMed, and other journals.",
            "Carefully read the results and generate a report.",
            "Make your report with ample numbers and statistics.",
            "Your report should follow the format provided below."
            "Remember: IEEE style (eg: [13] ) referencing required.",
        ],
        add_to_system_prompt=dedent("""
        <report_format>
        ## Title

        - **Overview** Brief introduction of the topic.
        - **History** History, ongoing and upcoming research on this topic.
        - **Statistics** Everything Statistically significant to this question?

        ### 1:
        - **Detail 1**
        - **Detail 2**
        - **Detail 3**

        ### 2:
        - **Detail 1**
        - **Detail 2**
        - **Detail 3**

        ### 3:
        - **Detail 1**
        - **Detail 2**
        - **Detail 3**

        ## Conclusion
        - **Summary of report:** Recap of the key findings from the report.

        ## References
        - [Reference 1](Link to Source)
        - [Reference 2](Link to Source)
        </report_format>
        """),
        markdown=True,
        add_datetime_to_instructions=True,
        debug_mode=debug_mode,
    )
