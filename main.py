from agents.team_agent import agent_team
import argparse

def main():
    parser = argparse.ArgumentParser(description="Market Analyzer - Query financial and market insights using agents.")
    parser.add_argument("--query","-q", type=str, required=True, help="Your query about the market, companies, or sectors")
    
    args = parser.parse_args()

    query = args.query

    print(f"\n🔍 Analyzing: {query}\n")
    response = agent_team.print_response(query, stream=True)

if __name__ == "__main__":
    main()
