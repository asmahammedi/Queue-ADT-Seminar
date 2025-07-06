class JiraTicketQueue:
    def __init__(self):
        self.tickets = []

    def enqueue(self, ticket):
        """Add a new Jira ticket to the queue."""
        self.tickets.append(ticket)
        print(f"Ticket '{ticket}' added to the queue.")

    def dequeue(self):
        """Process and remove the next ticket in the queue."""
        if self.isEmpty():
            print("No tickets to process.")
            return None
        ticket = self.tickets.pop(0)
        print(f"Ticket '{ticket}' has been processed.")
        return ticket

    def peek(self):
        """View the next ticket to be processed."""
        if self.isEmpty():
            return "No tickets in queue."
        return f"Next ticket: '{self.tickets[0]}'"

    def isEmpty(self):
        return len(self.tickets) == 0

    def size(self):
        return len(self.tickets)
    


# Example usage of the JiraTicketQueue class
queue = JiraTicketQueue()

queue.enqueue("BUG-101: Login error")
queue.enqueue("TASK-204: Add search filter")
queue.enqueue("FEATURE-305: New dashboard design")  

print(queue.size()) 

print(queue.peek())        

queue.dequeue()   

print(queue.size())

print(queue.peek()) 

queue.dequeue()   

print(queue.size())

print(queue.peek())


queue.dequeue() 
print(queue.peek())           
 
          
