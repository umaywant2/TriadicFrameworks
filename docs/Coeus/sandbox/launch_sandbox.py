from agents.nous import NousAgent
from agents.enTFT import EnTFTAgent
from agents.tops import TopsAgent

def launch_sandbox(agent_count=3, mode="enTFT"):
    print(f"Launching Coeus Sandbox with {agent_count} agents in {mode} mode...\n")

    # Initialize agents
    agents = [NousAgent(), EnTFTAgent(), TopsAgent()]
    tops = agents[2]

    # Assign roles
    roles = tops.assign_roles(agents, {"name": "SandboxInit"})
    tops.log_action(f"Roles assigned: {roles}")

    print("\nSandbox ready. Agents standing by.\n")

if __name__ == "__main__":
    launch_sandbox()

