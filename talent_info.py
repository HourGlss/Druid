raw_talents = {
    "druid": [
        {
            "id": 0,
            "name": ["Lifebloom"],
            "secondary_name": False,
            "tier": 0,
            "rank_max": 1,
            "children": [1, 2, 3],
            "parents": None
        },
        {
            "id": 1,
            "name": ["Ysera's Gift"],
            "secondary_name": False,
            "tier": 0,
            "rank_max": 1,
            "children": [4],
            "parents": [0]
        },
        {
            "id": 2,
            "name": ["Nature's Swiftness"],
            "secondary_name": False,
            "tier": 0,
            "rank_max": 1,
            "children": [5],
            "parents": [0]
        },
        {
            "id": 3,
            "name": ["Omen of Clarity"],
            "secondary_name": False,
            "tier": 0,
            "rank_max": 1,
            "children": [6],
            "parents": [0]
        },
        {
            "id": 4,
            "name": ["Grove Tending"],
            "secondary_name": False,
            "tier": 0,
            "rank_max": 1,
            "children": [7, 8],
            "parents": [1]
        },
        {
            "id": 5,
            "name": ["Nature's Splendor", "Passing Seasons"],
            "secondary_name": True,
            "tier": 0,
            "rank_max": 1,
            "children": [8, 9],
            "parents": [2]
        },
        {
            "id": 6,
            "name": ["Flash of Clarity"],
            "secondary_name": False,
            "tier": 0,
            "rank_max": 1,
            "children": [9, 10],
            "parents": [3]
        },
        {
            "id": 7,
            "name": ["Waking Dream"],
            "secondary_name": False,
            "tier": 0,
            "rank_max": 1,
            "children": None,
            "parents": [4]
        },
        {
            "id": 8,
            "name": ["Improved Regrowth"],
            "secondary_name": False,
            "tier": 0,
            "rank_max": 1,
            "children": [11, 12],
            "parents": [4, 5]
        },
        {
            "id": 9,
            "name": ["Abundance", "Cenarion Ward"],
            "secondary_name": True,
            "tier": 0,
            "rank_max": 1,
            "children": [12, 13],
            "parents": [5, 6]
        },
        {
            "id": 10,
            "name": ["Nourish"],
            "secondary_name": False,
            "tier": 0,
            "rank_max": 1,
            "children": None,
            "parents": [6]
        },
        {
            "id": 11,
            "name": ["Efflorescence"],
            "secondary_name": False,
            "tier": 1,
            "rank_max": 1,
            "children": [14, 15],
            "parents": [4, 8]
        },
        {
            "id": 12,
            "name": ["Tranquility"],
            "secondary_name": False,
            "tier": 1,
            "rank_max": 1,
            "children": [16],
            "parents": [8, 9]
        },
        {
            "id": 13,
            "name": ["Ironbark"],
            "secondary_name": False,
            "tier": 1,
            "rank_max": 1,
            "children": [17, 18],
            "parents": [6, 9]
        },
        {
            "id": 14,
            "name": ["Soul of the Forest"],
            "secondary_name": False,
            "tier": 1,
            "rank_max": 1,
            "children": [19, 20, 21],
            "parents": [11]
        },
        {
            "id": 15,
            "name": ["Cultivation"],
            "secondary_name": False,
            "tier": 1,
            "rank_max": 1,
            "children": [21, 22],
            "parents": [11]
        },
        {
            "id": 16,
            "name": ["Inner Peace", "Dreamstate"],
            "secondary_name": True,
            "tier": 1,
            "rank_max": 1,
            "children": [22],
            "parents": [12]
        },
        {
            "id": 17,
            "name": ["Improved Wild Growth"],
            "secondary_name": False,
            "tier": 1,
            "rank_max": 1,
            "children": [22, 23],
            "parents": [13]
        },
        {
            "id": 18,
            "name": ["Stonebark", "Improved Ironbark"],
            "secondary_name": True,
            "tier": 1,
            "rank_max": 1,
            "children": [24, 23],
            "parents": [13]
        },
        {
            "id": 19,
            "name": ["Verdancy"],
            "secondary_name": False,
            "tier": 1,
            "rank_max": 1,
            "children": [29],
            "parents": [14]
        },
        {
            "id": 20,
            "name": ["Rampant Growth"],
            "secondary_name": False,
            "tier": 1,
            "rank_max": 1,
            "children": [25],
            "parents": [14]
        },
        {
            "id": 21,
            "name": ["Regenesis"],
            "secondary_name": False,
            "tier": 1,
            "rank_max": 2,
            "children": [25, 26],
            "parents": [14, 15]
        },
        {
            "id": 22,
            "name": ["Harmonious Blooming"],
            "secondary_name": False,
            "tier": 1,
            "rank_max": 2,
            "children": [27, 26],
            "parents": [15, 16, 17]
        },
        {
            "id": 23,
            "name": ["Unstoppable Growth"],
            "secondary_name": False,
            "tier": 1,
            "rank_max": 2,
            "children": [27, 28],
            "parents": [17, 18]
        },
        {
            "id": 24,
            "name": ["Regenerative Heartwood"],
            "secondary_name": False,
            "tier": 1,
            "rank_max": 1,
            "children": [28],
            "parents": [18]
        },
        {
            "id": 25,
            "name": ["Spring Blossoms", "Growth"],
            "secondary_name": True,
            "tier": 2,
            "rank_max": 1,
            "children": [29, 30],
            "parents": [19, 20, 21]
        },
        {
            "id": 26,
            "name": ["Incarnation: Tree of Life", "Convoke the Spirits"],
            "secondary_name": True,
            "tier": 2,
            "rank_max": 1,
            "children": [30, 31, 32],
            "parents": [21, 22]
        },
        {
            "id": 27,
            "name": ["Adaptive Swarm"],
            "secondary_name": False,
            "tier": 2,
            "rank_max": 1,
            "children": [32, 33, 34],
            "parents": [22, 23]
        },
        {
            "id": 28,
            "name": ["Verdant Infusion", "Flourish"],
            "secondary_name": True,
            "tier": 2,
            "rank_max": 1,
            "children": [34, 35, 36],
            "parents": [23, 24]
        },
        {
            "id": 29,
            "name": ["Circle of Life and Death"],
            "secondary_name": False,
            "tier": 2,
            "rank_max": 1,
            "children": [37],
            "parents": [19, 25]
        },
        {
            "id": 30,
            "name": ["Budding Leaves"],
            "secondary_name": False,
            "tier": 2,
            "rank_max": 2,
            "children": [37, 38, 39],
            "parents": [25, 26]
        },
        {
            "id": 31,
            "name": ["Cenarius' Guidance"],
            "secondary_name": False,
            "tier": 2,
            "rank_max": 1,
            "children": [39],
            "parents": [26]
        },
        {
            "id": 32,
            "name": ["Embrace of the Dream"],
            "secondary_name": False,
            "tier": 2,
            "rank_max": 2,
            "children": [39, 40],
            "parents": [26, 27]
        },
        {
            "id": 33,
            "name": ["Unbridled Swarm"],
            "secondary_name": False,
            "tier": 2,
            "rank_max": 1,
            "children": [40],
            "parents": [27]
        },
        {
            "id": 34,
            "name": ["Luxuriant Soil"],
            "secondary_name": False,
            "tier": 2,
            "rank_max": 2,
            "children": [40, 41],
            "parents": [27, 28]
        },
        {
            "id": 35,
            "name": ["Natural Wisdom"],
            "secondary_name": False,
            "tier": 2,
            "rank_max": 1,
            "children": [41],
            "parents": [28]
        },
        {
            "id": 36,
            "name": ["Nurturing Dormancy"],
            "secondary_name": False,
            "tier": 2,
            "rank_max": 1,
            "children": [41],
            "parents": [28]
        },
        {
            "id": 37,
            "name": ["Photosynthesis"],
            "secondary_name": False,
            "tier": 2,
            "rank_max": 1,
            "children": None,
            "parents": [29, 30]
        },
        {
            "id": 38,
            "name": ["Undergrowth"],
            "secondary_name": False,
            "tier": 2,
            "rank_max": 1,
            "children": None,
            "parents": [30]
        },
        {
            "id": 39,
            "name": ["Germination"],
            "secondary_name": False,
            "tier": 2,
            "rank_max": 1,
            "children": None,
            "parents": [30, 31, 32]
        },
        {
            "id": 40,
            "name": ["Reforestation"],
            "secondary_name": False,
            "tier": 2,
            "rank_max": 1,
            "children": None,
            "parents": [32, 33, 34]
        },
        {
            "id": 41,
            "name": ["Power of the Archdruid", "Invigorate"],
            "secondary_name": True,
            "tier": 2,
            "rank_max": 1,
            "children": None,
            "parents": [34, 35, 36]
        }
    ]
}
