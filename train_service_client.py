import grpc
from train_service_pb2 import Ticket, User
from train_service_pb2_grpc import TrainServiceStub

def main():
    channel = grpc.insecure_channel('localhost:50051')
    client = TrainServiceStub(channel)

    # Example usage
    user = User(first_name="John", last_name="Doe", email="john.doe@example.com")
    ticket = Ticket(from="London", to="France", user=user)

    # Purchase Ticket
    purchased_ticket = client.PurchaseTicket(ticket)
    print("Purchased Ticket:")
    print(purchased_ticket)

    # Get Receipt
    receipt = client.GetReceipt(user)
    print("\nReceipt:")
    print(receipt)

    # View Users By Section
    section = "A"
    print(f"\nUsers in Section {section}:")
    for user_ticket in client.ViewUsersBySection(section):
        print(user_ticket)

    # Remove User
    removed_ticket = client.RemoveUser(user)
    print(f"\nRemoved User: {removed_ticket.user}")

    # Modify Seat
    modified_ticket = client.ModifySeat(User(first_name="John", last_name="Doe", email="john.doe@example.com"), "B")
    print(f"\nModified Seat:")
    print(modified_ticket)

if __name__ == '__main__':
    main()
