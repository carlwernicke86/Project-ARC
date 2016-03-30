__author__ = 'cardg_000'

# Uppercase is static object, Lowercase are moving objects
# G is ground/ Wall. This should always be on the bottom of the level
# P is platform
# Numbers represent corresponding rooms
# e is enemy
# O means outside
# S is starting point

room_template = [
            "                                                                                                         ",
            "                                                                                                         ",
            "                                                                                                         ",
            "                                                                                                         ",
            "                                                                                                         ",
            "                                                                                                         ",
            "                                                                                                         ",
            "                                                                                                         ",
            "                                                                                                         ",
            "                                                                                                         ",
            "                                                                                                         ",
            "                                                                                                         ",
            "                                                                                                         ",
            "GGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGG"]

room_outside = [
            "                                                                                                         ",
            "                                                                                                         ",
            "                                                                                                         ",
            "                                                                                                         ",
            "                                                                                                         ",
            "                                                                                                         ",
            "                                                                                                         ",
            "                                                     PPPPPP                                              ",
            "                                                                                                         ",
            "                                                  P                                                      ",
            "                                                  P                                                      ",
            "                 PPPPP                            P                                                      ",
            "      S                               E           P               e                       1              ",
            "GGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGG"]




room_01 = [
            "GGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGG",
            "G                                                                                                       G",
            "G                        e                                 PPPPPPPPPPPPP                                G",
            "G                    PPPPPPP                                                                            G",
            "G                                                                                                       G",
            "G                                    PPPPPPPPPPPPPPP                                                    G",
            "G                                                                                                       G",
            "G                         PPPPP                                      E                                  G",
            "G                                                              PPPPPPPPPPPPP                            G",
            "G                 PPPP                                                                                  G",
            "G                                                                                                       G",
            "G          PPPPP                   P                                                                    G",
            "G O                       P        P             e                                                  2   G",
            "GGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGG"]

room_02 = [
            "                                                                                                         ",
            "                                                                                                         ",
            "                                                                                                         ",
            "                                                                                                         ",
            "                                                                                                         ",
            "                                                                                                         ",
            "                                                                                                         ",
            "                                                                                                         ",
            "                                                                                                         ",
            "                                                                                                         ",
            "                                                                                                         ",
            "                                                                                                         ",
            "       1                                                                                                 ",
            "GGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGG"]