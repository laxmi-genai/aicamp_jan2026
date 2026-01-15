import os
from google.adk.agents.llm_agent import LlmAgent
from google.adk.tools.api_registry import ApiRegistry

# Configure with your Google Cloud Project ID and registered MCP server name
PROJECT_ID = "your-project-id"
MCP_SERVER_NAME = "projects/your-project-id/locations/global/mcpServers/google-bigquery.googleapis.com-mcp"
# locations/global/mcpServers/google-bigquery.googleapis.com-mcp

# Example header provider for BigQuery, a project header is required.
def header_provider(context):
    return {"x-goog-user-project": PROJECT_ID}

# Initialize ApiRegistry
api_registry = ApiRegistry(
    api_registry_project_id=PROJECT_ID,
    header_provider=header_provider
)

# Get the toolset for the specific MCP server
registry_tools = api_registry.get_toolset(
    mcp_server_name=MCP_SERVER_NAME,
    # Optionally filter tools:
    #tool_filter=["list_datasets", "run_query"]
)

# Create an agent with the tools
root_agent = LlmAgent(
    model="gemini-2.5-flash", 
    name="bigquery_assistant",
    instruction="""
Help user access their BigQuery data using the available tools.
    """,
    tools=[registry_tools],
)