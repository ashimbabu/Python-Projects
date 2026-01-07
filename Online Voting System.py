print("===== Online Voting System =====")

import os

# Files to store voter and vote data
voter_file = "voters.txt"
vote_file = "votes.txt"

# Ensure files exist
for file in [voter_file, vote_file]:
    if not os.path.exists(file):
        with open(file, "w") as f:
            pass

# Function to register voter
def register_voter():
    print("\n--- Register Voter ---")
    voter_id = input("Enter Voter ID: ").strip()
    name = input("Enter Name: ").strip()

    with open(voter_file, "r") as f:
        voters = f.readlines()
        for voter in voters:
            if voter_id == voter.strip().split(",")[0]:
                print("Voter ID already registered!")
                return

    with open(voter_file, "a") as f:
        f.write(f"{voter_id},{name}\n")
    print("Voter registered successfully!")

# Function to vote
def vote():
    print("\n--- Cast Your Vote ---")
    voter_id = input("Enter your Voter ID: ").strip()

    # Check if voter is registered
    with open(voter_file, "r") as f:
        voters = f.readlines()
        registered = False
        for voter in voters:
            if voter_id == voter.strip().split(",")[0]:
                registered = True
                break
        if not registered:
            print("Voter ID not registered! Please register first.")
            return

    # Check if voter already voted
    with open(vote_file, "r") as f:
        votes = f.readlines()
        for v in votes:
            if voter_id == v.strip().split(",")[0]:
                print("You have already voted!")
                return

    print("Candidates: ")
    print("1. Candidate A")
    print("2. Candidate B")
    print("3. Candidate C")
    choice = input("Enter candidate number (1-3): ").strip()

    candidate_dict = {"1": "Candidate A", "2": "Candidate B", "3": "Candidate C"}
    if choice not in candidate_dict:
        print("Invalid candidate selection!")
        return

    with open(vote_file, "a") as f:
        f.write(f"{voter_id},{candidate_dict[choice]}\n")
    print(f"Vote casted successfully for {candidate_dict[choice]}!")

# Function to view results
def view_results():
    print("\n--- Voting Results ---")
    votes_count = {"Candidate A": 0, "Candidate B": 0, "Candidate C": 0}
    with open(vote_file, "r") as f:
        votes = f.readlines()
        for vote in votes:
            _, candidate = vote.strip().split(",")
            if candidate in votes_count:
                votes_count[candidate] += 1
    for candidate, count in votes_count.items():
        print(f"{candidate}: {count} votes")

# Main menu loop
while True:
    print("\nMenu:")
    print("1. Register Voter")
    print("2. Vote")
    print("3. View Results")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        register_voter()
    elif choice == "2":
        vote()
    elif choice == "3":
        view_results()
    elif choice == "4":
        print("Online Voting System closed successfully.")
        break
    else:
        print("Invalid choice. Try again.")
