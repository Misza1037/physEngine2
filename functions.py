def check_events(screen):
    """ Reakcja na zdarzenia."""
    for event in pg.event.get():
        # Quitting the game
        if event.type == pg.QUIT or event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE:
            sys.exit()

            
def update_screen(screen, player, tears, flies):
    """Aktualizowanie ekranu."""
    # DRAWING
    screen.fill((130, 0, 230))

    # WYWOŁYWANIE RYSOWANIA OBIEKTÓW NA EKRANIE

    # SHOWING SCREEN
    pg.display.flip()


def update_tick():
    """Regulacja mechanizmów gry."""
    #TU SĄ OBLICZENIA SIŁ I POZYCJI KTÓRE ZACHODZĄ DLA POSZCZEGÓLNYCH OBIEKTÓW
