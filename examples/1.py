from dotenv import load_dotenv
load_dotenv()
import os

from crewai.flow.flow import Flow, listen, start
from litellm import completion
import agentops

agentops.init(os.getenv("AGENTOPS_API_KEY"), auto_start_session=False, skip_auto_end_session=True)

class ExampleFlow(Flow):
    model = "gpt-4o-mini"

    @start()
    def generate_city(self):
        print("Starting flow")

        response = completion(
            model=self.model,
            messages=[
                {
                    "role": "user",
                    "content": "Return the name of a random city in the world.",
                },
            ],
        )

        random_city = response["choices"][0]["message"]["content"]
        print(f"Random City: {random_city}")

        return random_city

    @listen(generate_city)
    def generate_fun_fact(self, random_city):
        response = completion(
            model=self.model,
            messages=[
                {
                    "role": "user",
                    "content": f"Tell me a fun fact about {random_city}",
                },
            ],
        )

        fun_fact = response["choices"][0]["message"]["content"]
        return fun_fact


agentops.start_session()
flow = ExampleFlow()
result = flow.kickoff()
agentops.end_session(end_state="Success")

print(f"Generated fun fact: {result}")
