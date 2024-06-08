import streamlit as st
from rag import  run_rag
# Placeholder function for input parser
def parse_input(objective_description, scenarios, expected_outputs):
    # Your logic to parse input and return potential prompts goes here
    prompts = run_rag(objective_description, scenarios, expected_outputs)

    potential_prompts = [
        f"Objective: {objective_description}",
        f"Scenarios: {scenarios}",
        f"Expected Outputs: {expected_outputs}",
        f"{prompts}"
    ]
    return potential_prompts

def main():
    st.title("PromptlyTech Prompt generator")

    st.write("## Input Details")

    # Input fields for detailed inputs
    objective_description = st.text_area("Objective Description:")
    scenarios = st.text_area("Scenarios:")
    expected_outputs = st.text_area("Expected Outputs:")

    # Button to submit prompt
    if st.button("Submit"):
        # Call the input parser function here
        potential_prompts = parse_input(objective_description, scenarios, expected_outputs)
        # Display potential prompts
        st.write("### Potential Prompts:")
        for prompt in potential_prompts:
            st.write(f"- {prompt}")

if __name__ == "__main__":
    main()
