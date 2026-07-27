"""
Mock data for TreeSaathi
Tables: User, Tree, adopter, activity_log

Relationships:
- Tree.owner_id      -> User.id        (nullable, 1 user : many trees)
- adopter.tree_id    -> Tree.id        (many adopters : 1 tree, max 10 per tree)
- adopter.user_id    -> User.id        (1 user : many adoptions)
- activity_log.tree_id -> Tree.id
- activity_log.user_id -> User.id
"""

from datetime import datetime, timedelta

# ---------------------------------------------------------------------------
# USER  (id is the 1-based index/position in this list, i.e. mockUsers[0] -> id 1)
# ---------------------------------------------------------------------------
mockUsers = [
    {"id": 1,  "username": "arjun_singh",     "email": "arjun.singh@gmail.com",     "password_hash": "$2b$12$aX1kQz9F0e9tYh1nQe0uQe", "name": "Arjun Singh",      "phone": "306-555-0101", "verified": True,  "notification_preferences": {"email": True,  "sms": False}, "created_at": "2023-04-11T09:15:00Z"},
    {"id": 2,  "username": "meera_patel",     "email": "meera.patel@gmail.com",     "password_hash": "$2b$12$bX2kQz9F0e9tYh1nQe0uRf", "name": "Meera Patel",      "phone": "306-555-0102", "verified": True,  "notification_preferences": {"email": True,  "sms": True},  "created_at": "2023-04-15T11:02:00Z"},
    {"id": 3,  "username": "liam_oconnor",    "email": "liam.oconnor@outlook.com",  "password_hash": "$2b$12$cX3kQz9F0e9tYh1nQe0uSg", "name": "Liam O'Connor",    "phone": "306-555-0103", "verified": False, "notification_preferences": {"email": False, "sms": False}, "created_at": "2023-05-02T14:30:00Z"},
    {"id": 4,  "username": "priya_shah",      "email": "priya.shah@yahoo.com",      "password_hash": "$2b$12$dX4kQz9F0e9tYh1nQe0uTh", "name": "Priya Shah",       "phone": "306-555-0104", "verified": True,  "notification_preferences": {"email": True,  "sms": False}, "created_at": "2023-05-19T08:45:00Z"},
    {"id": 5,  "username": "noah_bird",       "email": "noah.bird@gmail.com",       "password_hash": "$2b$12$eX5kQz9F0e9tYh1nQe0uUi", "name": "Noah Bird",        "phone": "306-555-0105", "verified": True,  "notification_preferences": {"email": True,  "sms": True},  "created_at": "2023-06-01T10:00:00Z"},
    {"id": 6,  "username": "sana_khan",       "email": "sana.khan@gmail.com",       "password_hash": "$2b$12$fX6kQz9F0e9tYh1nQe0uVj", "name": "Sana Khan",        "phone": "306-555-0106", "verified": True,  "notification_preferences": {"email": False, "sms": True},  "created_at": "2023-06-10T13:20:00Z"},
    {"id": 7,  "username": "ethan_wong",      "email": "ethan.wong@hotmail.com",    "password_hash": "$2b$12$gX7kQz9F0e9tYh1nQe0uWk", "name": "Ethan Wong",       "phone": "306-555-0107", "verified": False, "notification_preferences": {"email": True,  "sms": False}, "created_at": "2023-06-22T16:05:00Z"},
    {"id": 8,  "username": "fatima_ali",      "email": "fatima.ali@gmail.com",      "password_hash": "$2b$12$hX8kQz9F0e9tYh1nQe0uXl", "name": "Fatima Ali",       "phone": "306-555-0108", "verified": True,  "notification_preferences": {"email": True,  "sms": True},  "created_at": "2023-07-03T09:40:00Z"},
    {"id": 9,  "username": "carter_dubois",   "email": "carter.dubois@gmail.com",   "password_hash": "$2b$12$iX9kQz9F0e9tYh1nQe0uYm", "name": "Carter Dubois",    "phone": "306-555-0109", "verified": True,  "notification_preferences": {"email": True,  "sms": False}, "created_at": "2023-07-14T12:12:00Z"},
    {"id": 10, "username": "yuki_tanaka",     "email": "yuki.tanaka@gmail.com",     "password_hash": "$2b$12$jXakQz9F0e9tYh1nQe0uZn", "name": "Yuki Tanaka",      "phone": "306-555-0110", "verified": False, "notification_preferences": {"email": False, "sms": False}, "created_at": "2023-07-28T15:55:00Z"},
    {"id": 11, "username": "oliver_bear",     "email": "oliver.bear@gmail.com",     "password_hash": "$2b$12$kXbkQz9F0e9tYh1nQe0u1o", "name": "Oliver Bear",      "phone": "306-555-0111", "verified": True,  "notification_preferences": {"email": True,  "sms": True},  "created_at": "2023-08-05T09:00:00Z"},
    {"id": 12, "username": "grace_ironeagle", "email": "grace.ironeagle@gmail.com", "password_hash": "$2b$12$lXckQz9F0e9tYh1nQe0u2p", "name": "Grace Ironeagle",  "phone": "306-555-0112", "verified": True,  "notification_preferences": {"email": True,  "sms": False}, "created_at": "2023-08-19T11:25:00Z"},
    {"id": 13, "username": "mateo_lopez",     "email": "mateo.lopez@gmail.com",     "password_hash": "$2b$12$mXdkQz9F0e9tYh1nQe0u3q", "name": "Mateo Lopez",      "phone": "306-555-0113", "verified": False, "notification_preferences": {"email": False, "sms": True},  "created_at": "2023-09-02T14:10:00Z"},
    {"id": 14, "username": "chloe_wiebe",     "email": "chloe.wiebe@gmail.com",     "password_hash": "$2b$12$nXekQz9F0e9tYh1nQe0u4r", "name": "Chloe Wiebe",      "phone": "306-555-0114", "verified": True,  "notification_preferences": {"email": True,  "sms": True},  "created_at": "2023-09-16T08:35:00Z"},
    {"id": 15, "username": "daniel_okafor",   "email": "daniel.okafor@gmail.com",   "password_hash": "$2b$12$oXfkQz9F0e9tYh1nQe0u5s", "name": "Daniel Okafor",    "phone": "306-555-0115", "verified": True,  "notification_preferences": {"email": True,  "sms": False}, "created_at": "2023-09-30T17:48:00Z"},
    {"id": 16, "username": "isabella_romano", "email": "isabella.romano@gmail.com", "password_hash": "$2b$12$pXgkQz9F0e9tYh1nQe0u6t", "name": "Isabella Romano",  "phone": "306-555-0116", "verified": False, "notification_preferences": {"email": True,  "sms": False}, "created_at": "2023-10-13T10:20:00Z"},
    {"id": 17, "username": "jack_thunderbird","email": "jack.thunderbird@gmail.com","password_hash": "$2b$12$qXhkQz9F0e9tYh1nQe0u7u", "name": "Jack Thunderbird", "phone": "306-555-0117", "verified": True,  "notification_preferences": {"email": False, "sms": True},  "created_at": "2023-10-27T13:00:00Z"},
    {"id": 18, "username": "hannah_kim",      "email": "hannah.kim@gmail.com",      "password_hash": "$2b$12$rXikQz9F0e9tYh1nQe0u8v", "name": "Hannah Kim",       "phone": "306-555-0118", "verified": True,  "notification_preferences": {"email": True,  "sms": True},  "created_at": "2023-11-09T09:55:00Z"},
    {"id": 19, "username": "lucas_ferreira",  "email": "lucas.ferreira@gmail.com",  "password_hash": "$2b$12$sXjkQz9F0e9tYh1nQe0u9w", "name": "Lucas Ferreira",   "phone": "306-555-0119", "verified": False, "notification_preferences": {"email": False, "sms": False}, "created_at": "2023-11-22T16:40:00Z"},
    {"id": 20, "username": "aaliyah_moosomin", "email": "aaliyah.moosomin@gmail.com", "password_hash": "$2b$12$tXkkQz9F0e9tYh1nQe0uAx", "name": "Aaliyah Moosomin", "phone": "306-555-0120", "verified": True,  "notification_preferences": {"email": True,  "sms": True},  "created_at": "2023-12-05T12:15:00Z"},
]

# ---------------------------------------------------------------------------
# TREE  (id = 1-based position; owner_id references mockUsers[i]["id"] or None
#        for community-planted / unclaimed trees)
# ---------------------------------------------------------------------------
mockTrees = [
    {"id": 1,  "species": "American Elm",          "owner_id": 1,    "description": "Mature shade tree with broad canopy", "height": 12.5, "diameter": 0.42, "planting_date": "2018-05-10", "verified": True,  "last_activity": "2026-06-20T10:00:00Z", "status": "healthy",     "latitude": 50.435012, "longitude": -104.615034, "address": "Near the entrance of Wascana Park"},
    {"id": 2,  "species": "Bur Oak",                "owner_id": None, "description": "Young oak planted by city crew",     "height": 5.2,  "diameter": 0.12, "planting_date": "2022-09-14", "verified": True,  "last_activity": "2026-07-01T09:30:00Z", "status": "healthy",     "latitude": 50.448021, "longitude": -104.610011, "address": "Next to the downtown public library"},
    {"id": 3,  "species": "Manitoba Maple",         "owner_id": 2,    "description": "Front-yard tree, needs pruning",     "height": 8.0,  "diameter": 0.25, "planting_date": "2020-06-01", "verified": False, "last_activity": "2026-05-15T14:20:00Z", "status": "needs_care",  "latitude": 50.452145, "longitude": -104.621458, "address": "Front yard of a brick house in Cathedral area"},
    {"id": 4,  "species": "White Spruce",           "owner_id": 3,    "description": "Tall evergreen behind campus",       "height": 15.3, "diameter": 0.55, "planting_date": "2015-04-22", "verified": True,  "last_activity": "2026-06-28T11:10:00Z", "status": "healthy",     "latitude": 50.415099, "longitude": -104.590022, "address": "Behind the university campus buildings"},
    {"id": 5,  "species": "Green Ash",               "owner_id": None, "description": "Sapling near bus stop",              "height": 4.1,  "diameter": 0.08, "planting_date": "2023-05-30", "verified": False, "last_activity": "2026-04-02T08:00:00Z", "status": "at_risk",     "latitude": 50.470055, "longitude": -104.630045, "address": "Close to the transit stop"},
    {"id": 6,  "species": "Paper Birch",             "owner_id": 4,    "description": "Multi-stem birch along the trail",   "height": 7.2,  "diameter": 0.20, "planting_date": "2019-10-05", "verified": True,  "last_activity": "2026-07-10T15:45:00Z", "status": "healthy",     "latitude": 50.485012, "longitude": -104.670088, "address": "Along the Devonian Pathway"},
    {"id": 7,  "species": "Colorado Blue Spruce",    "owner_id": 5,    "description": "Ornamental spruce, well maintained", "height": 10.0, "diameter": 0.38, "planting_date": "2017-06-18", "verified": True,  "last_activity": "2026-06-05T13:00:00Z", "status": "healthy",     "latitude": 50.510044, "longitude": -104.600077, "address": "Corner of a residential intersection in the north end"},
    {"id": 8,  "species": "Cottonwood",              "owner_id": None, "description": "Large legacy cottonwood by creek",   "height": 20.5, "diameter": 0.90, "planting_date": "2001-05-01", "verified": True,  "last_activity": "2026-06-30T09:20:00Z", "status": "healthy",     "latitude": 50.420088, "longitude": -104.750012, "address": "Growing near Wascana Creek"},
    {"id": 9,  "species": "Trembling Aspen",         "owner_id": 6,    "description": "Fast-growing aspen cluster",         "height": 11.4, "diameter": 0.30, "planting_date": "2019-05-12", "verified": False, "last_activity": "2026-03-18T10:40:00Z", "status": "needs_care",  "latitude": 50.440023, "longitude": -104.450099, "address": "Bordering the eastern industrial park"},
    {"id": 10, "species": "Weeping Willow",          "owner_id": 7,    "description": "Iconic willow over drainage pond",   "height": 6.8,  "diameter": 0.22, "planting_date": "2021-04-25", "verified": True,  "last_activity": "2026-07-05T12:30:00Z", "status": "healthy",     "latitude": 50.530015, "longitude": -104.700055, "address": "By the neighborhood drainage pond"},
    {"id": 11, "species": "Silver Maple",            "owner_id": 8,    "description": "Roadside maple, good canopy cover",  "height": 9.6,  "diameter": 0.33, "planting_date": "2020-05-20", "verified": True,  "last_activity": "2026-06-12T08:50:00Z", "status": "healthy",     "latitude": 50.460077, "longitude": -104.580041, "address": "Along a residential boulevard in Lakeview"},
    {"id": 12, "species": "Jack Pine",               "owner_id": None, "description": "Naturally regenerated pine",         "height": 6.3,  "diameter": 0.18, "planting_date": "2021-09-01", "verified": False, "last_activity": "2026-02-14T09:00:00Z", "status": "at_risk",     "latitude": 50.499033, "longitude": -104.640012, "address": "Edge of the greenway near the ring road"},
    {"id": 13, "species": "Norway Maple",            "owner_id": 9,    "description": "Ornamental street tree",             "height": 8.9,  "diameter": 0.27, "planting_date": "2018-05-08", "verified": True,  "last_activity": "2026-06-22T14:00:00Z", "status": "healthy",     "latitude": 50.443067, "longitude": -104.601099, "address": "Boulevard tree in the Heritage neighborhood"},
    {"id": 14, "species": "Blue Spruce",             "owner_id": 10,   "description": "Backyard evergreen windbreak",       "height": 13.2, "diameter": 0.44, "planting_date": "2014-05-30", "verified": True,  "last_activity": "2026-05-28T10:15:00Z", "status": "healthy",     "latitude": 50.472011, "longitude": -104.560088, "address": "Backyard windbreak in the Rosemont area"},
    {"id": 15, "species": "Hackberry",               "owner_id": None, "description": "Recently planted drought-tolerant", "height": 3.5,  "diameter": 0.07, "planting_date": "2024-05-15", "verified": False, "last_activity": "2026-04-20T11:00:00Z", "status": "healthy",     "latitude": 50.428099, "longitude": -104.690034, "address": "New boulevard planting on 13th Avenue"},
    {"id": 16, "species": "Red Oak",                 "owner_id": 11,   "description": "Ornamental oak with fall colour",    "height": 7.8,  "diameter": 0.24, "planting_date": "2019-09-22", "verified": True,  "last_activity": "2026-06-08T13:25:00Z", "status": "healthy",     "latitude": 50.455028, "longitude": -104.520077, "address": "Front lawn in the Eastview neighborhood"},
    {"id": 17, "species": "Basswood",                "owner_id": 12,   "description": "Fragrant flowering basswood",        "height": 10.7, "diameter": 0.36, "planting_date": "2016-05-01", "verified": True,  "last_activity": "2026-06-18T09:10:00Z", "status": "healthy",     "latitude": 50.467055, "longitude": -104.610099, "address": "Park boulevard near the community centre"},
    {"id": 18, "species": "Manitoba Maple",          "owner_id": None, "description": "Volunteer sapling, unclaimed",       "height": 2.9,  "diameter": 0.05, "planting_date": "2024-06-02", "verified": False, "last_activity": "2026-01-30T08:00:00Z", "status": "at_risk",     "latitude": 50.481066, "longitude": -104.655012, "address": "Vacant lot near the rail yard"},
    {"id": 19, "species": "Scots Pine",              "owner_id": 13,   "description": "Windbreak pine in good condition",   "height": 9.1,  "diameter": 0.29, "planting_date": "2017-05-19", "verified": True,  "last_activity": "2026-06-01T15:30:00Z", "status": "healthy",     "latitude": 50.491022, "longitude": -104.670099, "address": "Farmstead edge near the city limits"},
    {"id": 20, "species": "American Basswood",       "owner_id": 14,   "description": "Community-planted memorial tree",    "height": 5.0,  "diameter": 0.14, "planting_date": "2022-06-05", "verified": True,  "last_activity": "2026-05-10T10:45:00Z", "status": "healthy",     "latitude": 50.437081, "longitude": -104.601056, "address": "Memorial grove in Wascana Park"},
    {"id": 21, "species": "Green Ash",               "owner_id": 15,   "description": "Backyard shade tree",                "height": 6.4,  "diameter": 0.19, "planting_date": "2020-05-25", "verified": False, "last_activity": "2026-03-05T09:00:00Z", "status": "needs_care",  "latitude": 50.449011, "longitude": -104.640077, "address": "Backyard in the Al Ritchie neighborhood"},
    {"id": 22, "species": "Colorado Blue Spruce",    "owner_id": None, "description": "Corner-lot evergreen",               "height": 14.0, "diameter": 0.48, "planting_date": "2013-05-14", "verified": True,  "last_activity": "2026-06-25T12:00:00Z", "status": "healthy",     "latitude": 50.503099, "longitude": -104.590033, "address": "Corner lot in the Uplands neighborhood"},
    {"id": 23, "species": "Trembling Aspen",         "owner_id": 16,   "description": "Small aspen grove start",            "height": 4.7,  "diameter": 0.10, "planting_date": "2023-05-03", "verified": False, "last_activity": "2026-04-14T08:30:00Z", "status": "healthy",     "latitude": 50.416055, "longitude": -104.520044, "address": "Edge of a new subdivision"},
    {"id": 24, "species": "White Spruce",            "owner_id": 17,   "description": "Windbreak row, well established",    "height": 16.8, "diameter": 0.60, "planting_date": "2008-05-09", "verified": True,  "last_activity": "2026-06-15T11:20:00Z", "status": "healthy",     "latitude": 50.522066, "longitude": -104.680011, "address": "Windbreak along a farm access road"},
    {"id": 25, "species": "Bur Oak",                 "owner_id": 18,   "description": "Heritage oak, over 40 years old",    "height": 18.2, "diameter": 0.75, "planting_date": "1985-05-01", "verified": True,  "last_activity": "2026-07-02T14:50:00Z", "status": "healthy",     "latitude": 50.433044, "longitude": -104.650088, "address": "Heritage property in the Cathedral area"},
]

# ---------------------------------------------------------------------------
# ADOPTER  (junction table: many users <-> many trees, max 10 adopters/tree,
#           UNIQUE(tree_id, user_id))
# ---------------------------------------------------------------------------
mockAdopters = [
    {"id": 1,  "tree_id": 2,  "user_id": 1,  "adopted_at": "2024-05-01T09:00:00Z"},
    {"id": 2,  "tree_id": 2,  "user_id": 6,  "adopted_at": "2024-05-03T10:15:00Z"},
    {"id": 3,  "tree_id": 5,  "user_id": 2,  "adopted_at": "2024-06-10T11:30:00Z"},
    {"id": 4,  "tree_id": 5,  "user_id": 8,  "adopted_at": "2024-06-12T13:00:00Z"},
    {"id": 5,  "tree_id": 5,  "user_id": 9,  "adopted_at": "2024-06-15T14:45:00Z"},
    {"id": 6,  "tree_id": 8,  "user_id": 3,  "adopted_at": "2024-04-20T08:20:00Z"},
    {"id": 7,  "tree_id": 8,  "user_id": 10, "adopted_at": "2024-04-25T09:40:00Z"},
    {"id": 8,  "tree_id": 12, "user_id": 4,  "adopted_at": "2024-07-01T10:00:00Z"},
    {"id": 9,  "tree_id": 12, "user_id": 11, "adopted_at": "2024-07-03T12:10:00Z"},
    {"id": 10, "tree_id": 12, "user_id": 13, "adopted_at": "2024-07-05T15:00:00Z"},
    {"id": 11, "tree_id": 15, "user_id": 5,  "adopted_at": "2024-08-11T09:30:00Z"},
    {"id": 12, "tree_id": 15, "user_id": 14, "adopted_at": "2024-08-14T11:00:00Z"},
    {"id": 13, "tree_id": 18, "user_id": 7,  "adopted_at": "2024-09-02T10:20:00Z"},
    {"id": 14, "tree_id": 18, "user_id": 16, "adopted_at": "2024-09-05T13:15:00Z"},
    {"id": 15, "tree_id": 18, "user_id": 19, "adopted_at": "2024-09-08T16:00:00Z"},
    {"id": 16, "tree_id": 22, "user_id": 12, "adopted_at": "2024-10-01T09:10:00Z"},
    {"id": 17, "tree_id": 22, "user_id": 15, "adopted_at": "2024-10-04T10:45:00Z"},
    {"id": 18, "tree_id": 1,  "user_id": 20, "adopted_at": "2024-05-20T08:00:00Z"},
    {"id": 19, "tree_id": 9,  "user_id": 17, "adopted_at": "2024-06-30T14:00:00Z"},
    {"id": 20, "tree_id": 21, "user_id": 18, "adopted_at": "2024-11-11T09:50:00Z"},
    {"id": 21, "tree_id": 21, "user_id": 4,  "adopted_at": "2024-11-14T11:20:00Z"},
    {"id": 22, "tree_id": 5,  "user_id": 13, "adopted_at": "2024-06-18T09:00:00Z"},
    {"id": 23, "tree_id": 12, "user_id": 6,  "adopted_at": "2024-07-09T10:30:00Z"},
]

# ---------------------------------------------------------------------------
# ACTIVITY_LOG  (action_type: plant / adopt / water)
# ---------------------------------------------------------------------------
mockActivityLog = [
    {"id": 1,  "user_id": 1,  "tree_id": 1,  "action_type": "plant", "timestamp": "2018-05-10T09:00:00Z"},
    {"id": 2,  "user_id": 1,  "tree_id": 2,  "action_type": "adopt", "timestamp": "2024-05-01T09:00:00Z"},
    {"id": 3,  "user_id": 1,  "tree_id": 2,  "action_type": "water", "timestamp": "2026-06-20T10:00:00Z"},
    {"id": 4,  "user_id": 6,  "tree_id": 2,  "action_type": "adopt", "timestamp": "2024-05-03T10:15:00Z"},
    {"id": 5,  "user_id": 6,  "tree_id": 2,  "action_type": "water", "timestamp": "2026-07-01T09:30:00Z"},
    {"id": 6,  "user_id": 2,  "tree_id": 3,  "action_type": "plant", "timestamp": "2020-06-01T08:00:00Z"},
    {"id": 7,  "user_id": 2,  "tree_id": 5,  "action_type": "adopt", "timestamp": "2024-06-10T11:30:00Z"},
    {"id": 8,  "user_id": 2,  "tree_id": 5,  "action_type": "water", "timestamp": "2026-04-02T08:00:00Z"},
    {"id": 9,  "user_id": 3,  "tree_id": 4,  "action_type": "plant", "timestamp": "2015-04-22T08:00:00Z"},
    {"id": 10, "user_id": 3,  "tree_id": 8,  "action_type": "adopt", "timestamp": "2024-04-20T08:20:00Z"},
    {"id": 11, "user_id": 3,  "tree_id": 8,  "action_type": "water", "timestamp": "2026-06-30T09:20:00Z"},
    {"id": 12, "user_id": 4,  "tree_id": 6,  "action_type": "plant", "timestamp": "2019-10-05T08:00:00Z"},
    {"id": 13, "user_id": 4,  "tree_id": 12, "action_type": "adopt", "timestamp": "2024-07-01T10:00:00Z"},
    {"id": 14, "user_id": 4,  "tree_id": 21, "action_type": "adopt", "timestamp": "2024-11-14T11:20:00Z"},
    {"id": 15, "user_id": 5,  "tree_id": 7,  "action_type": "plant", "timestamp": "2017-06-18T08:00:00Z"},
    {"id": 16, "user_id": 5,  "tree_id": 15, "action_type": "adopt", "timestamp": "2024-08-11T09:30:00Z"},
    {"id": 17, "user_id": 5,  "tree_id": 15, "action_type": "water", "timestamp": "2026-04-20T11:00:00Z"},
    {"id": 18, "user_id": 8,  "tree_id": 11, "action_type": "plant", "timestamp": "2020-05-20T08:00:00Z"},
    {"id": 19, "user_id": 8,  "tree_id": 5,  "action_type": "adopt", "timestamp": "2024-06-12T13:00:00Z"},
    {"id": 20, "user_id": 9,  "tree_id": 13, "action_type": "plant", "timestamp": "2018-05-08T08:00:00Z"},
    {"id": 21, "user_id": 9,  "tree_id": 5,  "action_type": "adopt", "timestamp": "2024-06-15T14:45:00Z"},
    {"id": 22, "user_id": 10, "tree_id": 14, "action_type": "plant", "timestamp": "2014-05-30T08:00:00Z"},
    {"id": 23, "user_id": 10, "tree_id": 8,  "action_type": "adopt", "timestamp": "2024-04-25T09:40:00Z"},
    {"id": 24, "user_id": 10, "tree_id": 8,  "action_type": "water", "timestamp": "2026-06-30T09:25:00Z"},
    {"id": 25, "user_id": 11, "tree_id": 16, "action_type": "plant", "timestamp": "2019-09-22T08:00:00Z"},
    {"id": 26, "user_id": 11, "tree_id": 12, "action_type": "adopt", "timestamp": "2024-07-03T12:10:00Z"},
    {"id": 27, "user_id": 12, "tree_id": 17, "action_type": "plant", "timestamp": "2016-05-01T08:00:00Z"},
    {"id": 28, "user_id": 12, "tree_id": 22, "action_type": "adopt", "timestamp": "2024-10-01T09:10:00Z"},
    {"id": 29, "user_id": 12, "tree_id": 22, "action_type": "water", "timestamp": "2026-06-25T12:00:00Z"},
    {"id": 30, "user_id": 13, "tree_id": 19, "action_type": "plant", "timestamp": "2017-05-19T08:00:00Z"},
    {"id": 31, "user_id": 13, "tree_id": 12, "action_type": "adopt", "timestamp": "2024-07-05T15:00:00Z"},
    {"id": 32, "user_id": 13, "tree_id": 5,  "action_type": "adopt", "timestamp": "2024-06-18T09:00:00Z"},
    {"id": 33, "user_id": 14, "tree_id": 20, "action_type": "plant", "timestamp": "2022-06-05T08:00:00Z"},
    {"id": 34, "user_id": 14, "tree_id": 15, "action_type": "adopt", "timestamp": "2024-08-14T11:00:00Z"},
    {"id": 35, "user_id": 15, "tree_id": 21, "action_type": "plant", "timestamp": "2020-05-25T08:00:00Z"},
    {"id": 36, "user_id": 15, "tree_id": 22, "action_type": "adopt", "timestamp": "2024-10-04T10:45:00Z"},
    {"id": 37, "user_id": 16, "tree_id": 23, "action_type": "plant", "timestamp": "2023-05-03T08:00:00Z"},
    {"id": 38, "user_id": 16, "tree_id": 18, "action_type": "adopt", "timestamp": "2024-09-05T13:15:00Z"},
    {"id": 39, "user_id": 17, "tree_id": 24, "action_type": "plant", "timestamp": "2008-05-09T08:00:00Z"},
    {"id": 40, "user_id": 17, "tree_id": 9,  "action_type": "adopt", "timestamp": "2024-06-30T14:00:00Z"},
    {"id": 41, "user_id": 17, "tree_id": 9,  "action_type": "water", "timestamp": "2026-03-18T10:40:00Z"},
    {"id": 42, "user_id": 18, "tree_id": 25, "action_type": "plant", "timestamp": "1985-05-01T08:00:00Z"},
    {"id": 43, "user_id": 18, "tree_id": 21, "action_type": "adopt", "timestamp": "2024-11-11T09:50:00Z"},
    {"id": 44, "user_id": 19, "tree_id": 18, "action_type": "adopt", "timestamp": "2024-09-08T16:00:00Z"},
    {"id": 45, "user_id": 20, "tree_id": 1,  "action_type": "adopt", "timestamp": "2024-05-20T08:00:00Z"},
    {"id": 46, "user_id": 20, "tree_id": 1,  "action_type": "water", "timestamp": "2026-06-20T10:05:00Z"},
    {"id": 47, "user_id": 6,  "tree_id": 12, "action_type": "adopt", "timestamp": "2024-07-09T10:30:00Z"},
    {"id": 48, "user_id": 7,  "tree_id": 18, "action_type": "adopt", "timestamp": "2024-09-02T10:20:00Z"},
]

if __name__ == "__main__":
    print(f"Users: {len(mockUsers)}")
    print(f"Trees: {len(mockTrees)}")
    print(f"Adopters: {len(mockAdopters)}")
    print(f"Activity log entries: {len(mockActivityLog)}")