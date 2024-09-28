#Task 1: Customer Service Ticket Tracker Demonstrate your 
#ability to use nested collections and loops by creating a system to track customer service tickets.
#Develop a program that: Tracks customer service tickets, each with a unique ID, customer name, issue description, and status (open/closed).
#Implement functions to:
#Open a new service ticket.
#Update the status of an existing ticket.
#Display all tickets or filter by status.
#Initialize with some sample tickets and include functionality for additional ticket entry.


service_tickets = {
    "Ticket001": {"Customer": "Alice", "Issue": "Login problem", "Status": "open"},
    "Ticket002": {"Customer": "Bob", "Issue": "Payment issue", "Status": "closed"}
}

def open_ticket(ticket_id, customer, issue):
    if ticket_id in service_tickets:
        print(f"Error: Ticket ID {ticket_id} already exists.")
    else:
        service_tickets[ticket_id] = {"Customer": customer, "Issue": issue, "Status": "open"}
        print(f"Ticket {ticket_id} opened for {customer}.")

def update_ticket_status(ticket_id, new_status):
    if ticket_id in service_tickets:
        service_tickets[ticket_id]["Status"] = new_status
        print(f"Ticket {ticket_id} status updated to {new_status}.")
    else:
        print(f"Error: Ticket ID {ticket_id} does not exist.")

def display_tickets(filter_status=None):
    for ticket_id, details in service_tickets.items():
        if filter_status is None or details["Status"] == filter_status:
            print(f"{ticket_id}: {details['Customer']} - {details['Issue']} [{details['Status']}]")


if __name__ == "__main__":
    print("All Tickets:")
    display_tickets()
    
    open_ticket("Ticket003", "Charlie", "Cannot reset password")

    update_ticket_status("Ticket001", "closed")
    
    print("\nOpen Tickets:")
    display_tickets("open")
    
    print("\nClosed Tickets:")
    display_tickets("closed")