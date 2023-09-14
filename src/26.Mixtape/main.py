# Mixtape.
#Theme: Travel Songs

playlist = ['Porches - rangerover',
            'Mount Eerie - You Swan, Go On',
            'Carolyn Polachek - Look at Me Now',
            'Pinegrove - Darkness',
            'LVP UP - Spirit Was',
            'Mitski - First Love / Late Spring',
]
print(playlist)

for song in playlist:
    print(song)

for i in range(len(playlist)):
    if i == len(playlist) -1:
        print(playlist[i])
    else:
        print(playlist[i] + playlist[i + 1])
       