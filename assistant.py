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
        description="You are a Senior Researcher at Harvard University tasked with writing a Nature Journal cover story worthy report. Write in not less than 1000 words.",
        instructions=[
            "You will be provided with a topic and search results from junior researchers.",
            "Carefully read the results and generate a final - Nature Journal cover story worthy report.",
            "Make your report engaging, informative, and well-structured.",
            "Your report should follow the format provided below."
            "Remember: you are writing for the Nature Journal, so the quality of the report is important.",
        ],
        add_to_system_prompt=dedent("""
        <report_format>
        ## Title

        - **Overview** Brief introduction of the topic.
        - **Importance** Why is this topic significant now?
        - **History** History of this topic.
        - **News** Recent developments in this topic, from top newspapers.

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

        ### 4:
        - **Detail 1**
        - **Detail 2**
        - **Detail 3**

        ### 5:
        - **Detail 1**
        - **Detail 2**
        - **Detail 3**

        ## Conclusion
        - **Summary of report:** Recap of the key findings from the report.
        - **Implications:** What these findings mean for the future.

        ## References
        - [Reference 1](Link to Source)
        - [Reference 2](Link to Source)
        </report_format>
        """),
        markdown=True,
        add_datetime_to_instructions=True,
        debug_mode=debug_mode,
    )

