import pygame
import socket
import select
from board import ChessBoard
from UserInterface import UserInterface

def main():
    pygame.init()
    screen = pygame.display.set_mode((600, 600))
    pygame.display.set_caption('Pawn Game')
    clock = pygame.time.Clock()

    # Initialize game state
    board = ChessBoard()
    ui = UserInterface(screen, board)
    color = None  # Track player color
    running = True

    # Setup the socket
    socketObject = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socketObject.connect(("localhost", 9999))
    socketObject.setblocking(0)  # Set the socket to non-blocking mode

    while running:
        # Handle Pygame events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Non-blocking network message check
        ready_to_read, _, _ = select.select([socketObject], [], [], 0)
        if ready_to_read:
            data = socketObject.recv(1024).decode()
            if data:
                print("Received data:", data)
                # Process the received data
                if data.startswith("Time"):
                    time = int(data[4:]) * 60
                    ui.updateTimer(time)
                    msg = "OK"
                    socketObject.send(msg.encode())

                elif data.startswith("Setup"):
                    ui.setupBoard(data)
                    ui.drawComponent()

                elif data == "White" or data == "Black":
                    color = data
                    ui.playerColor = color
                    ui.drawComponent()

                elif data == "Your turn":
                    move, flag = ui.clientMove()  # This should be adapted if it blocks
                    msg = move if flag == 0 else ("Win" if flag == -1 else "Lost")
                    socketObject.send(msg.encode())

                elif data == "Begin":
                    ui.firstgame = True
                    ui.drawComponent()

                elif data == "exit":
                    print("Server requested close.")
                    running = False

                else:
                    ui.drawComponent()

        # Refresh the game screen
        ui.drawComponent()
        pygame.display.flip()
        clock.tick(60)

    pygame.quit()
    socketObject.close()

if __name__ == "__main__":
    main()
