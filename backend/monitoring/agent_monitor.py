"""
Agent Monitoring Dashboard
"""

from datetime import datetime


class AgentMonitor:

    def __init__(self):

        # Number of active AI agents
        self.active_agents = 0

        # Number of running tasks
        self.running_tasks = 0

        # Tool usage count
        self.tool_usage = {}

        # Workflow statistics
        self.successful = 0
        self.failed = 0

        # Performance metrics
        self.execution_times = []
        self.mcp_latency = []

        # Cost tracking
        self.cost = 0.0

    # -------------------------------------------------------
    # Active Agents
    # -------------------------------------------------------

    def register_agent(self):
        self.active_agents += 1

    def finish_agent(self):
        if self.active_agents > 0:
            self.active_agents -= 1

    # -------------------------------------------------------
    # Running Tasks
    # -------------------------------------------------------

    def start_task(self):
        self.running_tasks += 1

    def finish_task(self):
        if self.running_tasks > 0:
            self.running_tasks -= 1

    # -------------------------------------------------------
    # Tool Usage
    # -------------------------------------------------------

    def record_tool(self, tool_name):

        if tool_name not in self.tool_usage:
            self.tool_usage[tool_name] = 0

        self.tool_usage[tool_name] += 1

    # -------------------------------------------------------
    # Workflow Execution
    # -------------------------------------------------------

    def record_execution(self, execution_time, success=True):

        self.execution_times.append(execution_time)

        if success:
            self.successful += 1
        else:
            self.failed += 1

    # -------------------------------------------------------
    # MCP Tool Latency
    # -------------------------------------------------------

    def record_latency(self, latency):

        self.mcp_latency.append(latency)

    # -------------------------------------------------------
    # Agent Cost
    # -------------------------------------------------------

    def add_cost(self, amount):

        self.cost += amount

    # -------------------------------------------------------
    # Dashboard
    # -------------------------------------------------------

    def dashboard(self):

        total = self.successful + self.failed

        if total == 0:
            success_rate = 0
        else:
            success_rate = round(
                (self.successful / total) * 100,
                2
            )

        if len(self.execution_times) == 0:
            avg_execution = 0
        else:
            avg_execution = round(
                sum(self.execution_times) /
                len(self.execution_times),
                2
            )

        if len(self.mcp_latency) == 0:
            avg_latency = 0
        else:
            avg_latency = round(
                sum(self.mcp_latency) /
                len(self.mcp_latency),
                2
            )

        return {

            "Timestamp": datetime.now(),

            "Active Agents": self.active_agents,

            "Running Tasks": self.running_tasks,

            "Tool Usage": self.tool_usage,

            "Workflow Success Rate": f"{success_rate}%",

            "Failed Executions": self.failed,

            "Average Execution Time": f"{avg_execution} sec",

            "MCP Tool Latency": f"{avg_latency} ms",

            "Agent Cost": f"${self.cost:.2f}"

        }


# ===========================================================
# Testing
# ===========================================================

if __name__ == "__main__":

    monitor = AgentMonitor()

    print("\nStarting Monitoring...\n")

    # Active Agents
    monitor.register_agent()
    monitor.register_agent()
    monitor.register_agent()

    # Running Tasks
    monitor.start_task()
    monitor.start_task()

    # Tool Usage
    monitor.record_tool("Employee Tool")
    monitor.record_tool("Employee Tool")
    monitor.record_tool("Payroll Tool")
    monitor.record_tool("Email Tool")
    monitor.record_tool("Calendar Tool")
    monitor.record_tool("Project Tool")
    monitor.record_tool("Notification Tool")

    # Workflow Execution
    monitor.record_execution(2.5, True)
    monitor.record_execution(3.1, True)
    monitor.record_execution(4.2, False)
    monitor.record_execution(1.8, True)

    # MCP Latency
    monitor.record_latency(120)
    monitor.record_latency(140)
    monitor.record_latency(160)
    monitor.record_latency(180)

    # Cost
    monitor.add_cost(0.03)
    monitor.add_cost(0.04)
    monitor.add_cost(0.02)
    monitor.add_cost(0.05)

    # Display Dashboard
    dashboard = monitor.dashboard()

    print("=" * 60)
    print("      ENTERPRISE AI AGENT MONITORING DASHBOARD")
    print("=" * 60)

    for key, value in dashboard.items():
        print(f"{key:<30}: {value}")

    print("=" * 60)