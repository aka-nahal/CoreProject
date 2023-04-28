from shinobi.builder.theme import AnimeThemeBuilder


def test_theme_builder():
    builder = AnimeThemeBuilder()
    data_dictionary = builder.build_dictionary()
    assert list(data_dictionary.keys()) == [
        50,
        51,
        52,
        53,
        54,
        81,
        55,
        39,
        56,
        57,
        58,
        35,
        59,
        13,
        60,
        61,
        62,
        63,
        64,
        65,
        66,
        17,
        18,
        67,
        38,
        19,
        6,
        68,
        69,
        20,
        70,
        71,
        40,
        3,
        72,
        73,
        74,
        21,
        23,
        75,
        29,
        11,
        31,
        76,
        77,
        78,
        32,
        79,
        80,
        48,
    ]
    assert list(data_dictionary.values()) == [
        "https://myanimelist.net/anime/genre/50/Adult_Cast",
        "https://myanimelist.net/anime/genre/51/Anthropomorphic",
        "https://myanimelist.net/anime/genre/52/CGDCT",
        "https://myanimelist.net/anime/genre/53/Childcare",
        "https://myanimelist.net/anime/genre/54/Combat_Sports",
        "https://myanimelist.net/anime/genre/81/Crossdressing",
        "https://myanimelist.net/anime/genre/55/Delinquents",
        "https://myanimelist.net/anime/genre/39/Detective",
        "https://myanimelist.net/anime/genre/56/Educational",
        "https://myanimelist.net/anime/genre/57/Gag_Humor",
        "https://myanimelist.net/anime/genre/58/Gore",
        "https://myanimelist.net/anime/genre/35/Harem",
        "https://myanimelist.net/anime/genre/59/High_Stakes_Game",
        "https://myanimelist.net/anime/genre/13/Historical",
        "https://myanimelist.net/anime/genre/60/Idols_Female",
        "https://myanimelist.net/anime/genre/61/Idols_Male",
        "https://myanimelist.net/anime/genre/62/Isekai",
        "https://myanimelist.net/anime/genre/63/Iyashikei",
        "https://myanimelist.net/anime/genre/64/Love_Polygon",
        "https://myanimelist.net/anime/genre/65/Magical_Sex_Shift",
        "https://myanimelist.net/anime/genre/66/Mahou_Shoujo",
        "https://myanimelist.net/anime/genre/17/Martial_Arts",
        "https://myanimelist.net/anime/genre/18/Mecha",
        "https://myanimelist.net/anime/genre/67/Medical",
        "https://myanimelist.net/anime/genre/38/Military",
        "https://myanimelist.net/anime/genre/19/Music",
        "https://myanimelist.net/anime/genre/6/Mythology",
        "https://myanimelist.net/anime/genre/68/Organized_Crime",
        "https://myanimelist.net/anime/genre/69/Otaku_Culture",
        "https://myanimelist.net/anime/genre/20/Parody",
        "https://myanimelist.net/anime/genre/70/Performing_Arts",
        "https://myanimelist.net/anime/genre/71/Pets",
        "https://myanimelist.net/anime/genre/40/Psychological",
        "https://myanimelist.net/anime/genre/3/Racing",
        "https://myanimelist.net/anime/genre/72/Reincarnation",
        "https://myanimelist.net/anime/genre/73/Reverse_Harem",
        "https://myanimelist.net/anime/genre/74/Romantic_Subtext",
        "https://myanimelist.net/anime/genre/21/Samurai",
        "https://myanimelist.net/anime/genre/23/School",
        "https://myanimelist.net/anime/genre/75/Showbiz",
        "https://myanimelist.net/anime/genre/29/Space",
        "https://myanimelist.net/anime/genre/11/Strategy_Game",
        "https://myanimelist.net/anime/genre/31/Super_Power",
        "https://myanimelist.net/anime/genre/76/Survival",
        "https://myanimelist.net/anime/genre/77/Team_Sports",
        "https://myanimelist.net/anime/genre/78/Time_Travel",
        "https://myanimelist.net/anime/genre/32/Vampire",
        "https://myanimelist.net/anime/genre/79/Video_Game",
        "https://myanimelist.net/anime/genre/80/Visual_Arts",
        "https://myanimelist.net/anime/genre/48/Workplace",
    ]